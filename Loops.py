
#1.Program counts up no. of vowels (a,e,i,o,u)  ##solved using basic loop 
word=input('enter your word:')
vowels='a,e,i,o,u'
i=0 
for x in word:
     if x in vowels:
       i+=1
print ('vowels no is',i)

#2.Program print location of i in any string 
#using len
noun = input('enter something:')
for ind in range(len(noun)):
    if noun[ind]=='i':
       print ('i location is',ind)
#no len
noun = input('enter something:')
i=0 
for x in noun:
    if x == 'i':
      print('i location is',i)
    i+=1

#3.Program generates muliplication table from 1 to passed no.
number = int(input('enter new number:'))
start = 1 

while start<=number:
   for i in range (1,13):
     print (f"{start} x {i}={start*i}")
     
   start+=1

#4.Mario
mario= int(input('enter height'))

for i in range (1,mario+1):
    print('*'* i)


             





