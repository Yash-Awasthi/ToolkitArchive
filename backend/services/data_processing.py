"""
Data Processing Utilities — ToolkitArchive
CSV/JSON parsing, data transformation, statistical analysis
"""

import csv
import json
import math
from typing import List, Dict, Optional, Any, Tuple
from dataclasses import dataclass
from collections import Counter, defaultdict
from io import StringIO


@dataclass
class DataStats:
    count: int
    mean: float
    median: float
    mode: Optional[float]
    std_dev: float
    min: float
    max: float
    range: float
    q1: float
    q3: float
    iqr: float
    variance: float
    skewness: float
    kurtosis: float


@dataclass
class TransformResult:
    data: List[Dict]
    rows_processed: int
    rows_dropped: int
    columns_added: List[str]
    columns_dropped: List[str]


class CSVProcessor:
    """Pure function CSV processing."""

    @staticmethod
    def parse_csv(text: str, delimiter: str = ',') -> List[Dict]:
        reader = csv.DictReader(StringIO(text), delimiter=delimiter)
        return [row for row in reader]

    @staticmethod
    def to_csv(data: List[Dict], delimiter: str = ',') -> str:
        if not data:
            return ""
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=data[0].keys(), delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)
        return output.getvalue()

    @staticmethod
    def filter_rows(data: List[Dict], column: str, op: str, value: Any) -> List[Dict]:
        result = []
        for row in data:
            cell = row.get(column)
            if cell is None:
                continue
            try:
                cell_val = float(cell) if isinstance(value, (int, float)) else cell
            except (ValueError, TypeError):
                cell_val = cell
            if op == 'eq' and cell_val == value:
                result.append(row)
            elif op == 'ne' and cell_val != value:
                result.append(row)
            elif op == 'gt' and cell_val > value:
                result.append(row)
            elif op == 'lt' and cell_val < value:
                result.append(row)
            elif op == 'gte' and cell_val >= value:
                result.append(row)
            elif op == 'lte' and cell_val <= value:
                result.append(row)
            elif op == 'contains' and str(value) in str(cell_val):
                result.append(row)
        return result

    @staticmethod
    def sort_by(data: List[Dict], column: str, ascending: bool = True) -> List[Dict]:
        def sort_key(row):
            val = row.get(column, '')
            try:
                return float(val)
            except (ValueError, TypeError):
                return str(val).lower()
        return sorted(data, key=sort_key, reverse=not ascending)

    @staticmethod
    def group_by(data: List[Dict], column: str) -> Dict[str, List[Dict]]:
        groups = defaultdict(list)
        for row in data:
            key = str(row.get(column, 'unknown'))
            groups[key].append(row)
        return dict(groups)

    @staticmethod
    def aggregate(data: List[Dict], column: str, operation: str) -> float:
        values = []
        for row in data:
            val = row.get(column)
            if val is not None:
                try:
                    values.append(float(val))
                except (ValueError, TypeError):
                    pass
        if not values:
            return 0.0
        if operation == 'sum':
            return sum(values)
        elif operation == 'avg':
            return sum(values) / len(values)
        elif operation == 'min':
            return min(values)
        elif operation == 'max':
            return max(values)
        elif operation == 'count':
            return len(values)
        elif operation == 'median':
            sorted_vals = sorted(values)
            n = len(sorted_vals)
            if n % 2 == 0:
                return (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2
            return sorted_vals[n // 2]
        return 0.0


class StatisticalAnalyzer:
    """Pure function statistical analysis."""

    @staticmethod
    def calculate_stats(values: List[float]) -> DataStats:
        if not values:
            return DataStats(0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        n = len(values)
        mean = sum(values) / n
        sorted_vals = sorted(values)
        if n % 2 == 0:
            median = (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2
        else:
            median = sorted_vals[n // 2]
        counter = Counter(values)
        mode = counter.most_common(1)[0][0] if counter else None
        variance = sum((x - mean) ** 2 for x in values) / n
        std_dev = math.sqrt(variance)
        min_val = min(values)
        max_val = max(values)
        q1_idx = n // 4
        q3_idx = 3 * n // 4
        q1 = sorted_vals[q1_idx]
        q3 = sorted_vals[q3_idx]
        iqr = q3 - q1
        if std_dev > 0:
            skewness = sum((x - mean) ** 3 for x in values) / (n * std_dev ** 3)
            kurtosis = sum((x - mean) ** 4 for x in values) / (n * std_dev ** 4) - 3
        else:
            skewness = 0
            kurtosis = 0
        return DataStats(
            count=n,
            mean=round(mean, 4),
            median=round(median, 4),
            mode=mode,
            std_dev=round(std_dev, 4),
            min=round(min_val, 4),
            max=round(max_val, 4),
            range=round(max_val - min_val, 4),
            q1=round(q1, 4),
            q3=round(q3, 4),
            iqr=round(iqr, 4),
            variance=round(variance, 4),
            skewness=round(skewness, 4),
            kurtosis=round(kurtosis, 4)
        )

    @staticmethod
    def detect_outliers_iqr(values: List[float], factor: float = 1.5) -> List[int]:
        if len(values) < 4:
            return []
        sorted_vals = sorted(values)
        n = len(sorted_vals)
        q1 = sorted_vals[n // 4]
        q3 = sorted_vals[3 * n // 4]
        iqr = q3 - q1
        lower_bound = q1 - factor * iqr
        upper_bound = q3 + factor * iqr
        return [i for i, v in enumerate(values) if v < lower_bound or v > upper_bound]

    @staticmethod
    def detect_outliers_zscore(values: List[float], threshold: float = 3.0) -> List[int]:
        if len(values) < 3:
            return []
        n = len(values)
        mean = sum(values) / n
        variance = sum((x - mean) ** 2 for x in values) / n
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return []
        return [i for i, v in enumerate(values) if abs((v - mean) / std_dev) > threshold]

    @staticmethod
    def correlation(x: List[float], y: List[float]) -> float:
        if len(x) != len(y) or len(x) < 2:
            return 0.0
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        denom_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
        denom_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))
        if denom_x == 0 or denom_y == 0:
            return 0.0
        return numerator / (denom_x * denom_y)

    @staticmethod
    def linear_regression(x: List[float], y: List[float]) -> Dict:
        if len(x) != len(y) or len(x) < 2:
            return {"slope": 0, "intercept": 0, "r_squared": 0}
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        denominator = sum((xi - mean_x) ** 2 for xi in x)
        if denominator == 0:
            return {"slope": 0, "intercept": mean_y, "r_squared": 0}
        slope = numerator / denominator
        intercept = mean_y - slope * mean_x
        ss_res = sum((yi - (slope * xi + intercept)) ** 2 for xi, yi in zip(x, y))
        ss_tot = sum((yi - mean_y) ** 2 for yi in y)
        r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
        return {
            "slope": round(slope, 6),
            "intercept": round(intercept, 6),
            "r_squared": round(r_squared, 6)
        }


class DataTransformer:
    """Pure function data transformation."""

    @staticmethod
    def normalize(values: List[float], method: str = 'minmax') -> List[float]:
        if not values:
            return []
        if method == 'minmax':
            min_val = min(values)
            max_val = max(values)
            range_val = max_val - min_val
            if range_val == 0:
                return [0.5] * len(values)
            return [(v - min_val) / range_val for v in values]
        elif method == 'zscore':
            n = len(values)
            mean = sum(values) / n
            variance = sum((x - mean) ** 2 for x in values) / n
            std_dev = math.sqrt(variance)
            if std_dev == 0:
                return [0.0] * len(values)
            return [(v - mean) / std_dev for v in values]
        elif method == 'decimal':
            max_abs = max(abs(v) for v in values) or 1
            return [v / max_abs for v in values]
        return values

    @staticmethod
    def bin(values: List[float], num_bins: int = 10) -> Dict[str, int]:
        if not values:
            return {}
        min_val = min(values)
        max_val = max(values)
        range_val = max_val - min_val
        if range_val == 0:
            return {"0": len(values)}
        bin_width = range_val / num_bins
        bins = defaultdict(int)
        for v in values:
            bin_idx = min(int((v - min_val) / bin_width), num_bins - 1)
            bin_label = f"{min_val + bin_idx * bin_width:.2f}-{min_val + (bin_idx + 1) * bin_width:.2f}"
            bins[bin_label] += 1
        return dict(bins)

    @staticmethod
    def moving_average(values: List[float], window: int) -> List[float]:
        if not values or window <= 0:
            return []
        result = []
        for i in range(len(values)):
            start = max(0, i - window + 1)
            window_vals = values[start:i + 1]
            result.append(sum(window_vals) / len(window_vals))
        return result

    @staticmethod
    def lag_features(values: List[float], lags: List[int]) -> Dict[str, List[float]]:
        features = {}
        for lag in lags:
            feature_name = f"lag_{lag}"
            features[feature_name] = [0.0] * lag + values[:-lag] if lag < len(values) else [0.0] * len(values)
        return features
