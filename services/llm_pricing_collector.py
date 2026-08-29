"""
LLM Pricing Data Collection Service
Collects and normalizes pricing data from multiple LLM providers

Pure functions for:
- Fetching pricing from provider APIs
- Normalizing pricing formats
- Detecting price changes
- Generating pricing reports
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Any
import time
from datetime import datetime, timedelta


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