import smtplib # Fungsi import smtplib adalah fungsi yang digunakan untuk mengimport modul smtplib


tujuan = input("Masukkan email tujuan: ") # Fungsi input adalah fungsi yang digunakan untuk memasukkan data
pesan = input("Masukkan pesan:") # Fungsi input adalah fungsi yang digunakan untuk memasukkan data


def sendEmail(tujuan, pesan): # Fungsi sendEmail adalah fungsi yang digunakan untuk mengirim email
    server = smtplib.SMTP('smtp.gmail.com', 587) # Fungsi smtplib.SMTP adalah fungsi yang digunakan untuk mengirim email melalui server smtp.gmail.com dengan port 587
    server.starttls() # Fungsi server.starttls adalah fungsi yang digunakan untuk memulai koneksi yang aman
    server.login('zr1agam@gmail.com', 'PASSWORD') # Fungsi server.login adalah fungsi yang digunakan untuk login ke email pengirim
    server.sendmail('zr1agam@gmail.com', tujuan , pesan ) # Fungsi server.sendmail adalah fungsi yang digunakan untuk mengirim email
    server.close() # Fungsi server.close adalah fungsi yang digunakan untuk menutup koneksi

sendEmail(tujuan,pesan)
print("Email has been sent successfully!")