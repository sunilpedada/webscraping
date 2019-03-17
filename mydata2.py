import json
with open('mydata1.json','r') as a:
    b=(json.load(a))
for q,c,d, in b:
	n=(q['dow'])
	m=(c['time'])
	f=d.get('conference-categories-count')
	o=(f.get('Large'))
	print({n:[m,o]})
	
