from tkinter import *
from tkinter import ttk
from download_package import download_arch

root = Tk()
root.title("Download your package!")
root.geometry("800x500")
root.resizable(False, False)

ttk.Style().configure(".", font="helvetica 13", foreground="#2F4F4F", padding=8,)
#ttk.Style().theme_use(".")


text_info = ttk.Label(text = "Вы можете устанавливать пакеты для дистрибутивов на базе Arch Linux используя эту программу. \nВведите название пакета:", font=("Arial", 12))
text_info.pack(anchor = CENTER, pady = 40)


entry = ttk.Entry(background = "#696969", foreground = "#696969")
entry.pack(anchor = S, pady = 10, ipady = 10, ipadx = 20)

installed = str

def start_download():
    global installed
    package_name = entry.get()
    if package_name == "":
        installed = "Ошибка! \nВы не можете ввести пустое поле"
    elif download_arch(package_name):
        installed = "Программа установлена"
    else:
        installed = "Ошибка! \nПакет не найден"

    print(installed)

btn_download = ttk.Button(text = "download", command = start_download)
btn_download.pack(anchor = S, pady = 30, ipadx = 40, ipady = 25)

def setting_window():
    window = Toplevel()
    window.title("settings")
    window.geometry("400x200")
    print("настройки открыты")

setting_btn = ttk.Button(text = "open setting", command = setting_window)
setting_btn.place(x = 700, y = 470)


root.mainloop()
