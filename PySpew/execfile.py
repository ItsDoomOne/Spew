import config as cfg
import subprocess, os
from utils import debugprint, fancyexit, disabledprint

def shellexec(shellexec):
    if not cfg.disable_shell:
        subprocess.run(shellexec, shell=True)
    else:
        disabledprint(f"DEBUG: Shell is disabled. Tried to run {shellexec}")
def mkdirexec(mkdirexec):
    if not cfg.disable_mkdir:
        os.mkdir(mkdirexec)
    else:
        disabledprint(f"DEBUG: Mkdir is disabled. Tried to create {mkdirexec}")
def printexec(printexec):
    if not cfg.disable_print:
        print(printexec)
    else:
        disabledprint(f"DEBUG: Print is disabled. Tried to print {printexec}")

def removeexec(removepath):
    if not cfg.disable_delete:
        debugprint(f"Path to be removed is {removepath}")
        if not os.path.exists(removepath):
            debugprint(f"DEBUG: Path {removepath} does not exist")
            fancyexit()
        if os.path.isfile(removepath):
            debugprint(f"DEBUG: Path {removepath} appears to be a file")
            os.remove(removepath)
        else:
            debugprint(f"DEBUG: Path {removepath} appears to be a folder")
            os.rmdir(removepath) #currently only deletes empty directories. 
    else:
        disabledprint(f"DEBUG: Delete is disabled. Tried to delete {removepath}")