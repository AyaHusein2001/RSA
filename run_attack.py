import attack as attak 


with open('pu_c.txt', "r") as file:
        contents = file.read()
        e_c=int(contents.split('\n')[0])
        n_c=int(contents.split('\n')[1])
        # print(e_c)
        # print(n_c)

with open('pu_s.txt', "r") as file:
        contents = file.read()
        e_s=int(contents.split('\n')[0])
        n_s=int(contents.split('\n')[1])
        # print(e_s)
        # print(n_s)

with open('cipher_c.txt', "r") as file:
        contents = file.read()
        cipher_c=contents.split('\n')
        cipher_c=[[int(x.strip('[]')) for x in s.split(',')] for s in cipher_c if s]
        # print(cipher_c)

with open('cipher_s.txt', "r") as file:
        contents = file.read()
        cipher_s=contents.split('\n')
        cipher_s=[[int(x.strip('[]')) for x in s.split(',')] for s in cipher_s if s]
        # print(cipher_s)

with open('plain_c.txt', "r") as file:
        contents = file.read()
        plain_c=contents.split('\n')
        #cipher_s=[[int(x.strip('[]')) for x in s.split(',')] for s in cipher_s if s]
        # print(plain_c)

with open('plain_s.txt', "r") as file:
        contents = file.read()
        plain_s=contents.split('\n')
        #cipher_s=[[int(x.strip('[]')) for x in s.split(',')] for s in cipher_s if s]
        # print(plain_s)

for cipher,i in zip(cipher_c,range(len(cipher_c))):
        m,v=attak.attack(cipher,n_s,e_s,plain_s[i])
        if(v):
          attak.write_to_file('client_revealed.txt',m)

for cipher,i in zip(cipher_s,range(len(cipher_s))):
        m,v=attak.attack(cipher,n_c,e_c,plain_c[i])
        if(v):
          attak.write_to_file('server_revealed.txt',m)

print('finished attack, please check client_revealed,server_revealed files to see revealed  messages ')
