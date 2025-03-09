import string
import random
from csv import writer




def password_generator():
    huruf_kecil = string.ascii_lowercase # kegunaan string.ascii_lowercase adalah untuk menghasilkan huruf kecil
    huruf_besar = string.ascii_uppercase # kegunaan string.ascii_uppercase adalah untuk menghasilkan huruf besar
    angka = string.digits # kegunaan string.digits adalah untuk menghasilkan angka
    simbol = string.punctuation # kegunaan string.punctuation adalah untuk menghasilkan simbol
    platfrom = input("Masukkan nama platform: \n") # input nama platform yang diinginkan # kegunaan \n adalah untuk membuat baris baru
    pass_length = int(input("Masukkan panjang password: \n")) # input panjang password yang diinginkan # kegunaan \n adalah untuk membuat baris baru
    hasil = []
    hasil.extend(list(huruf_kecil)) # menambahkan huruf kecil ke dalam list hasil
    hasil.extend(list(huruf_besar)) # menambahkan huruf besar ke dalam list hasil
    hasil.extend(list(angka)) # menambahkan angka ke dalam list hasil
    hasil.extend(list(simbol)) # menambahkan simbol ke dalam list hasil
    random.shuffle(hasil) # mengacak list hasil
    password = ("".join(hasil[0:pass_length])) # menggabungkan list hasil dengan panjang 16
    print(password)
    passdata=[platfrom,password] # membuat list head dimana berisi Platfrom dan Password
    with open('password.csv','a') as f: # membuka file csv bernama password.csv dan menuliskan file tersebut # f adalah variabel yang digunakan untuk membuka file csv
      nulisdata = writer(f) # menulis file csv dan f adalah variabel yang digunakan untuk membuka file csv
      nulisdata.writerow(passdata) # menulis list head ke dalam file csv. # kegunaan writerow adalah untuk menulis baris ke dalam file csv

password_generator()