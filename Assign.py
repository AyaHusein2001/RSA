#!/usr/bin/env python
# coding: utf-8

# In[21]:


from sympy import randprime
import random


# In[22]:


def compute_gcd(m, n):
	if n == 0:
		return m
	else:
		r = m % n
		return compute_gcd(n, r)




# In[24]:


def choose_e(fin):
    e=random.randint(2,fin)
    gcd = compute_gcd(fin, e)
    if(gcd==1):
        d=int(pow(e,-1,fin))
        return e,d
    else:
        return choose_e(fin)


# 

# In[25]:


def encrypt(n,m,e):
    c=pow(m,e,n)
    return c


# In[26]:


def decrypt(n,d,c):
    m=pow(c,d,n)
    return m


# In[27]:


def verify(original_m,decryp_m):
    if(original_m==decryp_m):
        return True
    else:
        return False


# In[28]:


def gen_key(nbits):
    p = randprime(pow(2,(nbits)), pow(2,(nbits+1)))
    q = randprime(pow(2,(nbits)), pow(2,(nbits+1)))
    # print('p=',p)
    # print('q=',q)
    n=p*q
    fin=(p-1)*(q-1)
    e,d=choose_e(fin)
    return e,d,n,p,q





# In[30]:


def group_plaintext(text):
    # Append spaces to fill the last grouping
    num_spaces = 5 - (len(text) % 5)
    if num_spaces != 5:
        text += ' ' * num_spaces
    # Split plaintext into groups of five characters
    groups = [text[i:i+5] for i in range(0, len(text), 5)]
    return groups


# In[32]:


def map_char_to_num(char):
    # Convert alphanumeric characters to their corresponding numbers
    if char.isdigit():
        return int(char)
    elif char.isalpha():
        return ord(char.lower()) - 87
    # Treat all other characters as spaces
    else:
        return 36


# In[33]:


def str_to_num(text):
    # Convert each character in the string to a number
    nums = list(map(map_char_to_num, text))
    # Compute the plaintext number using the formula
    num = sum([nums[i] * (pow(37 , (len(nums) - 1 - i))) for i in range(len(nums))])
    return num


# In[34]:


def convert_to_numbers(group):
    # numbers = []
    # for group in groups:
        # Convert characters to numbers using ASCII codes
    num=str_to_num(group)
    # numbers.append(num)
    
    return num


# In[35]:


def encode_message(group):
    # groups = group_plaintext(message)
    # print(groups)
    num=convert_to_numbers(group)
    return num


# In[36]:


def num_to_char(num):
    # Convert a number to its original character according to the alphabet conversion
    if num < 10:
        return str(num)
    elif (num < 37 and num!=36):
        return chr(num + 87)
    else:
        return ' '

def num_to_str(num):
    # Convert a number to its original string representation
    chars = []
    while num > 0:
        chars.insert(0, num_to_char(num % 37))
        num //= 37
    return ''.join(chars)

def decode_message(num):
    # plaintext=''
    # for num in num:
    plaintext = num_to_str(num)
    return plaintext



# In[38]:


def rsa_encrypt(n,string_group,e):
    encoded_group=encode_message(string_group)
    # ciphertexts=[]
    # for num in nums:
    ciphertext=encrypt(n,encoded_group,e)

    # print(nums)
    return ciphertext


# In[39]:


def rsa_decrypt(n,d,ciphertext):
    # nums=[]
    # for ciphertext in ciphertexts:
    num=decrypt(n,d,ciphertext)
    # print(ciphertexts)
    message=decode_message(num)
    return message



