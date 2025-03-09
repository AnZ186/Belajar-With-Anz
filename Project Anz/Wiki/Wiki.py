from tkinter import *
import wikipedia

def on_press():
    q=get_q.get()
    text.insert(INSERT,wikipedia.summary(q))

root = Tk() # kegunaan dari Tk() adalah untuk membuat window
root.title("Wikipedia") # untuk memberi judul pada window
pertanyaan = Label(root, text='Apa Itu ') # untuk memberi label pada window
pertanyaan.pack() #kegunaan dari pack() adalah untuk menampilkan label
get_q = Entry(root, bd=5) # untuk membuat kotak inputan
get_q.pack() # kegunaan dari pack() adalah untuk menampilkan kotak inputan
submit = Button(root, text='Cari', command=on_press) # untuk membuat tombol
# kegunaan dari command adalah untuk memanggil fungsi on_press
submit.pack() # kegunaan dari pack() adalah untuk menampilkan tombol
text =Text(root) # untuk membuat text
text.pack() # kegunaan dari pack() adalah untuk menampilkan text

root.mainloop() # kegunaan dari mainloop() adalah untuk menjalankan program