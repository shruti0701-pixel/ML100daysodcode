#!/usr/bin/env python
# coding: utf-8

# # BASICS OF PYTHON

# In[1]:


import this


# In[3]:


first_name = "Shruti"
last_name = "Paul"
print("My first name is {} and last name is {}.".format(first_name,last_name))


# In[4]:


first_name = "Shruti"
last_name = "Paul"
print("My first name is {1} and last name is {0}.".format(last_name,first_name))


# In[8]:


a = input("Enter the number A: ")
b = input("Enter the number B: ")
print(int(a)+int(b))


# ## Tutorial  3 - Python Loops And Control Statements(Ifelse,for,while,break)

# In[4]:


#if statement

val_input = int(input("Enter the number "))
#val_input = int(user_input)
if val_input % 2 == 0:
    print ("True")
else:
    print("False")


# In[3]:


## Age form
##nested if else condition

age=float(input("Enter the age"))

if(age<18):
    print("Minor Age")
elif(age>=18 and age<=45):
    print("Mid Age")
elif(age>45 and age<=50):
    print("Senior Mid Age")
else: 
    print("Senior Citizen")


# In[6]:


#nestedifelse
age = int(input("Enter yout age: "))

if (age<18):
    print("Minor age")
    if(age<15):
        print("You are in school")
    else:
        print("You are in college")
elif(age >= 18 and age<=45):
    print("Mid age")
elif(age>=50 and age<=60):
    print("Senior Mid Age")
else:
    print("Senior Citizen")


# In[7]:


##Loops statement
##for loop, while loop

lst = [1,2,3,4,5,6,7,8,9]
for i in lst:
    print(i**2)


# In[8]:


##find the sum of all the elements in the list

lst = [1,2,3,4,5,6,7,8,9]
sum1=0
for i in lst:
   sum1 += i

print(sum1)


# In[10]:


## find the sum of even and odd number

lst = [1,2,3,4,5,6,7,8,9]
even_sum = 0
odd_sum = 0

for i in lst:
    if (i%2 == 0):
        even_sum=even_sum+i
    else:
        odd_sum+=i

print("Even sum is {}".format(even_sum))
print("Odd sum is {}".format(odd_sum))


# In[1]:


##while condition 

i=0
even_sum = 0
odd_sum = 0
while(i<=10):

    if(i%2==0):
       even_sum=even_sum+i
    else:
        odd_sum+=i
    i+=1
print(even_sum,odd_sum)


# In[2]:


##break 

x=1
while(x<7):
    if x==4:
        break
    print(x)
    x+=1


# In[5]:


##continue

x=0
while(x<7):
    x+=1
    if x==4:
        continue
    print(x)
    


# In[ ]:





# In[ ]:




