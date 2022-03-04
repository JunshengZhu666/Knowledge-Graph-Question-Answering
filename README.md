# Knowledge-Graph-Question-Answering

# 1, A flow chart representing the main experimental procedures

![0_overall_procedures](https://user-images.githubusercontent.com/77312114/156826689-6c272c00-cd66-4c28-9b0e-a3bfa9e03623.png)

# 2, File contents

### KG3_2  

This is a pipeline of knowledge graph construction and question answering on dariy farming transition cows research. Including:

1, An dictionary tagger used to tag the research papers as the BIO(bigin - in - out) tagging format with domain dictionary entity. This component speed up the corpus preperation process.

2, A named entity recognition model using Bi-LSTM neural network. 

3, A relation extraction model using BERT. 

4, Entities and relationships are stored in graph database neo4j.

5, A quesiton answering component to map the nutral question to graph database query language.

### KG4 

A fully connected pipeline of KG3_2 but using bio-medical neural model without training

### KG4_2 

1, A tuned named entity recognition model using Bi-LSTM neural network. 

2, A relation extraction model with few-shoting learning

# 2, References

updating
