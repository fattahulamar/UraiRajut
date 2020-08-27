#!/usr/bin/env python
# coding: utf-8

# In[1]:


def urai(kata): 
    panjang =len(kata) #menghitung jumlah karakter
    hasil="" #membuat variable kosong
    for index in range(panjang+1): #menambahkan jumlah karakter setiap looping
        hasil+=kata[0:index] #hasil ditambah kata awal dan karakter yang ditambah setiap looping
    return hasil
print(urai('code'))


# In[2]:


def rajut(kata): 
    panjang =len(kata) #menghitung jumlah karakter
    hasil="" #membuat variable kosong
    for index in kata: #mengambil data pada kata
        hasil=kata[6:10] #mencetak karakter dengan index tertentu
    return hasil
print(rajut('ccocodcode'))


# In[ ]:




