#!/usr/bin/env python
# coding: utf-8

# In[4]:



#Triangle Calculator
B= float  (input("Enter The Base = "))
H= float  (input("Enter The Height = "))
Area = (B*H)/2
print('ANSWER =',(round(Area,3)))


# In[22]:


#Triangler Prism Calculator
B= float  (input("Enter The Base  = "))
H= float  (input("Enter The Height  = "))
W= float  (input("Enter The Width = "))
Area = 0.5*H*B*W

print('ANSWER =',round(Area,2))


# In[ ]:


#Rectangle Calcalator
S1= float(input("Enter Side 1: "))
S2= float(input("Enter Side 2: "))
area=S1*S2
print('Answer:',(round(area,3)))


# In[ ]:


#Rectangler Prism Calcalator
B= float  (input("Enter The Base  = "))
H= float  (input("Enter The Height  = "))
W= float  (input("Enter The Width = "))
T=B*H*W
print('Answer :',(round(T,3)))


# In[ ]:


# 3D circle cal
pi=3.14
r= float (input("Enter the radius ="))
volume = (4/3)*3.14*r**3
print('ANSWER =',volume)


# In[ ]:


#Cicumference Calcalator
r= float (input("Enter The Radius: "))
t= 2*3.14*r
print('ANSWER =',t)


# In[20]:


#Ellispe Calcalator
r1= float  (input("Enter The 1st Radius  = "))
r2= float  (input("Enter The 2nd Radius  = "))

t=3.14*r1*r2
print('Answer =',(round(t,3)))


# In[11]:


#Area Calcalator
S1= float(input("Enter Side 1: "))
S2= float(input("Enter Side 2: "))
area=S1*S2
print('Answer:',(round(area,3)))


# In[12]:


#Cube Calcalator
B= float  (input("Enter The Base  = "))
H= float  (input("Enter The Height  = "))
W= float  (input("Enter The Width = "))
T=B*H*W
print('Answer :',(round(T,3)))


# In[7]:


#JUST SUM RANDOM VAR 

#week 1
sum_of_marks=float  (input("Enter 1st Mark  ="))
#week 2
sum_of_marks=sum_of_marks+float  (input("Enter 2nd Mark ="))
#week3
sum_of_marks=sum_of_marks+float  (input("Enter 3rd Mark ="))
#week4
sum_of_marks=sum_of_marks+float  (input("Enter 4nd Mark ="))

print('Sum Of Marks =',sum_of_marks)


# In[5]:


# Interest Calculator 
p= float  (input("Enter The Amount = "))
r= float  (input("Enter The Rate = "))
t= float  (input("Enter The Amount Of Time/yrs = "))
v = p*(r/100)*t
print('ANSWER =',(round(v,2)))


# In[28]:


#Grade Calcalator
grade1= float (input("Enter Your 1th Grade: "))
grade2= float (input("Enter Your 2th Grade: "))
grade3= float (input("Enter Your 3th Grade: "))
grade4= float (input("Enter Your 4th Grade: "))
t= (grade1+grade2+grade3+grade4)/4
print('ANSWER =',t)


# In[18]:


# Exponnets Cal = Heaven
a= float(input("Enter 1st Value: "))
b= float(input("Enter 2st Value: "))
t=a ** b
print(round(t,3))

