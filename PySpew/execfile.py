import config as cfg
import subprocess, os
from utils import debugprint, fancyexit, disabledprint

def shellexec(run):
    if run == "":
        return
    if not cfg.disable_shell:
        subprocess.run(run, shell=True)
    else:
        disabledprint(f"DEBUG: Shell is disabled. Tried to run {run}")
def mkdirexec(run):
    if run == "":
        return   
    if not cfg.disable_mkdir:
        os.mkdir(run)
    else:
        disabledprint(f"DEBUG: Mkdir is disabled. Tried to create {run}")
def printexec(run):
    if run == "":
        return
    if not cfg.disable_print:
        print(run)
    else:
        disabledprint(f"DEBUG: Print is disabled. Tried to print {run}")

def fileexec(run):
    if run == "":
        return
    print("not implemented")

def unzipexec(run):
    if run == "":
        return
    print("not implemented")

def aliasexec(run):
    if run == "":
        return
    print("not implemented")

def delaliasexec(run):
    if run == "":
        return
    print("not implemented")

def removeexec(run):
    if run == "":
        return
    if not cfg.disable_delete:
        debugprint(f"Path to be removed is {run}")
        if not os.path.exists(run):
            debugprint(f"DEBUG: Path {run} does not exist")
            fancyexit()
        if os.path.isfile(run):
            debugprint(f"DEBUG: Path {run} appears to be a file")
            os.remove(run)
        else:
            debugprint(f"DEBUG: Path {run} appears to be a folder")
            os.rmdir(run) #currently only deletes empty directories. 
    else:
        disabledprint(f"DEBUG: Delete is disabled. Tried to delete {run}")