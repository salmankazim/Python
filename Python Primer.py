#!/usr/bin/env python
# coding: utf-8

# In[113]:


8*3


# In[114]:


37/2


# In[ ]:


oneline = "234234ljaljf"
singlequote= '342lfd  aslf7s8'
print(oneline)
print(singlequote)
print()
multiline = '''This is first line

this is second line

this is third line'''
print(multiline)


# In[203]:


singlequote = 'he says "aren\'t shouldn\'t wouldn\'t"'
print(singlequote)

doublequote = "he says \"aren't shouldn't wouldn't\""
print(doublequote)

triplequote = '''he says "aren't wouldn't shouldn't"'''
print(triplequote)


# In[ ]:


myscore = 1000
message = "my score is %s boom 😍"
print(message %myscore)


# In[ ]:


string = " what did the number %s said to the number %s "
print(string %(9,3))
print(string %(3,9))
print(string %("sal",'sna'))
print(string %('san','sal'))


# In[ ]:


print(100*"sal")
print(100*"sal\t")
print(100*"sal\n")


# ## lists

# In[29]:


my_list = ['shampoo',"vegi",'fruit','''medicint''','pens',3,2,4]
print(my_list[4])
print(my_list[0:])
print(my_list[0:3])
print(my_list[:5])
print(my_list[:-1])


# In[76]:


string_list = ["i","am", "me", "no", "body","is","like"]
# string_list.append('me')
num_list = [1,2,34,5,3,6,34]

print(string_list)
string_list.append("me")
string_list.append('''This is other
  string''')

print(num_list)
print(string_list)

del string_list[8]
merge_list = [string_list,num_list]
merge_list2 = [num_list,string_list]

print(merge_list)
print(merge_list2)

list3 = [string_list+num_list]
print(list3)

list4 = (string_list+num_list)
print(list4)

list5 = string_list + num_list
print(list5)

sw=string_list*4
print(sw)


# # tuples
# we can't change the value in tuples

# In[86]:


my_tuples = ("he " ,"is ",34,34,234,54,5,64,5)
print(my_tuples)
print(my_tuples[0])

my_tuples1 = ("he " ,"is ",34,34,234,54,5,64,5)
print(my_tuples)

tuple3 = my_tuples+ my_tuples1 
print(tuple3)

tuple4 = tuple3*5
print(tuple4)


# # Maps or dictionary
# we can't add to maps by + operateator like lists

# In[91]:


my_dic = {
    "ali":"football",
    "asad":"badminion",
    "taha":"marshal art"
}
my_dic["taha"]="squas"
print(my_dic)

del my_dic["ali"]
print("this is after removing ali: " ,my_dic)

# This is not working in the case of dictionary like tuples and lists
# mul = my_dic*5
# print(mul)


# # conditions 

# In[117]:


age = 494
if (age < 50):   
    print("you are young")
else:
    print("Huh: ?")


# In[138]:


age = 203
if (age > 0 and age <=5):
    print("you are a baby you can sit and crawal")
elif(age > 5 and age <= 10):
    print("you can run")
elif(age >=10 and age <= 20):
    print("YOu can go out side")
elif(age > 20 and age < 60):
    print("you can do anything you want:")
else:
    print("Huhh! No idea")


# In[141]:


age = '23'
age = int(age)
if (age > 0 and age <=5):
    print("you are a baby you can sit and crawal")
elif(age > 5 and age <= 10):
    print("you can run")
elif(age >=10 and age <= 20):
    print("YOu can go out side")
elif(age > 20 and age < 60):
    print("you can do anything you want:")
else:
    print("Huhh! No idea")


# In[147]:


age = '23.4'
age = float(age)
if (age > 0 and age <=5):
    print("you are a baby you can sit and crawal")
elif(age > 5 and age <= 10):
    print("you can run")
elif(age >=10 and age <= 20):
    print("YOu can go out side")
elif(age > 20 and age < 60):
    print("you can do anything you want:")
else:
    print("Huhh! No idea")


# In[151]:


age = 23
age = str(age)
if (age == "23"):
    print("you are a baby you can sit and crawal")
elif(age == '23'):
    print("you can run")
elif(age =='10' and age == '20'):
    print("YOu can go out side")
elif(age == '23'):
    print("you can do anything you want:")
else:
    print("Huhh! No idea")


# In[176]:


for i in range(0,20):
    print("hi",i)


# In[175]:


for i in range(0,20):
    print("hi%s" %i)


# In[181]:


my_list = ['shampoo',"vegi",'fruit','''medicint''','pens',3,2,4]
for i in my_list:
    print(i)
#     print(i)
    for j in my_list:
        print(j)


# In[191]:


x = 45
y = 80
while x < 50 and y < 100:
    x = x+1
    y = y+1
    print(x,y)


# In[188]:


print(list(range(20,32)))


# In[189]:


for i in range(23,29):
    print(i)


# # function

# In[209]:



myname = "salman"

def func(name):
    print("my name is %s. "%(name),"Hi!!!✌")

func(myname)


# In[206]:


def function(fname,lname):
    print("Your first name is %s and your last name is %s" %(fname,lname))
    print("But in passport it would be look like %s %s" %(lname, fname))
function("salman","kazim")


# In[226]:


import time
print(time.asctime())


# # Class and objects

# In[230]:


class Things:
    pass
class animate(Things):
    pass
class unanimate(Things):
    pass
class mammals(animate):
    pass
class giraffe(mammals):
    pass
monkey = giragge()


# In[ ]:


class Animals(Animate):
    def to_move(self):
        pass
    def to_breath(self):
        pass
    def to_eatFood(self):
        pass


# In[233]:


def normal_function():
    print("This is from normal function")
    
class myClass:
    def func():
        print("this method from inside the class: ")
    def otherFun():
        print("This funtion from the other method: ")
        
    


# In[246]:


test=[]
print (bool(test))

test1=[0]
print(bool(test1))

test2 = 0
print(bool(test2))

test3= 0.0
print(bool(test3))

test4 = 1
print(bool(test4))

testnull = None
print("None: ",bool(testnull))

String = ""
print("String: ", bool(String))


# In[247]:


list = [234,34,25,]
dir(list)


# In[262]:


print('\n return value from empty dir()')
print(dir(C:/Window))


# In[ ]:





# In[ ]:





# In[ ]:




