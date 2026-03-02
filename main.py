from tkinter import *
from tkinter import ttk
from download_package import download_arch

root = Tk()
root.title("Download your package!")
root.geometry("800x500")
root.resizable(False, False)

ttk.Style().theme_use("clam")

text_info = ttk.Label(text = "Вы можете устанавливать пакеты для дистрибутивов на базе Arch Linux используя эту программу. \nВведите название пакета:", font=("Arial", 12))
text_info.pack(anchor = CENTER, pady = 40)



entry = ttk.Entry()
entry.pack(anchor = S, pady = 10, ipady = 10, ipadx = 20)

installed = str

def start_download():
    global installed
    package_name = entry.get()
    if download_arch(package_name):
        installed = "Программа установлена"
    else:
        installed = "Произошла ошибка"

    print(installed)

btn_download = ttk.Button(text = "download", command = start_download)
btn_download.pack(anchor = S, pady = 30, ipadx = 40, ipady = 25)


root.mainloop()
