# from nltk.stem import PorterStemmer

class QuestionPaser:

    '''To build entity dictionary'''
    def build_entitydict(self, args):

        entity_dict = {}
        
        for arg, types in args.items():
            for type in types:
                if type not in entity_dict:
                    entity_dict[type] = [arg]
                else:
                    entity_dict[type].append(arg)
                    #stemmed_entity_dict = stem(entity_dict)

        return entity_dict


    # ============ Use different question templates by entity dictionary ================
    '''main function'''
    def parser_main(self, res_classify):
        #extract the entities
        args = res_classify['args']
        entity_dict = self.build_entitydict(args)
        #extract the question types
        question_types = res_classify['question_types']
        sqls = []
        for question_type in question_types:
            sql_ = {}
            sql_['question_type'] = question_type
            sql = []
            
            # ========== set type and dict here ================ 
            if question_type == 'cause_diseases':
                sql = self.sql_transfer(question_type, entity_dict.get('nutrition'))            

            elif question_type == 'prevent_diseases':
                sql = self.sql_transfer(question_type, entity_dict.get('diseases'))                     

            if sql:
                sql_['sql'] = sql

                sqls.append(sql_)

        return sqls

    # ================= Cypher Query Language ==================
    # ========= use different cypher language to query the neo4j database ============= 
    '''Excecute different questions with sqls'''
    def sql_transfer(self, question_type, entities):
        if not entities:
            return []

        # cypher query
        sql = []

        # ======== Query1 =======
        # for cause_diseases
        if question_type == 'cause_diseases':
            sql = ["MATCH (m:Diseases)<-[r:cause]-(n:Nutrition) where n.nname=\"{0}\" return n.nname, m.dname".format(i) for i in entities]

        # ======== Query2 =======
        # for prevent_diseases
        if question_type == 'prevent_diseases':
            sql = ["MATCH (m:Diseases)<-[r:prevent]-(n:Nutrition) where m.dname=\"{0}\" return n.nname, m.dname".format(i) for i in entities]


        return sql

if __name__ == '__main__':
    handler = QuestionPaser()
