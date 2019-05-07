from stanfordnlp.server import CoreNLPClient
import json
import os
import re
import numpy as np

#To run openie cd into stanford folder and run this command: java -mx8g -Xmx8g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment,coref,openie" -port 9000 -timeout 30000
os.environ['CORENLP_HOME'] = os.path.join(os.getcwd(), 'stanford-corenlp-full-2018-10-05/')
nlpClient = CoreNLPClient(timeout=30000, memory='16G', output_format='json')

def generate_blanks(text):
    global nlpClient
    output = nlpClient.annotate(text, annotators=['pos, ner, relation'])

    removed_pos = []
    for s in output['sentences']:
        num_words = len(s['tokens'])
        # randomly generate a number in num_words
        indices = np.random.choice(num_words, num_words, replace=False)
        for index in indices:
            index_pos = s['tokens'][index]['pos']
            if index_pos in {"JJ", "JJR", "JJS", "RB", "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"}:
                # get its pos and add to removed_pos
                print("word to be removed:", s['tokens'][index])
                removed_pos.append(s['tokens'][index]['pos'])
                break

    print("removed pos", removed_pos)
    return removed_pos


    