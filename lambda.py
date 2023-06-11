'''lambda fuctions'''

#Take a value from user
a=lambda:input('enter any number')
print(a())
b=lambda:input('enter any number')
print(b())

#To perform Arthimetic operation
multi= lambda x,y:x*y
c= int(input('enter any number'))
d=int(input('enter any number'))
print("multiplication of two numbrs",multi(c,d))


#square a value in list
List=lambda x:[i**2 for i in x]
user=int(input('enter how many numbers to be squared(ex.1,2,3,....)'))
L=[]
for i in range(1,user+1):
    L.append(i)
print(List(L))

 
