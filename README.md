# genpark-hyde-hypothetical-document-embeddings-skill

Agent Skill implementing **HyDE (Hypothetical Document Embeddings)** query expansion and vector matching in 100% Python standard library.

## Architectural Flow
```mermaid
flowchart TD
    Q["User Query"] --> Gen["HyDE Generator (Synthesizes Pseudo Answer)"]
    Gen --> PseudoDoc["Hypothetical Document P(x)"]
    PseudoDoc --> Vec1["Lexical-Semantic Vector V(P)"]
    Corpus["Candidate Corpus C(x)"] --> Vec2["Lexical-Semantic Vector V(C)"]
    Vec1 & Vec2 --> CosSim["Cosine Similarity Score"]
    CosSim --> Rank["Relevance Ranking Decision"]
```
