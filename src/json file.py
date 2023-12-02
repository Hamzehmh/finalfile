import json
print("----------------start--------------------")

file = "src\data1.json"

with open(file, "r") as f:
    data = json.load(f)
    #name_data = (data["size"])
print(data)    
    
#for i in name_data:
 #     print(i)
  #    size = (i[size])
   #   color = (i[color])
    #  print(f'{size} is {color}')

print("----------------end--------------------")
