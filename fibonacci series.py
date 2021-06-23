#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fibo(n):    #defining a function fibo 
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

noofterms=int(input("ENTER NO OF TERMS : "))    #getting no of terms from inpuy

# check if the number of terms is valid

if noofterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(noofterms):
       print(fibo(i))


# In[ ]:




