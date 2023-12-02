import json

file = "data.json"

with open(file, "r") as json_file:
    data = json.load(json_file)
    name_data = (data["tense"])
    for i in name_data:
        en = (i[en])
        age = (i[type])
        print(f'(en) is (type)')