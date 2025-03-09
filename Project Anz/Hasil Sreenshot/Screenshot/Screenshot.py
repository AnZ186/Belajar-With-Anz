import pyautogui # Fungsi untuk memangil library pyautogui
import time # Fungsi untuk memangil library time
import tkinter as tk # Fungsi untuk memangil library tkinter sebagai tk

def screenshot():
    pyautogui.alert("Udah Pas?") # Fungsi untuk memberikan alert
    time.sleep(0) # Fungsi untuk memberikan delay waktu
    nama = time.time() # Fungsi untuk memberikan nama file screenshot
    nama = 'C:/Users/anzissquid/Desktop/Belajar Python/Project Anz/Hasil Sreenshot/{}.png'.format(nama) # Fungsi untuk memberikan path file screenshot
    gambar = pyautogui.screenshot() # Fungsi untuk mengambil screenshot
    gambar.save(nama) # Fungsi untuk menyimpan screenshot
    gambar.show() # Fungsi untuk menampilkan screenshot

root = tk.Tk() # Fungsi untuk membuat window
frame = tk.Frame(root) # Fungsi untuk membuat frame
frame.pack() # Fungsi untuk menampilkan frame

tombol = tk.Button(frame, text="Take Screenshot", command=screenshot) # Fungsi untuk membuat tombol screenshot
tombol.pack(side=tk.LEFT)

tutup = tk.Button(frame, text="Quit", command=quit) # Fungsi untuk membuat tombol quit
tutup.pack(side=tk.LEFT)

root.mainloop() # Fungsi untuk menjalankan window