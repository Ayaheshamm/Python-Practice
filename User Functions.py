#1.password+username detection
list=[{'name':'omar','pass':'123'},{'name':'ahmed','pass':'456'}]

username = input('enter name:')
password = input('enter pass:')
for i in list:
    if i['name']== username and i['pass']== password:
      print('welcome')
      break
    elif i['name']== username and i['pass']!=password: 
       print ('wrong password')
       break
    elif i['name'] != username and i['pass']== password:
       print ('wrong user')
       break 
    else :
       print ('Try Again')

 #2.fill array of 5 elements from user ,sort it ascend,descend,display output 
elements =[]

for i in range (5):
     number = int(input('enter number:'))
     elements.append(number)

print(elements)

elements.sort()
print (elements)

elements.sort(reverse=True)   
print (elements)

#3. program generates multiplication table from 1 to passed number (list inside list)

given = int(input("Dear user enter number: "))

bblist = []  # big list

for i in range(1, given + 1):
    sslist = []  
    for j in range(1, i + 1):
        sslist.append(i * j)  
    bblist.append(sslist)  

print(bblist)

#4.ask user for name (no empty string,no int)
#then ask his email format djd@gmail.com

while True:
    name = input("Enter your name: ").strip()
    if name == "":
        print("invalid")
    elif name.isdigit():
        print("invalid")
    else:
        break

while True:
    email = input("Enter your email: ").strip()
    if "@" not in email or "." not in email.split("@")[-1]:
        print("Invalid email")
    else:
        break

print(name)
print(email)

