"""HyDE Hypothetical Document Query Expansion Engine.
100% Python Standard Library.
"""

import math
import collections
import re

class HyDEQueryExpander:
    """Hypothetical Document Embeddings (HyDE) zero-shot retrieval expander."""
    def __init__(self):
        self.stopwords = {"the", "a", "an", "is", "in", "at", "of", "on", "for", "to", "with", "and"}

    def generate_hypothetical_answer(self, query):
        keywords = [w.lower() for w in re.findall(r'\b\w+\b', query) if w.lower() not in self.stopwords]
        pseudo_doc = f"Regarding {query}: A core solution involves {', '.join(keywords)}. High-efficiency mechanisms optimize these parameters under standard production constraints."
        return pseudo_doc

    def lexical_vector(self, text):
        words = [w.lower() for w in re.findall(r'\b\w+\b', text) if w.lower() not in self.stopwords]
        counts = collections.Counter(words)
        total = sum(counts.values()) or 1
        return {k: v / total for k, v in counts.items()}

    def cosine_similarity(self, vec1, vec2):
        keys = set(vec1.keys()).union(vec2.keys())
        dot = sum(vec1.get(k, 0.0) * vec2.get(k, 0.0) for k in keys)
        norm1 = math.sqrt(sum(v * v for v in vec1.values()))
        norm2 = math.sqrt(sum(v * v for v in vec2.values()))
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)
