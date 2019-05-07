import json
from ibm_watson import ToneAnalyzerV3
from os import environ
from paragraph_generator import get_random_paragraph

ibm_params = {
     'apikey': environ['IBM_API_KEY'],
     'url': environ['IBM_API_URL'],
     'version': environ['IBM_API_VERSION']
     }

tone_analyzer = ToneAnalyzerV3(
    version=ibm_params['version'],
    iam_apikey=ibm_params['apikey'],
    url=ibm_params['url']
)

def analyze_tone(text):
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    return json.dumps(tone_analysis, indent=2)

def main():
    # text = 'Team, I know that times are tough! Product '\
    #     'sales have been disappointing for the past three '\
    #     'quarters. We have a competitive product, but we '\
    #     'need to do a better job of selling it!'
    text = get_random_paragraph()
    print(analyze_tone(text))

if __name__ == '__main__':
    main()