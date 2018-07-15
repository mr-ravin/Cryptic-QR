# Cryptic-QR
This repository contains QR code generation mechanism from a text present in a file. After performing encryption over the text, it then creates the QR code.

## Pre-Requisite
- [pycrypto](https://pypi.org/project/pycrypto/)

To install run:
```python
pip install pycrypto
```
- [qrencode](https://fukuchi.org/works/qrencode/)

To install run:
```python
$ sudo apt-get install qrencode
```

### How to use the library:

To Generate QR code from Text:
```
import cryptic_qr as cq
cq.generate_qr("text_here","outputQRfile.png") # It generates QR file named outputQRfile.png of text "text_here"
cq.generate_qr("textfile.txt","outputQRfile.png") # It generates QR file named outputQRfile.png of text present in textfile.txt
cq.gen_qr_aes_text(key1,key2,text,output_file="output.png",replace_char="`") # key1 and key2 are encryption keys, text is plain text which will be encrypted using AES encryption.
cq.gen_qr_aes_file(key1,key2,file_name,replace_char="`") # it reads plain text from file_name (.txt) file.
```
To Decrypt from QR code:
- Read QR using qr scanner.
- Pass the encrypted text to:
```python
cq.decrypt_aes_file(key1,key2,text,output_file="result.txt",replace_char="`") # text represents the encrypted text, and the decrypted text will get written in output_file.
cq.decrypt_aes_text(key1,key2,text,replace_char="`") # text represents the encrypted text, and the decrypted text will get return by the function.
```

Note: Currenlty, we are working on improving the encryption mechanism, so it is adviced to not use encryption, till this line is present in this documentation page.
