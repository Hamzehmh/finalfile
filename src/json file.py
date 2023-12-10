import json
print("----------------start--------------------")

file = "src/data1.json"


with open(file, "r") as f:
    data = json.load(f)
    #name_data = (data["size"])
print(data)    
    
for i in data:
      print(i[1])
      

      
  #    size = (i[size])
   #   color = (i[color])
    #  print(f'{size} is {color}')
    #dfg709i7hfh

print("----------------end--------------------")
