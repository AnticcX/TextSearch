from dataclasses import dataclass, field

@dataclass
class TrieNode:
    children: dict[str, "TrieNode"] = field(default_factory=dict)
    is_terminal: bool = False
    weight: float = 0.0
    phrase: str = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _collect_candidates(self, node: TrieNode, candidates: list[tuple[str, float]]):
        if node.is_terminal:
            candidates.append((node.phrase, node.weight))
        for child_node in node.children.values():
            self._collect_candidates(child_node, candidates)

    def insert(self, phrase: str, weight: float):
        current_node = self.root
        for char in phrase:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_terminal = True
        current_node.weight = max(current_node.weight, weight)
        current_node.phrase = phrase

    def search(self, prefix: str, top_k: int = 5) -> list[tuple[str, float]]:
        current_node = self.root
        # walk down prefix path
        for char in prefix:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]

        # collect all descendants from current_node
        candidates = []
        self._collect_candidates(current_node, candidates)

        # sort candidates by weight and return top_k
        candidates.sort(key=lambda x: x[1], reverse=True)
        return candidates[:top_k]