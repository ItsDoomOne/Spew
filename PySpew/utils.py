import platform, sys, os, shutil
import config as cfg

system = platform.system()

def debugprint(text):
    if cfg.debug:
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

def help_prompt():
    print("Usage: spew [OPTION]... <path or url>")
    print("Display information about a Spew file.")
    print()
    print("Options:")
    print("  --help     display this info and exit")