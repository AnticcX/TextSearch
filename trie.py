from dataclasses import dataclass

@dataclass
class TrieNode:
    children: dict[str, "TrieNode"] = {}
    is_terminal: bool = False
    weight: float = 0.0
    phrase: str = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, phrase: str, weight: float):
        current_node = self.root
        for char in phrase:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_terminal = True
        current_node.weight = max(current_node.weight, weight)
        current_node.phrase = phrase