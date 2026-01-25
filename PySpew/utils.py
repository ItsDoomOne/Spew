import platform, sys, os, shutil, base64, tarfile
import requests
import config as cfg
from pathlib import Path

system = platform.system()
print_if_disabled = False

if cfg.debug or cfg.print_if_disabled: 
    print_if_disabled = True

def debugprint(text):
    if cfg.debug:
        print(text)

def disabledprint(text):
    if print_if_disabled:
        print(text)

def path_setup():
    global tempPath
    if system == "Windows":
        tempPath = (os.getenv('TEMP')+"\\spew\\")
    elif system in ("Linux","Darwin","FreeBSD"):
        tempPath = ("/tmp/spew/")
    else:
        raise OSError("Unsupported operating system.")  
    os.makedirs(os.path.dirname(tempPath), exist_ok=True)
    return tempPath

def fancyexit(text=None):
    if not text == None:
        print(text)
    if os.path.exists(tempPath):
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
        
def execute_spewfile2(path):
    path_object = Path(path)
    if path_object.exists():
        #extract to temppath defined in main script
        print("WORK IN PROGRESS")
        