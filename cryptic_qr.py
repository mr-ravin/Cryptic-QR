import sys
import os
from Crypto.Cipher import AES

def generate_qr(text,output_img="output.png"):
  command="qrencode -o "+str(output_img)+" \""+str(text)+"\""
  os.system(command)

def generate_qr_file(input_file,output_img="output.png",replace_char="`"):
  read_data=open(input_file,"r")
  text=read_data.read()
  text=text.replace("\n",replace_char)
  command="qrencode -o "+str(output_img)+" \""+str(text)+"\""
  os.system(command)
  
def output_file(text,output_file="result.txt",replace_char="`"):
  text=text.replace(replace_char,"\n")
  write_file=open(output_file,"w")
  write_file.write(text)
  write_file.close()
  
def output_text(text,replace_char="`"):
  text=text.replace(replace_char,"\n")
  return text

#### below code is under continuous development 
def encrypt_aes_text(key1,key2,text,replace_char="`"):
  text=text.replace("\n",replace_char)
  remaining=len(text)%16 # text should have length multiple of 16
  while remaining>0:
    text=text+"-"
    remaining=remaining-1
    
  remaining=len(key1)%16 # key1 should have length multiple of 16
  while remaining>0:
    key1=key1+"-"
    remaining=remaining-1

  remaining=len(key2)%16 # key2 should have length multiple of 16
  while remaining>0:
    key2=key2+"-"
    remaining=remaining-1

  encrypt_obj = AES.new(key1, AES.MODE_CBC,key2)
  encrypt_text=encrypt_obj.encrypt(text)
  return encrypt_text

def gen_qr_aes_file(key1,key2,file_name,replace_char="`"):
  file_dat=open(file_name,"r")
  file_data=file_dat.read()
  file_data=file_data.replace("\n",replace_char)
  file_data=encrypt_aes_text(key1,key2,file_data)
  output_file=file_name.split(".")[0]
  output_file=output_file+".png"
  file_dat.close()
  generate_qr(file_data,output_file)
  
def gen_qr_aes_text(key1,key2,text,output_file="output.png",replace_char="`"):
  text=text.replace("\n",replace_char)
  file_data=encrypt_aes_text(key1,key2,text)
  generate_qr(file_data,output_file)

def decrypt_aes_file(key1,key2,text,output_file="result.txt",replace_char="`"):
  remaining=len(key1)%16 # text should have length multiple of 16
  while remaining>0:
    key1=key1+"-"
    remaining=remaining-1

  remaining=len(key2)%16 # text should have length multiple of 16
  while remaining>0:
    key2=key2+"-"
    remaining=remaining-1

  decrypt_text = AES.new(key1, AES.MODE_CBC,key2)
  
  is_out=0
  while is_out!=1:
    if decrypt_text[-1]=='-':
      decrypt_text=decrypt_text[:-1]
    else:
      is_out=1
      
  write_file=open(output_file,"w")  
  decrypt_text=decrypt_text.replace(replace_char,"\n")
  write_file.write(decrypt_text)
  write_file.close()

  
def decrypt_aes_text(key1,key2,text,replace_char="`"):
  remaining=len(key1)%16 # text should have length multiple of 16
  while remaining>0:
    key1=key1+"-"
    remaining=remaining-1

  remaining=len(key2)%16 # text should have length multiple of 16
  while remaining>0:
    key2=key2+"-"
    remaining=remaining-1

  decrypt_obj = AES.new(key1, AES.MODE_CBC,key2)
  decrypt_text=decrypt_obj.decrypt(text)
  
  is_out=0
  while is_out!=1:
    if decrypt_text[-1]=='-':
      decrypt_text=decrypt_text[:-1]
    else:
      is_out=1    
  decrypt_text=decrypt_text.replace(replace_char,"\n")
  return decrypt_text
