from py2neo import Graph

class AnswerSearcher:
    # ========================= Password ==================
    def __init__(self):
        self.g = Graph("http://localhost:7474", user="neo4j", password="neo4jneo4j")
        self.num_limit = 20

    '''Cypher query'''
    def search_main(self, sqls):
        final_answers = []
        for sql_ in sqls:
            question_type = sql_['question_type']
            queries = sql_['sql']
            answers = []
            for query in queries:
                ress = self.g.run(query).data()
                answers += ress
            final_answer = self.answer_prettify(question_type, answers)
            if final_answer:
                final_answers.append(final_answer)
        return final_answers


    # ===================== Answer template ========================

    '''qustion_type，answer template'''
    def answer_prettify(self, question_type, answers):
        final_answer = []
        if not answers:
            return 'Sorry I cannot understand your question:<'
            
        """if question_type == 'ask_symptom':
            l_ = []
            for i in answers:
                if i['n.sname'] not in l_:
                    l_.append(i['n.sname'])
                    final_answer = 'For the symptom {2}, The possible diseases in this case might be: {0}  The other symptoms of {0} including {1}'.format(i['m.dname'], i['m.dsymptoms'], i['n.sname'])
                    print(final_answer)"""
        # ===== question_type =====
        # 1, NUT - cause - DIS
        # question_name: cause_diseases
        if question_type == 'cause_diseases':
            l_ = []
            # answers
            desc = [i['m.dname'] for i in answers]
            # query keywords
            subject = answers[0]['n.nname']
            # answers format 
            final_answer = '{0} might casue diseases：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            print(final_answer)

        # ===== question_type =====
        # 1, DIS - how prevent - NUT
        # question_name: prevent_diseases
        elif question_type == 'prevent_diseases':
            l_ = []
            # answers
            desc = [i['n.nname'] for i in answers]
            # query keywords
            subject = answers[0]['m.dname']
            # answers format 
            final_answer = '{1} might prevent diseases：{0}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            print(final_answer)
    
        elif question_type == 'ask_treatment':
            l_ = []
            for i in answers:
                if i['m.dname'] not in l_:
                    l_.append(i['m.dname'])
                    final_answer = 'The treatment of  {0} could be: {1}'.format(i['m.dname'], i['m.dtreatments'])
                    print(final_answer)

        return final_answer
       

if __name__ == '__main__':
    searcher = AnswerSearcher()