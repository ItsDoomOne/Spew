import platform, sys, os, shutil

system = platform.system()

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