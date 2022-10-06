str1='My name is Harmokay'#assigning a single quote string to str1
print(str1)
str2="My name is Harmokay" #assigning a double qoute string to str2
print(str2)
str3='''My name is Harmokay''' #assigning triple quote string to str3
print(str3)
str4="""My name is Harmokay""" #assigning triple quote string to str4
print(str4)

#MULTIPLE STRING
str5='''this is my own multi-line string using quote''' #assigning triple single quote multi-line string
print(str5)
str6="""this is my own multi-line string using quote""" #assigning triple double quote multi-line string
print(str6)

#quote in quote
str7="welcome to engr-d class" #icluding a double quote to str7
print(str7)
str8='welcome to engr-d class' #icluding a sinle quote to str8
print(str8)

#string length and indexing
str9='sabi programmer'
print(len(str9)) #return the length of str9

print(str9[0]) #return first index using +ve indexing
print(str9[-15]) #return first index using -ve indexing

print(str9[14])#return first index using +ve indexing
print(str9[-1]) #return first index using -ve indexing

print(str9[7]) #return the 8th index usimg +ve indexing
print(str9[-8]) #return the 8th index usimg -ve indexing


#ESCAPE SEQUENCES
str10='welcome to \'eng d\'class' #escape sequence in single quote
print(str10)
str11="welcome to \"eng d\"class" #escape sequence in single double quote
print(str11)
str12=r'welcome to \'eng d\'class' #ignoring escape
print(str12)
str13='https:\\sabiprogrammers.org\\home' #escape sequence to include \
print(str13)
str14='including\tDistance' #iclude tab in str14
print(str14)
str15='go to \nNext Line' #iclude newline
print(str15)

#string operators
str16='catherine'
str17='welcome back'
print(str16+str17)#concatenating two strings
print(str16*3)#kate how many times would i call
print(str16[0:4])#slicing
print(str16[5:9])#slicing
print('kate'in str16) #check if kate is in str16
print('back'in str17) #is back in str17
print('kate'not in str16) #check if kate is not in str16
print('come'not in str17) #is come not in str17
       




 

