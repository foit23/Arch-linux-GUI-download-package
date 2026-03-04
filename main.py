from download_package import download_arch

print("вы запустили консольную версию программы, введите название пакета:")
if download_arch(input()):
    installed = "Программа установлена"
else:
    installed = "Произошла ошибка"

print(installed)