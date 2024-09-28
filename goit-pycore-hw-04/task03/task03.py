import sys
from colorama import Fore, Style, init
from pathlib import Path

init(autoreset=True)

def visualise_directory_structure(path, space=0):
    try:
        directory = Path(path)
        if not directory.exists():
            print(f"{Fore.RED}Error: Path '{path}' does not exist.")
            return
        
        if not directory.is_dir():
            print(f"{Fore.RED}Error: Path '{path}' is not a directory.")
            return
        
        indent = ' ' * space
        for el in directory.iterdir():
            if el.is_dir():
                print(f'{Fore.BLUE}{indent}{el.name}')
                visualise_directory_structure(el, space + 4)
            else:
                print(f'{Fore.GREEN}{indent}{el.name}')
                
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Invalid command")
    else:
        visualise_directory_structure(sys.argv[1])