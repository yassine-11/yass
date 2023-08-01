print("hello")
print(5+3)
a=3
b=5
print(a+b)
for n in range(0,40):
   print(n)
   if n % 2 == 1:
        print("odd")
   else:
        print("even")     

fruitlist = ["apple","banana","grape","Orange"]
for fruit in fruitlist: 
    print(fruit)
c = 5 == 3
d = 7 > 3
print(c,d)
n=0
while n<50:
    print(n)
    n+=1
def addAnB(a,b):
    print("this is my function")
    return a+2*b
print(addAnB(4,2))
file1 = open ('data1.txt','r')
lines = file1.readlines()
print(lines)
for line in lines:
    #print(line)
    column = line.split(",")
    #print(column[1])
    if int(column[1]) > 30:
        print(line)

    
