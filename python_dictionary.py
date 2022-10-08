dict1={'ibk':20,'vera':30,'kate':40} #string in a dict
print(dict1)
dict2={1:50,2:60,3:70} #int in a dict
print(dict2)
dict3={('kayode',4,'catherine'):(100,110,120),(7,8,9):(130,(140,150)),(10,11,'fish'):(160,170,180)} #tuple in a dict
print(dict3)
dict4={'pro':[1,2,3],'gra':[4,5,6],'mmers':[7,8,9]} #list in a dict
print(dict4)
print(type(dict4))

emptydict=dict() #creating an empty dict
print(emptydict)

dict5=dict(i='one',ii='two',iii='three')
print(dict5)

print(dict5['i'])
print(dict5['ii'])
print(dict5['iii'])
print(dict5.get('i'))
print(dict5.get('iv'))

for key in dict5:
  print('key='+key+',value='+dict5[key])

dict5['i']=11 #updating the value of i
dict5['ii']=11 #updating the value of ii
dict5['iii']=11 #updating the value of iii
print(dict5)

dict5['iv']=44 #adding key iv
dict5['v']=55 #adding key v
print(dict5)

del dict5['v'] #deleting a key:value pair
print(dict5)

del dict3 #deleting a dictionary

print(dict5.keys()) #printing keys alone
print(dict5.values()) #printing value alone

print('iv' in dict5)
print('v' in dict5)

dict6={'name':'steve','age':25,'marks':60}
dict7={'name':'anil','age':23,'marks':75}
dict8={'name':'asha','age':20,'marks':70}

dict9={1:dict6,2:dict7,3:dict8} #multidimensional dictionary i.e a dict in a dict
print(dict9)

print(dict6['age'])
print(dict9[1]['age'])
dict1.clear() #clearing dict1
print(dict1)

keys={'mumbai','banglore','chicago','newyork'}
value='city'
dict10=dict.fromkeys(keys,value)
print(dict10)

print(dict9.items())

print(dict2.pop(2)) #popping key2
print('after popping(2 key):',dict2)

print(dict2.pop(4,'fadesola')) #popping key2
print('popped item:',dict2.popitem()) #printing popped item

dict11={'i':1,'iii':3,'v':5}
dict12={'ii':2,'iv':4}
dict11.update(dict12)
print('updated dictionary:',dict11)











