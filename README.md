# Knowledge-Graph-Question-Answering
Transition Cow KBQA &amp; Nueral Entity Extractor &amp; Nueral Relationship Extractor

# this project is on-going 

# ===== Pipeline ===== 

![image](https://user-images.githubusercontent.com/77312114/140336576-0f68c2e6-ebd2-4b07-9206-01b146ea0a35.png)

# ===== Data Schema =====

![image](https://user-images.githubusercontent.com/77312114/140336747-e1cffac0-e91e-4dcc-ab66-8de84575cae5.png)

# ===== Explain the question answering part =====



1, Prepare:

    # Start neo4j database. 
    # Put into the two entity words list under the folder:
![image](https://user-images.githubusercontent.com/77312114/142640798-fbe6f71f-f930-4dfc-a187-ac9e93ea3e37.png)



2, Code skeleton:

![image](https://user-images.githubusercontent.com/77312114/121019573-2273b500-c7d2-11eb-9fbd-9c50957b86ec.png)



3, Question Template setting up:

3,1 answer_search.py:

    # 1 Change url, username and password to connect the neo4j database
    
    # 2 Set the final answer template for different question type:
    #  question_type == 'cause_diseases'
    #  '{0} might casue diseases：{1}', 'n.nname', 'm.dname'
![image](https://user-images.githubusercontent.com/77312114/142640139-b96c5fc8-761f-4e76-9ace-08ff69b8d67b.png)

    
3,2 chatbot_graph.py: 

    # 1 Can set the testing questions:
![image](https://user-images.githubusercontent.com/77312114/142640347-5fb0489f-1d42-4ab3-a26f-4be7d13a680b.png)
    
3,3 question_classifier.py:

    # 1 Load in the entity word lists
    # search and change all 'diseases' in script for your entity word list
![image](https://user-images.githubusercontent.com/77312114/142641311-3c542fe2-d500-4840-883a-44793c187c17.png)
    
    # 2 Set the question classification words 
![image](https://user-images.githubusercontent.com/77312114/142641975-47a00ce3-3cda-4f80-8337-0bcf240ca299.png)
    
    # 3 Set the question classification rules 
![image](https://user-images.githubusercontent.com/77312114/142642231-81612afa-8d0c-48c5-bd8b-2b09d231b733.png)

    # 4 Build word type dictionary (python dictionary)
![image](https://user-images.githubusercontent.com/77312114/142644574-f9c3109d-3020-4ecd-9ad1-56da4092f98a.png)
    
3,4 question_parser.py:
    
    # 1 Pass the retrived entities to according question template
![image](https://user-images.githubusercontent.com/77312114/142645569-561ad9ec-8b44-48c1-8cd4-485b790c5de7.png)

    # 2 Use different query language(Cypher) to query the neo4j database
![image](https://user-images.githubusercontent.com/77312114/142645858-69a399cb-fa5d-4d2d-8443-f47056061979.png)




