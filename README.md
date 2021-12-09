# Knowledge-Graph-Question-Answering
# this project is on-going 

# ===== KG3_2 ===== 

This is a pipeline of knowledge graph construction and question answering on dariy farming transition cows research. Including:

1, An dictionary tagger used to tag the research papers as the BIO(bigin - in - out) tagging format with domain dictionary entity. This component speed up the corpus preperation process.

2, An named entity recognition model using Bi-LSTM neural network. 

3, A relation extraction model using BERT. 

4, Entities and relationships are stored in graph database neo4j.

5, A quesiton answering component to map the nutral question to graph database query language.

# ===== KG4 =====

A fully connected pipeline of KG3_2 but using bio-medical neural model without training


