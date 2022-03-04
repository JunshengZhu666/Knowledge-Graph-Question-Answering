===== Dictionary_Tagger2: This file is used to tag the agumentated data =======================================


# 1, Load text and dictionary: new_tokenize_text, nutrition_dict, disease_dict


# 2, Expand each sentence: expanded_word_list


# 3, Get the list of entity: ent_list_dis, ent_list_nut


# 4, Tag the origin sentence list: 

t_sent_split(origin list), 

dis_tagged_sent(tagged by dis),

nut_tagged_sent,


# 5, Concat two tagged list: 

tag_sum_mid,


# 6, Concat tagged lists with 'END', origin lists with 'END'

final_tag

ori_sum_mid


# 7, Output to excel 

rich_sentence.xlsx


===== Dictionary_Tagger2_To_get_rich_ent_sent: =======================================



This file is used to shuffle, split and get the 

training dataset (txt)

testing dataset (txt) 

agumented dataset (txt)


### 1, Load and shuffle the dataset 


### 2, Split into (4:1) train and test 

training_set_txt.txt (output txt)

testing_set_txt.txt (output txt)


### 3, Get the agumented data from training set 

from list of training set sentences (training_set)


### 4, Load text and dictionary: training_set, nutrition_dict, disease_dict


### 5, Expand each sentence: expanded_word_list


### 6, Get the list of entity: ent_list_dis, ent_list_nut


### 7, Tag the origin sentence list: 

t_sent_split(origin list), 

dis_tagged_sent(tagged by dis),

nut_tagged_sent(tagged by nut),


### 8, Concat two tagged list: 

tag_sum_mid,


### 9, Concat tagged lists with 'END', origin lists with 'END'

final_tag

ori_sum_mid

### 10, Split by 'END' to get the list of tag and sentence

split_tag (tag)

t_sent_split (sentence) 

### 11, Get the rich sentences

rich_sent: list of sentences of list of words

rich_tag: list of tags

### 12, Expand the rich sentences 

rich_sent_ones

rich_sent_twos

rich_sent_threes

### 13, Sum up and output to text

sum_rich_sent

rich_sentence_from_training_set.txt

# ===== Now tag the train, test, agu dataset 

rich_sentence_from_training_set

testing_set_txt

training_set_txt

get: 

training_set_excel

testing_set_excel

rich_sentence_from_training_excel


after change format to txt, could be used for training 


===== rubbish =======================================

