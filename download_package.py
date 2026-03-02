import subprocess
import sys
from getpass import getpass
import shlex

def download_arch(package):
    
    password = getpass("Пароль sudo: ")
    
    try:
        process = subprocess.run(
            ["echo", password, "|", "sudo", "pacman", "-S", package],
            input = "y",
            text = True,
            capture_output=True,                        
        )
        print(process.stdout)
        print("запуск установки...")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ошибка: {e}")
        return False

