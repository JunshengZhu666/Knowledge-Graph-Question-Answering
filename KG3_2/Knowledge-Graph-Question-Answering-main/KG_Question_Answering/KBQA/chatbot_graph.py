from question_classifier import *
from question_parser import *
from answer_search import *

'''Query and Answer'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = 'Good Question!!! Ask for advisors for more help ~ '
        res_classify = self.classifier.classify(sent)
        if not res_classify=='':
            print(answer)
        #print('class：',res_classify)
        res_sql = self.parser.parser_main(res_classify)
        #print('sql query',res_sql)

        final_answers = self.searcher.search_main(res_sql)
        if final_answers=='':
            print(answer)

            #return '\n'.join(final_answers)


# ========================== Test =================================
# ============ Input the test question =============================
if __name__ == '__main__':
    handler = ChatBotGraph()
    # Test-start
    # 1, NUT - cause - DIS 
    # 2, NUT - prevent - DIS 
    # 3, NUT - cause - DIS 
    problems=["What might high fermentable energy cause?"
    ,"What would prevent fatty liver?"
    ,"What might over-conditioning cause?"]
    for id,problem in enumerate(problems):
        print("========== The {0} question is:  {1}： ==========".format(id,problem))
        handler.chat_main(problem)
        print("\n")
    print("End of the test","\n")
    #Test-end
    while 1:
        unstemmed_question = input('Any other questions?:')
        handler.chat_main(unstemmed_question)
        print("\n")

