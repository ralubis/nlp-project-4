from stanfordnlp.server import CoreNLPClient
import json
import os
import re
import numpy as np

#To run openie cd into stanford folder and run this command: java -mx8g -Xmx8g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment,coref,openie" -port 9000 -timeout 30000
os.environ['CORENLP_HOME'] = os.path.join(os.getcwd(), 'stanford-corenlp-full-2018-10-05/')
nlpClient = CoreNLPClient(timeout=30000, memory='16G', output_format='json')

def generate_blanks(text):
    """
    given an input pargraph, generate one random blank per sentence
    and return text with "____" replacing all removed words
    """

    global nlpClient
    output = nlpClient.annotate(text, annotators=['pos'])

    removed = []
    for s in output['sentences']:
        num_words = len(s['tokens'])
        # randomly generate a number in num_words
        indices = np.random.choice(num_words, num_words, replace=False)
        for index in indices:
            index_pos = s['tokens'][index]['pos']
            if index_pos in {"JJ", "JJR", "JJS", "RB", "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"}:
                # get its pos and add to removed_pos
                #print("word to be removed:", s['tokens'][index])
                temp = [index, s['tokens'][index]['originalText'], s['tokens'][index]['pos']]
                removed.append(temp)
                s['tokens'][index]['word'] = "_____"
                break

    new_text = []
    for s in output['sentences']:
        for t in s['tokens']:
            new_text += [t['word']]

    print("removed pos", removed)
    return removed, ' '.join(new_text)


def fillin_blanks(new_text, removed):
    """
    todo: refactor 
    """
    for i in range(len(removed)):
        new_text = re.sub("_____", removed[i][-1], new_text, count=1)
    return new_text






    