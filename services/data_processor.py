"""
Data Processing Utilities
Extracted from free-for-dev's data organization patterns

Features:
- Data normalization and cleaning
- Aggregation and grouping
- Filtering and search
- Category management
- Deduplication
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Callable
from collections import defaultdict
import re
import json


@dataclass
class DataItem:
    """Generic data item with metadata"""
    id: str
    name: str
    description: str
    category: str
    tags: List[str]
    url: Optional[str]
    metadata: Dict[str, Any]
    created_at: Optional[float]
    updated_at: Optional[float]


@dataclass
class AggregationResult:
    """Result of data aggregation"""
    group: str
    count: int
    items: List[DataItem]
    summary: Dict[str, Any]


class DataProcessor:
    """
    Data processing utilities
    Extracted from free-for-dev's approach to organizing large datasets
    """
    
    def __init__(self):
        self.items: List[DataItem] = []
        self.categories: Dict[str, List[DataItem]] = defaultdict(list)
        self.tags: Dict[str, List[DataItem]] = defaultdict(list)
    
    def add_item(self, item: DataItem):
        """Add a data item"""
        self.items.append(item)
        self.categories[item.category].append(item)
        
        for tag in item.tags:
            self.tags[tag].append(item)
    
    def add_items(self, items: List[DataItem]):
        """Add multiple data items"""
        for item in items:
            self.add_item(item)
    
    def normalize_text(self, text: str) -> str:
        """
        Normalize text for consistent comparison
        
        Args:
            text: Input text
        
        Returns:
            Normalized text
        """
        # Lowercase
        text = text.lower()
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Remove special characters (keep alphanumeric and spaces)
        text = re.sub(r'[^\w\s]', '', text)
        
        return text
    
    def normalize_item(self, item: DataItem) -> DataItem:
        """
        Normalize a data item
        
        Args:
            item: Data item to normalize
        
        Returns:
            Normalized data item
        """
        return DataItem(
            id=item.id.lower().strip(),
            name=self.normalize_text(item.name),
            description=self.normalize_text(item.description),
            category=self.normalize_text(item.category),
            tags=[self.normalize_text(tag) for tag in item.tags],
            url=item.url,
            metadata=item.metadata,
            created_at=item.created_at,
            updated_at=item.updated_at
        )
    
    def deduplicate(
        self,
        items: Optional[List[DataItem]] = None,
        key: Callable[[DataItem], str] = lambda item: item.id
    ) -> List[DataItem]:
        """
        Remove duplicate items
        
        Args:
            items: List of items (uses self.items if None)
            key: Function to extract unique key
        
        Returns:
            Deduplicated list
        """
        if items is None:
            items = self.items
        
        seen = set()
        unique_items = []
        
        for item in items:
            item_key = key(item)
            if item_key not in seen:
                seen.add(item_key)
                unique_items.append(item)
        
        return unique_items
    
    def filter_by_category(
        self,
        category: str,
        items: Optional[List[DataItem]] = None
    ) -> List[DataItem]:
        """
        Filter items by category
        
        Args:
            category: Category to filter by
            items: List of items (uses self.items if None)
        
        Returns:
            Filtered items
        """
        if items is None:
            items = self.items
        
        normalized_category = self.normalize_text(category)
        return [
            item for item in items
            if self.normalize_text(item.category) == normalized_category
        ]
    
    def filter_by_tags(
        self,
        tags: List[str],
        match_all: bool = False,
        items: Optional[List[DataItem]] = None
    ) -> List[DataItem]:
        """
        Filter items by tags
        
        Args:
            tags: Tags to filter by
            match_all: If True, item must have all tags; if False, any tag
            items: List of items (uses self.items if None)
        
        Returns:
            Filtered items
        """
        if items is None:
            items = self.items
        
        normalized_tags = [self.normalize_text(tag) for tag in tags]
        
        if match_all:
            return [
                item for item in items
                if all(
                    self.normalize_text(item_tag) in normalized_tags
                    for item_tag in item.tags
                )
            ]
        else:
            return [
                item for item in items
                if any(
                    self.normalize_text(item_tag) in normalized_tags
                    for item_tag in item.tags
                )
            ]
    
    def search(
        self,
        query: str,
        items: Optional[List[DataItem]] = None
    ) -> List[DataItem]:
        """
        Search items by text query
        
        Args:
            query: Search query
            items: List of items (uses self.items if None)
        
        Returns:
            Matching items
        """
        if items is None:
            items = self.items
        
        normalized_query = self.normalize_text(query)
        query_words = normalized_query.split()
        
        results = []
        for item in items:
            searchable_text = f"{item.name} {item.description} {' '.join(item.tags)}"
            normalized_text = self.normalize_text(searchable_text)
            
            # Check if all query words are present
            if all(word in normalized_text for word in query_words):
                results.append(item)
        
        return results
    
    def aggregate_by(
        self,
        field: str,
        items: Optional[List[DataItem]] = None
    ) -> List[AggregationResult]:
        """
        Aggregate items by a field
        
        Args:
            field: Field to aggregate by (category, tag, etc.)
            items: List of items (uses self.items if None)
        
        Returns:
            List of aggregation results
        """
        if items is None:
            items = self.items
        
        groups: Dict[str, List[DataItem]] = defaultdict(list)
        
        for item in items:
            if field == 'category':
                groups[item.category].append(item)
            elif field == 'tag':
                for tag in item.tags:
                    groups[tag].append(item)
            else:
                groups[item.metadata.get(field, 'unknown')].append(item)
        
        results = []
        for group, group_items in groups.items():
            summary = {
                'count': len(group_items),
                'unique_tags': list(set(tag for item in group_items for tag in item.tags))
            }
            
            results.append(AggregationResult(
                group=group,
                count=len(group_items),
                items=group_items,
                summary=summary
            ))
        
        # Sort by count descending
        results.sort(key=lambda x: x.count, reverse=True)
        
        return results
    
    def get_statistics(self, items: Optional[List[DataItem]] = None) -> Dict[str, Any]:
        """
        Get statistics about the dataset
        
        Args:
            items: List of items (uses self.items if None)
        
        Returns:
            Statistics dictionary
        """
        if items is None:
            items = self.items
        
        if not items:
            return {
                'total': 0,
                'categories': {},
                'tags': {},
                'avg_tags_per_item': 0
            }
        
        # Count categories
        category_counts = defaultdict(int)
        for item in items:
            category_counts[item.category] += 1
        
        # Count tags
        tag_counts = defaultdict(int)
        for item in items:
            for tag in item.tags:
                tag_counts[tag] += 1
        
        # Calculate average tags per item
        total_tags = sum(len(item.tags) for item in items)
        avg_tags = total_tags / len(items)
        
        return {
            'total': len(items),
            'categories': dict(category_counts),
            'tags': dict(tag_counts),
            'avg_tags_per_item': avg_tags,
            'unique_categories': len(category_counts),
            'unique_tags': len(tag_counts)
        }
    
    def export_to_json(
        self,
        items: Optional[List[DataItem]] = None,
        indent: int = 2
    ) -> str:
        """
        Export items to JSON
        
        Args:
            items: List of items (uses self.items if None)
            indent: JSON indentation
        
        Returns:
            JSON string
        """
        if items is None:
            items = self.items
        
        data = []
        for item in items:
            data.append({
                'id': item.id,
                'name': item.name,
                'description': item.description,
                'category': item.category,
                'tags': item.tags,
                'url': item.url,
                'metadata': item.metadata
            })
        
        return json.dumps(data, indent=indent, ensure_ascii=False)
    
    def import_from_json(self, json_str: str) -> List[DataItem]:
        """
        Import items from JSON
        
        Args:
            json_str: JSON string
        
        Returns:
            List of imported items
        """
        data = json.loads(json_str)
        items = []
        
        for record in data:
            item = DataItem(
                id=record['id'],
                name=record['name'],
                description=record.get('description', ''),
                category=record.get('category', 'uncategorized'),
                tags=record.get('tags', []),
                url=record.get('url'),
                metadata=record.get('metadata', {}),
                created_at=record.get('created_at'),
                updated_at=record.get('updated_at')
            )
            items.append(item)
        
        return items


def create_data_processor() -> DataProcessor:
    """
    Create a new data processor
    
    Returns:
        DataProcessor instance
    """
    return DataProcessor()