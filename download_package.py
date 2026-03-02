import subprocess
import sys
from getpass import getpass


def download_arch(package):
    
    try:
        subprocess.run(
            ["pacman", "-S", package],
            capture_output = True,
            text = True,
            input = "y"
        )
        
        
        check_package = subprocess.run(["pacman", "-Qe", package])        
        if check_package.returncode == 0:
            return True
        else:
            return False

    except subprocess.SubprocessError as e:
        print(f"ошибка: {e}")
        return False

    