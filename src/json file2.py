import json

print("----------------start---------------------")

file = "src/data3 finglish.json"


with open(file, "r") as f:
    data = json.load(f)
    #name_data = (data["size"])
print(data)    
    
for i in data:
      print(i)
      

      
  #    size = (i[size])
   #   color = (i[color])
    #  print(f'{size} is {color}')
    #dfg709i7hfhlklsdf55pop

print("----------------end---------------------")
