"""
LLM Pricing Data Collection Service
Collects and normalizes pricing data from multiple LLM providers

Extracted from inspiration repos:
  llm-prices, llm-prices-data, llmpricing, model-specs, model-catalog,
  inference-cost-truth, genai-prices, llm-price-compass, llm-price-war

Pure functions for:
- Fetching pricing from provider APIs and community data feeds
- Normalizing pricing formats (per-1K vs per-1M token conventions)
- Detecting price changes
- Generating pricing reports
- Break-even analysis (self-host vs API) from inference-cost-truth
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Tuple
from enum import Enum
import json
import time
from datetime import datetime, timedelta
import os


@dataclass
class ModelPricing:
    """LLM model pricing information"""
    provider: str
    model: str
    input_cost_per_1k: float  # Cost per 1K input tokens in USD
    output_cost_per_1k: float  # Cost per 1K output tokens in USD
    max_context: int  # Maximum context window size
    last_updated: str  # ISO timestamp
    currency: str = "USD"
    notes: str = ""


@dataclass
class PricingChange:
    """Detected pricing change"""
    provider: str
    model: str
    field: str
    old_value: float
    new_value: float
    change_percentage: float
    detected_at: str


class ModelStatus(Enum):
    """Model lifecycle status, from llm-prices-data schema."""
    CURRENT = "Current"
    RETIRED = "Retired"
    PREVIEW = "Preview"
    DEPRECATED = "Deprecated"


@dataclass
class ModelSpec:
    """Full model specification, from model-specs / model-catalog inspiration repos.
    Extends ModelPricing with capability and compatibility metadata."""
    provider: str
    model: str
    input_per_mtok: float          # USD per 1M input tokens (industry standard)
    output_per_mtok: float         # USD per 1M output tokens
    cached_input_per_mtok: Optional[float] = None
    context_window: int = 0
    modality: List[str] = field(default_factory=lambda: ["text"])
    status: ModelStatus = ModelStatus.CURRENT
    open_source: bool = False
    parameters: Optional[int] = None
    released: str = ""
    retired_on: Optional[str] = None
    pricing_url: str = ""
    description: str = ""
    tags: List[str] = field(default_factory=list)

    @property
    def input_per_1k(self) -> float:
        """Convert per-1M to per-1K for backward compat."""
        return self.input_per_mtok / 1000

    @property
    def output_per_1k(self) -> float:
        return self.output_per_mtok / 1000


@dataclass
class BreakEvenResult:
    """Break-even analysis from inference-cost-truth.
    How many API output tokens per month make self-hosting cheaper."""
    self_host_model: str
    gpu_model: str
    gpu_count: int
    monthly_fixed_usd: float
    api_model: str
    api_provider: str
    api_output_per_1m: float
    break_even_tokens_per_month: int
    monthly_capacity_at_utilization: Dict[str, int] = field(default_factory=dict)
    reachable_at_utilization: Dict[str, Optional[str]] = field(default_factory=dict)


class LLMPricingCollector:
    def __init__(self):
        self.providers = {
            'openai': self._fetch_openai_pricing,
            'anthropic': self._fetch_anthropic_pricing,
            'google': self._fetch_google_pricing,
            'cohere': self._fetch_cohere_pricing,
            'mistral': self._fetch_mistral_pricing
        }
        self.pricing_cache: Dict[str, List[ModelPricing]] = {}
        self.change_history: List[PricingChange] = []
    
    def fetch_all_pricing(self) -> Dict[str, List[ModelPricing]]:
        """
        Fetch pricing from all providers
        
        Returns:
            Dictionary mapping provider names to their pricing lists
        """
        all_pricing = {}
        
        for provider_name, fetcher in self.providers.items():
            try:
                pricing = fetcher()
                all_pricing[provider_name] = pricing
                self.pricing_cache[provider_name] = pricing
            except Exception as e:
                print(f"Failed to fetch pricing for {provider_name}: {e}")
                # Use cached data if available
                if provider_name in self.pricing_cache:
                    all_pricing[provider_name] = self.pricing_cache[provider_name]
        
        return all_pricing
    
    def detect_changes(self, new_pricing: Dict[str, List[ModelPricing]]) -> List[PricingChange]:
        """
        Detect pricing changes by comparing with cached data
        
        Args:
            new_pricing: New pricing data
        
        Returns:
            List of detected changes
        """
        changes = []
        
        for provider, models in new_pricing.items():
            if provider not in self.pricing_cache:
                continue
            
            old_models = {m.model: m for m in self.pricing_cache[provider]}
            
            for model in models:
                if model.model in old_models:
                    old_model = old_models[model.model]
                    
                    # Check input cost change
                    if old_model.input_cost_per_1k != model.input_cost_per_1k:
                        change_pct = ((model.input_cost_per_1k - old_model.input_cost_per_1k) / 
                                    old_model.input_cost_per_1k * 100)
                        changes.append(PricingChange(
                            provider=provider,
                            model=model.model,
                            field='input_cost_per_1k',
                            old_value=old_model.input_cost_per_1k,
                            new_value=model.input_cost_per_1k,
                            change_percentage=change_pct,
                            detected_at=datetime.now().isoformat()
                        ))
                    
                    # Check output cost change
                    if old_model.output_cost_per_1k != model.output_cost_per_1k:
                        change_pct = ((model.output_cost_per_1k - old_model.output_cost_per_1k) / 
                                    old_model.output_cost_per_1k * 100)
                        changes.append(PricingChange(
                            provider=provider,
                            model=model.model,
                            field='output_cost_per_1k',
                            old_value=old_model.output_cost_per_1k,
                            new_value=model.output_cost_per_1k,
                            change_percentage=change_pct,
                            detected_at=datetime.now().isoformat()
                        ))
        
        self.change_history.extend(changes)
        return changes
    
    def generate_report(self, pricing: Dict[str, List[ModelPricing]]) -> Dict[str, Any]:
        """
        Generate a pricing report
        
        Args:
            pricing: Pricing data from all providers
        
        Returns:
            Report with statistics and insights
        """
        report = {
            'generated_at': datetime.now().isoformat(),
            'providers': {},
            'cheapest_models': [],
            'most_expensive_models': [],
            'average_prices': {}
        }
        
        all_models = []
        
        for provider, models in pricing.items():
            provider_stats = {
                'model_count': len(models),
                'cheapest_input': None,
                'cheapest_output': None,
                'most_expensive_input': None,
                'most_expensive_output': None
            }
            
            if models:
                # Find cheapest and most expensive
                cheapest_input = min(models, key=lambda m: m.input_cost_per_1k)
                most_expensive_input = max(models, key=lambda m: m.input_cost_per_1k)
                cheapest_output = min(models, key=lambda m: m.output_cost_per_1k)
                most_expensive_output = max(models, key=lambda m: m.output_cost_per_1k)
                
                provider_stats['cheapest_input'] = {
                    'model': cheapest_input.model,
                    'cost': cheapest_input.input_cost_per_1k
                }
                provider_stats['most_expensive_input'] = {
                    'model': most_expensive_input.model,
                    'cost': most_expensive_input.input_cost_per_1k
                }
                provider_stats['cheapest_output'] = {
                    'model': cheapest_output.model,
                    'cost': cheapest_output.output_cost_per_1k
                }
                provider_stats['most_expensive_output'] = {
                    'model': most_expensive_output.model,
                    'cost': most_expensive_output.output_cost_per_1k
                }
                
                # Calculate averages
                avg_input = sum(m.input_cost_per_1k for m in models) / len(models)
                avg_output = sum(m.output_cost_per_1k for m in models) / len(models)
                
                report['average_prices'][provider] = {
                    'input': avg_input,
                    'output': avg_output
                }
                
                all_models.extend(models)
            
            report['providers'][provider] = provider_stats
        
        # Find overall cheapest and most expensive
        if all_models:
            sorted_by_input = sorted(all_models, key=lambda m: m.input_cost_per_1k)
            report['cheapest_models'] = [
                {'provider': m.provider, 'model': m.model, 'input_cost': m.input_cost_per_1k}
                for m in sorted_by_input[:5]
            ]
            report['most_expensive_models'] = [
                {'provider': m.provider, 'model': m.model, 'input_cost': m.input_cost_per_1k}
                for m in sorted_by_input[-5:]
            ]
        
        return report
    
    def compare_models(
        self, 
        pricing: Dict[str, List[ModelPricing]], 
        model1: str, 
        model2: str
    ) -> Dict[str, Any]:
        """
        Compare pricing between two specific models
        
        Args:
            pricing: Pricing data
            model1: First model name
            model2: Second model name
        
        Returns:
            Comparison results
        """
        model1_pricing = None
        model2_pricing = None
        
        for provider, models in pricing.items():
            for model in models:
                if model.model == model1:
                    model1_pricing = model
                elif model.model == model2:
                    model2_pricing = model
        
        if not model1_pricing or not model2_pricing:
            return {'error': 'One or both models not found'}
        
        input_cost_diff = model2_pricing.input_cost_per_1k - model1_pricing.input_cost_per_1k
        output_cost_diff = model2_pricing.output_cost_per_1k - model1_pricing.output_cost_per_1k
        
        return {
            'model1': {
                'provider': model1_pricing.provider,
                'model': model1_pricing.model,
                'input_cost': model1_pricing.input_cost_per_1k,
                'output_cost': model1_pricing.output_cost_per_1k,
                'max_context': model1_pricing.max_context
            },
            'model2': {
                'provider': model2_pricing.provider,
                'model': model2_pricing.model,
                'input_cost': model2_pricing.input_cost_per_1k,
                'output_cost': model2_pricing.output_cost_per_1k,
                'max_context': model2_pricing.max_context
            },
            'comparison': {
                'input_cost_difference': input_cost_diff,
                'output_cost_difference': output_cost_diff,
                'cheaper_input': model1 if input_cost_diff > 0 else model2,
                'cheaper_output': model1 if output_cost_diff > 0 else model2,
                'larger_context': model1 if model1_pricing.max_context > model2_pricing.max_context else model2
            }
        }
    
    def _fetch_openai_pricing(self) -> List[ModelPricing]:
        """Fetch OpenAI pricing (simulated)"""
        # In production, this would call OpenAI's API or scrape their pricing page
        return [
            ModelPricing(
                provider="openai",
                model="gpt-4",
                input_cost_per_1k=0.03,
                output_cost_per_1k=0.06,
                max_context=8192,
                last_updated=datetime.now().isoformat()
            ),
            ModelPricing(
                provider="openai",
                model="gpt-4-turbo",
                input_cost_per_1k=0.01,
                output_cost_per_1k=0.03,
                max_context=128000,
                last_updated=datetime.now().isoformat()
            ),
            ModelPricing(
                provider="openai",
                model="gpt-3.5-turbo",
                input_cost_per_1k=0.0005,
                output_cost_per_1k=0.0015,
                max_context=16385,
                last_updated=datetime.now().isoformat()
            )
        ]
    
    def _fetch_anthropic_pricing(self) -> List[ModelPricing]:
        """Fetch Anthropic pricing (simulated)"""
        return [
            ModelPricing(
                provider="anthropic",
                model="claude-3-opus",
                input_cost_per_1k=0.015,
                output_cost_per_1k=0.075,
                max_context=200000,
                last_updated=datetime.now().isoformat()
            ),
            ModelPricing(
                provider="anthropic",
                model="claude-3-sonnet",
                input_cost_per_1k=0.003,
                output_cost_per_1k=0.015,
                max_context=200000,
                last_updated=datetime.now().isoformat()
            ),
            ModelPricing(
                provider="anthropic",
                model="claude-3-haiku",
                input_cost_per_1k=0.00025,
                output_cost_per_1k=0.00125,
                max_context=200000,
                last_updated=datetime.now().isoformat()
            )
        ]
    
    def _fetch_google_pricing(self) -> List[ModelPricing]:
        """Fetch Google pricing (simulated)"""
        return [
            ModelPricing(
                provider="google",
                model="gemini-pro",
                input_cost_per_1k=0.00025,
                output_cost_per_1k=0.0005,
                max_context=32760,
                last_updated=datetime.now().isoformat()
            ),
            ModelPricing(
                provider="google",
                model="gemini-flash",
                input_cost_per_1k=0.000075,
                output_cost_per_1k=0.0003,
                max_context=32760,
                last_updated=datetime.now().isoformat()
            )
        ]
    
    def _fetch_cohere_pricing(self) -> List[ModelPricing]:
        """Fetch Cohere pricing (simulated)"""
        return [
            ModelPricing(
                provider="cohere",
                model="command-r-plus",
                input_cost_per_1k=0.003,
                output_cost_per_1k=0.015,
                max_context=128000,
                last_updated=datetime.now().isoformat()
            ),
            ModelPricing(
                provider="cohere",
                model="command-r",
                input_cost_per_1k=0.00015,
                output_cost_per_1k=0.0006,
                max_context=128000,
                last_updated=datetime.now().isoformat()
            )
        ]
    
    def _fetch_mistral_pricing(self) -> List[ModelPricing]:
        """Fetch Mistral pricing (simulated)"""
        return [
            ModelPricing(
                provider="mistral",
                model="mistral-large",
                input_cost_per_1k=0.008,
                output_cost_per_1k=0.024,
                max_context=32000,
                last_updated=datetime.now().isoformat()
            ),
            ModelPricing(
                provider="mistral",
                model="mistral-small",
                input_cost_per_1k=0.001,
                output_cost_per_1k=0.003,
                max_context=32000,
                last_updated=datetime.now().isoformat()
            )
        ]

    # ---- Break-even analysis (extracted from inference-cost-truth) ----

    def load_break_even_data(self, json_path: str) -> List[BreakEvenResult]:
        """Load break-even analysis from inference-cost-truth break-even.json.

        Each row compares self-hosting a model on GPUs vs calling an API,
        showing the monthly token volume at which self-hosting becomes cheaper.
        """
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        results = []
        for row in data.get("rows", []):
            results.append(BreakEvenResult(
                self_host_model=row.get("self_host_model", ""),
                gpu_model=row.get("gpu_model", ""),
                gpu_count=row.get("gpu_count", 0),
                monthly_fixed_usd=row.get("monthly_fixed_usd", 0),
                api_model=row.get("api_model", ""),
                api_provider=row.get("api_provider", ""),
                api_output_per_1m=row.get("api_output_per_1m", 0),
                break_even_tokens_per_month=row.get("break_even_output_tokens_per_month", 0),
                monthly_capacity_at_utilization=row.get(
                    "monthly_output_capacity_by_utilization", {}
                ),
                reachable_at_utilization=row.get("reachable_at_utilization", {}),
            ))
        return results

    def find_cheapest_self_host(
        self, break_even_data: List[BreakEvenResult],
        monthly_tokens: int
    ) -> Optional[BreakEvenResult]:
        """Find the cheapest self-hosting option for a given monthly token volume.

        Returns the self-host config with the lowest monthly_fixed_usd that can
        serve the requested volume at a given utilization, or None if none can.
        """
        candidates = []
        for be in break_even_data:
            for util_label, capacity in be.monthly_capacity_at_utilization.items():
                if capacity >= monthly_tokens:
                    candidates.append((be, util_label))
        if not candidates:
            return None
        candidates.sort(key=lambda x: x[0].monthly_fixed_usd)
        return candidates[0][0]

    # ---- Model spec loading (extracted from llm-prices-data / model-specs) ----

    def load_model_specs(self, json_path: str) -> List[ModelSpec]:
        """Load model specifications from llm-prices-data models.json format.

        This is the community-maintained daily-verified pricing data from the
        llm-prices-data inspiration repo.
        """
        with open(json_path, "r", encoding="utf-8") as f:
            rows = json.load(f)

        specs = []
        for row in rows:
            status_str = row.get("status", "Current")
            try:
                status = ModelStatus(status_str)
            except ValueError:
                status = ModelStatus.CURRENT

            specs.append(ModelSpec(
                provider=row.get("provider", ""),
                model=row.get("model", ""),
                input_per_mtok=row.get("input_per_mtok", 0),
                output_per_mtok=row.get("output_per_mtok", 0),
                cached_input_per_mtok=row.get("cached_input_per_mtok"),
                context_window=row.get("context_window", 0),
                modality=row.get("modality", ["text"]),
                status=status,
                open_source=row.get("open_source", False),
                parameters=row.get("parameters"),
                released=row.get("released", ""),
                retired_on=row.get("retired_on"),
                pricing_url=row.get("pricing_url", ""),
                description=row.get("description", ""),
                tags=row.get("tags", []),
            ))
        return specs

    def filter_by_status(
        self, specs: List[ModelSpec], status: ModelStatus
    ) -> List[ModelSpec]:
        """Filter model specs by lifecycle status."""
        return [s for s in specs if s.status == status]

    def find_cheapest_by_context(
        self, specs: List[ModelSpec], min_context: int
    ) -> List[ModelSpec]:
        """Find cheapest models meeting a minimum context window requirement."""
        eligible = [s for s in specs
                     if s.context_window >= min_context
                     and s.status == ModelStatus.CURRENT]
        eligible.sort(key=lambda s: s.input_per_mtok)
        return eligible

    # ---- llm-prices per-vendor format (from llm-prices repo) ----

    def load_vendor_pricing(self, json_path: str) -> List[ModelPricing]:
        """Load pricing from llm-prices per-vendor JSON format.

        Each vendor file (openai.json, anthropic.json, etc.) has:
          {"vendor": "openai", "models": [{"id": "gpt-4o", "name": "GPT-4o",
           "price_history": [{"input": 2.5, "output": 10, "input_cached": 1.25,
           "from_date": null, "to_date": null}]}]}

        Prices are in USD per 1M tokens (matching llm-prices convention).
        We convert to per-1K for the ModelPricing dataclass.
        """
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        vendor = data.get("vendor", "unknown")
        results = []
        for model_entry in data.get("models", []):
            model_id = model_entry.get("id", "")
            model_name = model_entry.get("name", model_id)
            price_history = model_entry.get("price_history", [])
            if not price_history:
                continue
            # Use the most recent price entry (last in the array)
            latest = price_history[-1]
            input_per_m = latest.get("input", 0)
            output_per_m = latest.get("output", 0)
            cached = latest.get("input_cached")
            results.append(ModelPricing(
                provider=vendor,
                model=model_id,
                input_cost_per_1k=input_per_m / 1000,
                output_cost_per_1k=output_per_m / 1000,
                max_context=0,
                last_updated=datetime.now().isoformat(),
                notes=f"cached_input={cached}/Mtok" if cached else "",
            ))
        return results

    def load_all_vendor_pricing(self, directory: str) -> Dict[str, List[ModelPricing]]:
        """Load all vendor JSON files from a directory (llm-prices data/ folder).

        Returns a dict keyed by vendor name, same as fetch_all_pricing().
        """
        all_pricing = {}
        for fname in sorted(os.listdir(directory)):
            if not fname.endswith(".json"):
                continue
            fpath = os.path.join(directory, fname)
            try:
                pricing = self.load_vendor_pricing(fpath)
                if pricing:
                    vendor = pricing[0].provider
                    all_pricing[vendor] = pricing
                    self.pricing_cache[vendor] = pricing
            except Exception as e:
                print(f"Failed to load {fname}: {e}")
        return all_pricing

    def get_price_history(
        self, json_path: str, model_id: str
    ) -> List[Dict[str, Any]]:
        """Get the full price history for a specific model from a vendor file.

        llm-prices tracks price changes over time with from_date/to_date.
        """
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        for model_entry in data.get("models", []):
            if model_entry.get("id") == model_id:
                return model_entry.get("price_history", [])
        return []

    def load_current_v1(self, json_path: str) -> List[ModelPricing]:
        """Load from llm-prices current-v1.json API format.

        Format: {"updated_at": "2025-10-10", "prices": [{"id": "amazon-nova-micro",
        "vendor": "amazon", "name": "Amazon Nova Micro",
        "input": 0.035, "output": 0.14, "input_cached": null}]}
        """
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        results = []
        for entry in data.get("prices", []):
            input_per_m = entry.get("input", 0)
            output_per_m = entry.get("output", 0)
            cached = entry.get("input_cached")
            results.append(ModelPricing(
                provider=entry.get("vendor", ""),
                model=entry.get("id", ""),
                input_cost_per_1k=input_per_m / 1000,
                output_cost_per_1k=output_per_m / 1000,
                max_context=0,
                last_updated=data.get("updated_at", datetime.now().isoformat()),
                notes=f"name={entry.get('name','')}; cached={cached}/Mtok" if cached else f"name={entry.get('name','')}",
            ))
        return results