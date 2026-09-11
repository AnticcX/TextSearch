from dataclasses import dataclass

@dataclass
class TrieNode:
    children: dict[str, "TrieNode"] = {}
    is_terminal: bool = False
    weight: float = 0.0
    phrase: str = None