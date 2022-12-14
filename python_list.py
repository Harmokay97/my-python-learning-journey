list1=[] #declaring an empty list
print(list1)

list2=['adewumi','kayode','vera','christy'] #
print(list2)

list3=[1,3,5,3,6] #int list
print(list3)

list4=[1.3,4.5,2.9,5.6] #float list
print(list4)

list5=[True,False] #bool list
print(list5)

list6=[1,2.0,True,'harmokay'] #heterogenous
print(list)

#INDEXING
print(list2[0]) #first index +ve indexing
print(list2[-4]) #first index -ve indexing
print(list2[3]) #first index +ve indexing
print(list2[-1]) #first index -ve indexing

#LIST OF LIST
list7=[1,2,3,[4,5,6,[7,8,[9]]],10]
print(list7)
print(list7[0]) #return 1
print(list7[3]) #return [4,5,6,[7,8,[9]]]
print(list7[4]) #return 10
print(list7[3][3]) #return [7,8,[9]]
print(list7[3][3][2]) #return [9]

#LIST CONVERSION
list8=[1,2,3,4]
print(type(list8))

list9=list('sabi programmer')#convert str to list
print(list9)

list10=list({1:'one',2:'two'}) #convert a dict list
print(list10)

list11=list((10,20,30)) #convert a tuple to list
print(list11)

list12=list({100,200,300}) #convert set to list
print(list12)

#iterate a list
for name in list2:
    print(name)

for ind in range(len(list2)):
    print(list2[ind])

#list operators
print(list2+list3) #+operator
print([1,2,3] *3) #*operator

print('adewumi' in list2) #in operator
print('harmokay'not in list2) #not in operator

print(list2[1:5]) #slicing

#update list
list2[0]='vera'
list2.append('michael')
print(list2)

#remove item
print('list2: ', list2)
del list2[0]
print('after de list2[0]: ', list2)

list2.remove('kayode')
print('after removing kayode: ', list2)

print(list2.pop()) #remove last index
print('after popping last index: ', list2)

list2.clear() #make the list empty
print(list2)

del list2 #delete list2

#list methods
list13=[2,4,6,8]

#copy fmctions
list14=list13.copy()
print(list14)

#append functions
list13.append(10)
print('list13: ', list13)
print('list14: ', list14)

#count function
list13.append(4)
print(list13.count(4))
print(list13.count(4))

#extend functions
list14.extend([12,14,16])
print(list14)

#index functions
print(list14.index(14))
print(list13)
print(list13.index(4))

#insert function
list13.insert(3,7) #index, value
print(list13)

list13.insert(0,1) #index value
print(list13)

#pop function
list13.pop(3) #remove at index 3
print(list13)
list.pop() #remove from last index
print(list13)

#remove function
list13.remove(1) #remove 1 from the list
print(list13)

#reverse function
list13.reverse()
print(list13)

#sort function
list.sort()
print(list13)
list13.sort(reverse=True)
print(list13)





