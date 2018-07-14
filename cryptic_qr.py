import sys
import os
from Crypto.Cipher import AES

def generate_qr(text,filename):
  command="qrencode -o "+str(filename)+" \""+str(text)+"\""
  os.system(command)

def encrypt_aes_text(key1,key2,text,replace_char="`"):
  text=text.replace("\n",replace_char)
  encrypt_obj = AES.new(key1, AES.MODE_CBC,key2)
  encrypt_text=encrypt_obj.encrypt(text)
  return encrypt_text

def gen_qr_aes_file(key1,key2,file_name,replace_char="`"):
  file_dat=open(file_name)
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
  text=text.replace(replace_char,"\n")
  decrypt_text = AES.new(key1, AES.MODE_CBC,key2)
  write_file=open(output_file,"w")
  write_file.write(decrypt_text)
  write_file.close()

def decrypt_aes_text(key1,key2,text,replace_char="`"):
  text=text.replace(replace_char,"\n")
  decrypt_obj = AES.new(key1, AES.MODE_CBC,key2)
  decrypt_text=decrypt_obj.decrypt(text)
  return decrypt_text
