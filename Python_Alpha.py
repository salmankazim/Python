#!/usr/bin/env python
# coding: utf-8

# # string subtitution

# In[172]:


float_string2 = "%.3f" % (1.232343)
float_string2


# In[174]:


print("%(value)s %(value)s %(value)s !" % {"value":"Sharfoo"})


# In[163]:


xy= {"x":0, "y":10}
print("Graph a point at where x={x} and y={y}".format(**xy))


# In[166]:


"Python is as simple as {0}, {1}, {2}".format("a", "b", "c")


# In[167]:


print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2, "z":3})


# In[168]:


print("%(value)s %(value)s %(value)s !" % {"value":"Sharfoo"})


# In[ ]:


i = 0
while (i < 10):
    print(i)
    i = i + 1


# In[5]:


i = 0 
while(i < 10):
    print(i)
  
    if(i == 0):
        break
    i += 1
 


# In[13]:


i = 0
while(i < 10):
    i += 1
    if(i == 3):
        continue
        print(i)
        if(i == 8):
            break
            i += 1
    print(i)

        


    


# In[14]:


i = 0
while(i < 10):
    i += 1
    print(i)


# In[22]:


my_list = list(range(10))
print(my_list)
for i in my_list:
#     print(i)
    if(i == 31):
        print("item found! ")
        break
else:
    print("It wasn't found")


# # List Comprehension

# In[30]:


#old version
string = "pakisisafj"
list1 = []
for letter in string:
    list1.append(letter)
list1


# In[32]:


#list comprehension
mystring = "234l7safo"
list1 = [letter for letter in mystring]
list1


# In[33]:


#another example is
mylist = [char for char in "abcdegfa"]
mylist


# In[34]:


numlist = [num for num in range(12,23)]
numlist


# In[36]:


#when we cast a string into integer
mystring = ['1','2','3','3','4','5']
cast = [int(num) for num in mystring]
cast
type(cast)


# In[48]:


mystring = ['1 2    ','      2   d','3b ','3 b','4','5']
strip = [char.strip() for char in mystring]
strip


# In[53]:


mylist = [[1,2,3], [4,5,6], [7,8,9],[10,11,12]]
newlist = [number for element in mylist for number in element]
newlist


# In[62]:


#dictionary comprehension
print({i:str(i)+"value" for i in range(10)})


# In[73]:


mydictionaray = {1:"horse", 2:"cat", 3:"dog", 4:"lion"}
print({values:keys for keys,values in mydictionaray.items()})
mydictionaray.keys()
mydictionaray.values()


# In[76]:


#set
myList = ['1','2','3','3','4','5','4',"5"]
set(myList)


# In[77]:


set("aabbccdeeefssldjkgjal")


# In[9]:


#another way of set comprehension
myList1 = ['1','2','3','3','4','5','4',"5"]
my_set = {e for e in myList1}
my_set


# # error/exception handling

# In[10]:


1/0


# In[21]:


try:
    1/0
except ZeroDivisionError:
    print("you can't divide by zero: ")
        
    


# In[23]:


#Bare Except
try:
    1/0
except:
    print("you can't dividie by zero ")


# In[29]:


12/2


# In[40]:


my_string= ("I like %s") %( "Python")
my_string


# In[50]:


my_dict= {"a":1, "b":2, "c":3}
try:
    print(my_dict["d"])
except KeyError:
    print("The key is not found")


# In[56]:


mylist = [1,2,3,4,5,6]
try:
    print(mylist[5])
except IndexError:
    print("The index doesn't exist")


# In[78]:


mydict = {1:"a", 2:"b",3:"c",4:"d"}
try:
     mydict[5]
except KeyError:
    print('The key doesn\'t exist')
except IndexError:
    print("The index doen\'t exist")
except:
    print("Some unknown error")


# In[82]:


mydict = {1:"a", 2:"b",3:"c",4:"d"}
try:
    mydict[14]
except (IndexError,KeyError):
    print("The key or index error is possible")


# In[85]:


mydict = {1:"a", 2:"b",3:"c",4:"d"}
try:
     mydict[1]
except KeyError:
    print('The key doesn\'t exist')
except IndexError:
    print("The index doen\'t exist")
except:
    print("Some unknown error")
finally:
    print("The finally statement is executed")


# In[91]:


mydict = {1:"a", 2:"b",3:"c",4:"d"}
try:
    mydict[13]
except (IndexError,KeyError):
    print("The key or index error is possible")
else:
    print("no Error is executed")
finally:
    print("the finally statement is executed")


# In[94]:


mydict = {1:"a", 2:"b",3:"c",4:"d"}
try:
     mydict[15]
except KeyError:
    print('The key doesn\'t exist')
except IndexError:
    print("The index doen\'t exist")
except:
    print("Some unknown error")
else:
    print("no Error is executed")
finally:
    print("The finally statement is executed")


# # File handling

# In[107]:


x = open(r"D:\test.txt","r")
data = x.read()
print(data)
x.close()


# In[148]:


x = open(r"D:\test.txt","r")
datum = x.readline()
data = x.readlines()
print(datum)
print(data)
x.close()


# In[145]:


text = open(r"D:\test.txt","r")
# data = text.read()
# print(data)
for lines in text:
    print(lines)
text.close()


# In[155]:


text = open(r"D:\test.txt","w")
dataa = text.write("""this elsdja
aflkasdfjsdoiafj


aflsdfjaifua
afalsdfjsdlaf""")
text.close()
# print(dataa)


# # import

# In[157]:


import this


# In[175]:


import math
math.sqrt(4)
math.ceil(3.5)
math.floor(3.5)


# In[178]:


from math import sqrt
sqrt(5)
sqrt(98)


# In[181]:


from math import sqrt,pi
pi
sqrt(3)


# In[189]:


from math import*
# sqrt =5
sqrt(5)
print(sqrt)


# In[195]:


def function():
    print("This is my first function: ")
function()


# In[197]:


def empty_function():
    pass
empty_function()


# In[203]:


def add(a,b):
    return a+b
add(3,3)
add(3,5)
add(a=5,b=9)
total = add(a=1,b=2)
print(total)


# In[212]:


def keywordFunction(a=2,b=2,c=3):
    return a+b+c
keywordFunction(a=1,b=1,c=1)


# In[246]:


def mixFunction(a,b=7,c=3):
    return a+b+c
# mixFunction(2,3,5)
#this is also default arguement keyword function
mixFunction(9)


# In[248]:


def mixed_function(a, b, c=3):
    return a+b+c
mixed_function(2,3)


# In[249]:


# To get infinite arguments, we use * argsand for infinite we use ** kwargs


# In[262]:


def infinite(*args , **keyargs):
    print(args)
    print(keyargs)
infinite(122,35,235,c=5,d=3,e=5,g=3)


# In[274]:


def fun1():
    a=1
    b=3
    return a+b
def fun2():
    c=5
    return a+c
fun1()
fun2()


# In[276]:


def fun1():
    global a
    a=11
    b=3
    return a+b
def fun2():
    c=5
    return a+c
print(fun1())
fun2()


# # class

# In[278]:


x = "salman"
dir(x)


# In[280]:


class myclass:
    "this is string"
    def __init__(self):
        "this is constructor"
        pass


# In[296]:


class Vehicle:
    "this is vehicle class"
    def __init__(self,doors,tires,color):
        self.doors = doors
        self.tires = tires
        self.color = color
    def brake(self):
        "Stop the car"
        return "stop"
    def drive(self):
        d = "drive the car"
        return d
print(Vehicle.brake)


# In[ ]:




