from dataclasses import dataclass
from typing import Any, TypeAlias

FieldName: TypeAlias = str

@dataclass
class FieldConfig:
    is_searchable: bool = True
    is_suggestable: bool = False
    weight: float = 1.0

@dataclass
class Document:
    id: str | int
    fields: dict[FieldName, Any]
    popularity: float = 0.0


class Schema:
    field_configurations: dict[FieldName, FieldConfig]

    def get_searchable_fields(self) -> list[FieldName]:
        return [
            field_names for field_names, config in self.field_configurations.items() if config.is_searchable
        ]

    def get_suggestable_fields(self) -> list[FieldName]:
        return [
            field_names for field_names, config in self.field_configurations.items() if config.is_suggestable
        ]