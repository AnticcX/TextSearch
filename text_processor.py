from .normalizer import tokenize
from .document import Document, Schema

DEFAULT_STOP_WORDS = ("a", "an", "and", "are", "as", "at", "be", "but", "by",
                      "for", "if", "in", "into", "is", "it", "no", "not", "of",
                      "on", "or", "such", "that", "the", "their", "then", "there",
                      "these", "they", "this", "to", "was", "will", "with")


class TextProcessor:
    def __init__(self, stop_words=None):
        if stop_words is None:
            self.stop_words = set(DEFAULT_STOP_WORDS)
        else:
            self.stop_words = set(stop_words)

    def process_text(self, raw_text: str) -> list[str]:
        raw_tokens = tokenize(raw_text)
        filtered_tokens = [token for token in raw_tokens if token not in self.stop_words]
        return filtered_tokens

    def process_document(document: Document, schema: Schema) -> dict[str, list[str]]:
        processed_fields = {}
        for field_name in schema.get_searchable_fields():
            if field_name in document.fields:
                raw_val = str(document.fields[field_name])
                processed_fields[field_name] = self.process_text(raw_val)
        return processed_fields