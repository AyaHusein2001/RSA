import socket
import threading
import pickle
import Assign as RSA
import attack as attack
import time


e,d,n,p,q=RSA.gen_key(27)

e_partner=None
n_partner=None

choice=input('server(1) or client (2):')
cipherfile=''
plainfile=''
if choice=="1":
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("192.168.1.6",9999))
    # server.bind(("172.28.104.39",9999))
    server.listen()
    client,_=server.accept()
    attack.write_to_file('pu_s.txt', e)
    attack.write_to_file('pu_s.txt', n)
  
    cipherfile='cipher_s.txt'
    plainfile='plain_s.txt'
    e_length = (e.bit_length() + 7) // 8
    e_bytes=e.to_bytes(e_length, byteorder='big')
    client.send(e_bytes)
    n_length = (n.bit_length() + 7) // 8
    n_bytes= n.to_bytes(n_length, byteorder='big')
    client.send(n_bytes)
    e_partner_bytes=client.recv(1024)
    e_partner=int.from_bytes(e_partner_bytes, byteorder='big')
    n_partner_bytes=client.recv(1024)
    n_partner=int.from_bytes(n_partner_bytes, byteorder='big')
    # print('waiting for connection ')
    # print('client Public n is ',n_partner)
elif choice=="2":
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("192.168.1.6",9999))
    # client.connect(("172.28.104.39",9999))
    attack.write_to_file('pu_c.txt', e)
    attack.write_to_file('pu_c.txt', n)
    cipherfile='cipher_c.txt'
    plainfile='plain_c.txt'
    e_partner_bytes=client.recv(1024)
    e_partner=int.from_bytes(e_partner_bytes, byteorder='big')
    n_partner_bytes=client.recv(1024)
    n_partner=int.from_bytes(n_partner_bytes, byteorder='big')
    e_length = (e.bit_length() + 7) // 8
    e_bytes=e.to_bytes(e_length, byteorder='big')
    client.send(e_bytes)
    n_length = (n.bit_length() + 7) // 8
    n_bytes= n.to_bytes(n_length, byteorder='big')
    client.send(n_bytes)
    # print('server Public e is ',e_partner)
    # print('server Public n is ',n_partner)

else:
    exit()

def sending_messages(c):
    while True:
        message=input("")
        groups = RSA.group_plaintext(message)
        enc_message=[]
        c.send(pickle.dumps(len(groups)))
        
        for group in groups:
            encrypted_group=RSA.rsa_encrypt(n_partner,group,e_partner)
            c.send(pickle.dumps(encrypted_group))
            enc_message.append(encrypted_group)
            time.sleep(1)
        attack.write_to_file(cipherfile, enc_message)
        print("You: "+message)

def recieving_messages(c):
    while True:
        no_groups=pickle.loads(c.recv(1024))
        dec_message=''
        for i in range(no_groups):
            # print('i=',i)
            decrypted_group=RSA.rsa_decrypt(n,d,pickle.loads(c.recv(1024)))
            dec_message+=decrypted_group
        attack.write_to_file(plainfile, dec_message)
        print("Partner: "+dec_message)

threading.Thread(target=sending_messages,args=(client,)).start()
threading.Thread(target=recieving_messages,args=(client,)).start()