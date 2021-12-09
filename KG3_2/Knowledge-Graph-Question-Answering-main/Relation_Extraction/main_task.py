#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
from @author: weetee

JZ looking at 2021-10-27

"""

# importing from src.tasks
from src.tasks.trainer import train_and_fit

# importing from src.tasks
from src.tasks.infer import infer_from_trained, FewRel

# importing logging and argparse
import logging
from argparse import ArgumentParser


# The configration for fine-tuning the BERT model on SemEval, FewRel tasks


# logging asctime, levelname and message
logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', \
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
logger = logging.getLogger('__file__')

# adding the arguments for fine-tuning
if __name__ == "__main__":


    parser = ArgumentParser()

    # task: semeval
    parser.add_argument("--task", type=str, default='semeval', help='semeval, fewrel')

    # ==================== training data ======================
    # train_data
    parser.add_argument("--train_data", type=str, default='./data/SemEval2010_task8_all_data/SemEval2010_task8_training/TRAIN_FILE_COW.TXT', \
                        help="training data .txt file path")

    # ==================== testing data ======================
    # test_data
    parser.add_argument("--test_data", type=str, default='./data/SemEval2010_task8_all_data/SemEval2010_task8_testing_keys/TEST_FILE_COW.TXT', \
                        help="test data .txt file path")

    # use_pretrained_blanks: NO                    
    parser.add_argument("--use_pretrained_blanks", type=int, default=0, help="0: Don't use pre-trained blanks model, 1: use pre-trained blanks model")
    
    # ========================= num_classes of relation classes ===========================
    # (2021-11-02) IndexError: Target 8 is out of bounds. 
    # (2021-11-02) 9 is running: to 24/119
    parser.add_argument("--num_classes", type=int, default=9, help='number of relation classes')
    
    # ============================== batch_size ========================
    # (2021 - 11 - 02) For TRAIN_FILE_COW: batch_size = 8
    parser.add_argument("--batch_size", type=int, default=8, help="Training batch size")
    
    # steps of gradient accumulation: 2
    parser.add_argument("--gradient_acc_steps", type=int, default=2, help="No. of steps of gradient accumulation")
    
    # max_norm: 1.0
    parser.add_argument("--max_norm", type=float, default=1.0, help="Clipped gradient norm")
    
    # fp16: floating point 32
    parser.add_argument("--fp16", type=int, default=0, help="1: use mixed precision ; 0: use floating point 32") # mixed precision doesn't seem to train well
    
    # ================================= number of epochs ====================
    # Runing on the origin dataset
    # ...
    # epoch4: accurracy 0.78
    # epoch5: accurracy 0.81
    parser.add_argument("--num_epochs", type=int, default=12, help="No of epochs")
    
    # learing_rate: 0.00007
    parser.add_argument("--lr", type=float, default=0.00007, help="learning rate")
    
    # model number: using BERT
    parser.add_argument("--model_no", type=int, default=0, help='''Model ID: 0 - BERT\n
                                                                            1 - ALBERT\n
                                                                            2 - BioBERT''')

    # model size: bert-base_uncased                                                                        
    parser.add_argument("--model_size", type=str, default='bert-base-uncased', help="For BERT: 'bert-base-uncased', \
                                                                                                'bert-large-uncased',\
                                                                                    For ALBERT: 'albert-base-v2',\
                                                                                                'albert-large-v2'\
                                                                                    For BioBERT: 'bert-base-uncased' (biobert_v1.1_pubmed)")
    # train: train
    parser.add_argument("--train", type=int, default=1, help="0: Don't train, 1: train")
    
    # infer: infer
    parser.add_argument("--infer", type=int, default=1, help="0: Don't infer, 1: Infer")
    
    args = parser.parse_args()
    
    # net = train_and_fit
    if (args.train == 1) and (args.task != 'fewrel'):
        net = train_and_fit(args)
    
    # infering
    if (args.infer == 1) and (args.task != 'fewrel'):
        inferer = infer_from_trained(args, detect_entities=True)

        # infer type1
        test = "The surprise [E1]visit[/E1] caused a [E2]frenzy[/E2] on the already chaotic trading floor."
        inferer.infer_sentence(test, detect_entities=False)
        
        # infer type2
        test2 = "After eating the chicken, he developed a sore throat the next morning."
        inferer.infer_sentence(test2, detect_entities=True)
        
        while True:
            sent = input("Type input sentence ('quit' or 'exit' to terminate):\n")
            if sent.lower() in ['quit', 'exit']:
                break
            inferer.infer_sentence(sent, detect_entities=False)
    
    # for fewrel
    if args.task == 'fewrel':
        fewrel = FewRel(args)
        meta_input, e1_e2_start, meta_labels, outputs = fewrel.evaluate()