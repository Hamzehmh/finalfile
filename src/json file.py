import json

#print("----------------START------------------")
#my_info = [
  {
    "fa": "Man dar hal e hazer inja kar mikonam",
    "en": "I'm working at the moment",
    "type": "positive",
    "tense": "Present Continuous"
  }]
print("----------------DUMP---------------------")
ali = json.dumps(my_info)
print(ali)
print("----------------LOAD---------------------")
hasam = json.loads(ali)
print("===>",hasam)
print("----------------END----------------------")



#json.dump(my_info,fp=["datata.json"])

with open("data_file.json", "w") as f:
    json.dump(data, f)



import json
 
f = open('../src/data.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)
 
# Closing file
f.close()