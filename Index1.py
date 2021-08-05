import pandas
data=pandas.read_csv('Data.py')
data.head()
name=data['name'].tolist()
mass=data['mass'].tolist()
radius=data['radius'].tolist()
distance=data['distance'].tolist()
gravity=data['gravity'].tolist()
dictpython={}
stars=[]
for i in range(0,len(name)):
	dictpython['name']=name[i]
	dictpython['mass']=mass[i]
	dictpython['radius']=radius[i]
	dictpython['distance']=distance[i]
	dictpython['gravity']=gravity[i]
	stars.append(dictpython)
	dictpython={}