import pos_tagging
import json
from paragraph_generator import get_random_paragraph
from aidlib import do_ai_madlib
from sentiment_analysis import analyze_tone

BLANK_TOKEN = "_"

def regular_madlibs(new_text, removed):
    for i in range(len(removed)):
        pos = removed[i][2]
        
        prompt = "idk"
        if pos in {"JJ", "JJR", "JJS"}:
            prompt = "Type an adjective: "
        elif pos in {"RB", "RBR", "RBS"}:
            prompt = "Type an adverb: "
        elif pos in {"VB", "VBD", "VBG", "VBN", "VBP", "VBZ"}:
            prompt = "Type a verb: "
        else:
            prompt = "I messed up!"

        response = input(prompt)
        removed[i].append(response)

    print(pos_tagging.fillin_blanks(new_text, removed))

def sentiment_madlibs(new_text, removed):
    sentiment = json.loads(analyze_tone(text))
    overall_tone = sentiment["document_tone"]["tones"][0]["tone_name"].lower()
    sentence_sentiments = sentiment["sentences_tone"]

    for i in range(len(removed)):
        pos = removed[i][2]
        tones = sentence_sentiments[i]["tones"]
        if len(tones) == 0:
            tone = overall_tone
        else:
            tone = tones[0]["tone_name"].lower()
        
        prompt = "idk"
        if pos in {"JJ", "JJR", "JJS"}:
            prompt = "Type an adjective that exhibits the tone of " + tone + ": "
        elif pos in {"RB", "RBR", "RBS"}:
            prompt = "Type an adverb that exhibits the tone of " + tone + ": "
        elif pos in {"VB", "VBD", "VBG", "VBN", "VBP", "VBZ"}:
            prompt = "Type a verb: "
        else:
            prompt = "I messed up!"

        response = input(prompt)
        removed[i].append(response)

    print(pos_tagging.fillin_blanks(new_text, removed))

def bert_solver(new_text):
    print(do_ai_madlib(new_text, BLANK_TOKEN))

if __name__ == "__main__":
    stop = False
    while not stop:
        text = get_random_paragraph()
        #return the paragraph with removed words
        removed, new_text = pos_tagging.generate_blanks(text)
        print("Here is the original text:")
        print(new_text)
        response = input("Would you like: \n1. a regular MadLibs \n2. a MadLibs with a suggested tone, \n3. a MadLibs that has been filled out by an AI?\n")
        if "1" in response or "regular" in response:
            regular_madlibs(new_text, removed)
        elif "2" in response or "tone" in response:
            sentiment_madlibs(new_text, removed)
        else:
            bert_solver(new_text)
        response = input("Would you like to fill out a MadLibs? y/n\n")
        if "n" in response.lower():
            stop = True
    