# Cryptic-QR
This repository contains QR code generation mechanism from a text present in a file. After performing encryption over the text, it then creates the QR code.

#### Code Developer: [Ravin Kumar](https://mr-ravin.github.io)

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
cq.generate_qr_file("textfile.txt","outputQRfile.png") # It generates QR file named outputQRfile.png of text present in textfile.txt
cq.gen_qr_aes_text(key1,key2,text,output_file="output.png",replace_char="`") # key1 and key2 are encryption keys, text is plain text which will be encrypted using AES encryption.
cq.gen_qr_aes_file(key1,key2,file_name,replace_char="`") # it reads plain text from file_name (.txt) file.
```


### To Decrypt text from QR code [If AES Encryption used]:
- Read QR using qr scanner.
- Pass the encrypted text to:
```python
cq.decrypt_aes_file(key1,key2,text,output_file="result.txt",replace_char="`") # text represents the encrypted text, and the decrypted text will get written in output_file.
cq.decrypt_aes_text(key1,key2,text,replace_char="`") # text represents the encrypted text, and the decrypted text will get return by the function.
```
### To Read text from QR code [If NO Encryption used]:

#### Note: We are doing this because qrencode can not process new line "\n", so at the time of qr code generation, we replaced that character with replace_char, and now to get the original text, we have to run one of the following functions described below.

- Read QR using qr scanner.
- Pass the text to:
```python
cq.output_file(text,output_file="result.txt",replace_char="`") # text represents the output text of QR code, and the original text will get written in output_file.
cq.output_text(text,replace_char="`") # text represents the output text of QR code, and the original text will get return by the function.
```

Note: Currenlty, we are working on improving the encryption mechanism, so it is adviced to not use encryption, till this line is present in this documentation page.
### When using text file as input, end file with a new line.

```python
Copyright (c) 2018 Ravin Kumar
Website: https://mr-ravin.github.io

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
