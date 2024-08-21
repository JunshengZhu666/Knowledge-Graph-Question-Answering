# Knowledge-Graph-Question-Answering

# 1, Some Charts
![image](https://github.com/user-attachments/assets/61717ed5-1828-4864-ac75-7ed3a204f6a8)
![image](https://github.com/user-attachments/assets/91efd249-e274-49bc-8f6b-0f2c4e214538)

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

### Publish 
Automated extraction of domain knowledge in the dairy industry
https://www.sciencedirect.com/science/article/pii/S0168169923007184
