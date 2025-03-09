        # Multiline Strings #
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

b = "Hello, World! "
c = "I'm a programmer. {}"
Umur = 20
#print(b[0]) # output: H

#print(b * 3) # output: Hello, World!Hello, World!Hello, World! # Fungsi * digunakan untuk menggabungkan string.

#print(len(b)) # output: 13 # Fungsi len() digunakan untuk menghitung jumlah karakter dalam string.

#print(b[7:12]) # output: World # Fungsi [x:y] digunakan untuk mengambil karakter dari index x sampai index y-1.

#print(b.lower()) # output: hello, world! # Fungsi lower() digunakan untuk mengubah semua karakter dalam string menjadi huruf kecil.
#print(b.upper()) # output: HELLO, WORLD! # Fungsi upper() digunakan untuk mengubah semua karakter dalam string menjadi huruf besar.
#print(b.replace('l', 'M')) # output: HeMMo, WorMd! # Fungsi replace() digunakan untuk mengganti karakter dalam string.
#print(b + c.format(Umur)) # output: Hello, World!I'm a programmer.20 # Fungsi format() digunakan untuk memasukkan nilai variabel ke dalam string.