import platform, sys, shutil, base64, tarfile
import requests
from pathlib import Path
from os import getenv
system = platform.system()

def debugprint(debug, text):
    if debug == 1: print(text)
    else: return

def disabledprint(text, state=False):
    if state:
        print(text)

def path_setup():
    global tempPath
    if system == "Windows":
        tempPath = (getenv('TEMP')+"\\spew\\")
    elif system in ("Linux","Darwin","FreeBSD"):
        tempPath = ("/tmp/spew/")
    else:
        raise OSError("Unsupported operating system.")  
    Path(tempPath).mkdir(exist_ok=True, parents=True)
    return tempPath

def fancyexit(text=None):
    if not text == None:
        print(text)
    if Path(tempPath).exists:
        shutil.rmtree(tempPath)
    sys.exit()

def download_file(url, path):
    if (url.startswith("http://") or url.startswith("https://")):
        try:
            with open(path, "wb") as file:
                response = requests.get(url)
                file.write(response.content)           
        except requests.exceptions.RequestException as e:
            print("Error: either the protocol is incorrect or the URL is unreachable")
            debugprint(f"Details: {e}")

def help_prompt():
    print("Usage: spew [OPTION]... <path or url>")
    print("Display information about a Spew file.")
    print()
    print("Options:")
    print("  --help     display this info and exit")

def debugmenu():
    print("DEBUG MENU")
    print("You can: (1) Test current development material or (2) Exit ")
    option = input("Choose your fate: ")
    if option == "1":
        base64_decode("YQphYgphYmMKYWJjZAphYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5egoxMjM0NTY3ODkwCiciw6d+Xgo=", "/home/doom/bse")

def base64_decode(string, path):
    path_object = Path(path)
    if path_object.parent.exists():
        debugprint(f"{path} Parent is real")
        decoded = base64.b64decode(string)
        with open(path_object, "wb") as f:
            f.write(decoded)
    else:
        fancyexit(f"{path} Parent does not exist; halting.")

def ascii85_decode(string, path):
    path_object = Path(path)
    if path_object.parent.exists():
        debugprint(f"{path} Parent is real")
        decoded = base64.a85decode(string)
        with open(path_object, "wb") as f:
            f.write(decoded)
    else:
        fancyexit(f"{path} Parent does not exist; halting.")

def is_spew_file(filepath):
    try:
        with open(filepath, "r") as file:
            first_line = file.readline()
            if first_line.split()[0].lower() == "spew" and (file.name.endswith(".spew") or file.name.endswith(".spw")):
                return True
            else:
                return False
    except (IndexError, FileNotFoundError):
        return False
def nothing():
    return