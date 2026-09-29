from client import HyDEQueryExpander

expander = HyDEQueryExpander()
query = "How to achieve lock-free concurrent ring buffer?"
pseudo_doc = expander.generate_hypothetical_answer(query)
doc_corpus = "LMAX Disruptor implements a lock-free circular ring buffer with sequence barriers."

v_query = expander.lexical_vector(pseudo_doc)
v_doc = expander.lexical_vector(doc_corpus)
sim = expander.cosine_similarity(v_query, v_doc)

print("Generated Pseudo Document:", pseudo_doc)
print(f"Cosine Similarity to Corpus: {sim:.4f}")
