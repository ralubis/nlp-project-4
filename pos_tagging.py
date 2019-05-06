from stanfordnlp.server import CoreNLPClient
import json
import os
import re

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
        # get its pos and add to removed_pos

    return removed_pos


    