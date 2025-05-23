import json

def read_json(uri):
    "Reads in a dictionary from a json file uri"
    with open('data.json', 'r') as file:
        return json.load(file)

def write_json(dict, uri):
    "Writes a json file from a dictionary"
    json_obj = json.dumps(dict)

    with open(uri, 'w') as outf:
        outf.write(json_obj)
