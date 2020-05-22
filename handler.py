print('container start')

try:
    import unzip_requirements
except ImportError as error:
    pass
print("unzipped")

import json
import en_core_web_sm
from spacy import displacy
print("import ends")

MODEL = en_core_web_sm.load()
print('model loaded')

def create_dep(text):
    doc = MODEL(text)
    
    return displacy.parse_deps(doc)


    

def handle_request(event, context):
    request_body = event['body']
    text = json.loads(request_body)['text']

    print(text)
    if text is not None:
        results = create_dep(text)

    response = {
        "statusCode": 200,
        "body": json.dumps(results),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    return response

    