import json
with open('mydata1.json','r') as a:
    b=json.load(a)
for q in b:
    for n in q:
        print(n['dow'])
    


