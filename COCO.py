name,age = input("enter ur name: n age: ").split()
Age = int(age)
if name[0] == 'a' or name[0] == 'A':
    if Age == 20:
        print("u can watch movie!!")
    else:
        print("ur not eligible")    
else:
    print("sorrie")        

if 'a' in name:
    print("okay") 

#we can check whether the string is empty or not
str=""
if str:
    print("not empty: ")
else:
    print("empty")   
n = input("value of n: ")
while (n <10 ):
    print("hello")
