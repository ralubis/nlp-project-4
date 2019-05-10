import pos_tagging
import json
from paragraph_generator import get_random_paragraph
from aidlib import do_ai_madlib
from sentiment_analysis import analyze_tone

BLANK_TOKEN = "_"

if __name__ == "__main__":
    text = get_random_paragraph()

    #return the paragraph with removed words
    removed, new_text = pos_tagging.generate_blanks(text)
    print("Here is the original text:")
    print(new_text)
    # print("Here is the sentiment analysis")
    # print(analyze_tone(text))

    sentiment = json.loads(analyze_tone(text))
    overall_tone = sentiment["document_tone"]["tones"][0]["tone_name"].lower()
    sentence_sentiments = sentiment["sentences_tone"]
    
    # #prompt the user for each black and store all input
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

    print(removed)

    # return completed paragraph
    print(pos_tagging.fillin_blanks(new_text, removed))

    # print(do_ai_madlib(new_text, BLANK_TOKEN))
    