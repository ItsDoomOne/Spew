from subprocess import run as runproc
from utils import debugprint, fancyexit, disabledprint, base64_decode, ascii85_decode, download_file
from pathlib import Path

def shellexec(run):
    if run == "":
        return
    if not flags["disable_shell"]:
        runproc(run, shell=True)
    else:
        disabledprint(f"DEBUG: Shell is disabled. Tried to run {run}", kaboom)

def mkdirexec(run):
    if run == "":
        return   
    if not flags["disable_mkdir"]:
        Path(run).mkdir()
    else:
        disabledprint(f"DEBUG: Mkdir is disabled. Tried to create {run}", kaboom)

def printexec(run):
    if run == "":
        return
    if not flags["disable_print"]:
        print(run)
    else:
        disabledprint(f"DEBUG: Print is disabled. Tried to print {run}", kaboom)

def removeexec(run):
    if run == "":
        return
    if not flags["disable_delete"]:
        debugprint(f"Path to be removed is {run}")
        if not Path(run).exists():
            debugprint(f"DEBUG: Path {run} does not exist")
            fancyexit()
        if Path(run).is_file():
            debugprint(f"DEBUG: Path {run} appears to be a file")
            Path(run).unlink()
        else:
            debugprint(f"DEBUG: Path {run} appears to be a folder")
            Path(run).rmdir() #currently only deletes empty directories. 
    else:
        disabledprint(f"DEBUG: Delete is disabled. Tried to delete {run}", kaboom)

def fileexec(run):
    if run == "":
        return
    if not len(run.split()) == 3:
        fancyexit("File command is malformed.")
    filetype = (run.split()[0]).lower()
    content = (run.split()[1])
    path = (run.split()[2]).lower()
    if filetype == "inline":
        #inlinelogic
        print("Inline is not implemented")
    elif filetype == "b64":
        base64_decode(content, path)
    elif filetype == "a85":
        ascii85_decode(content, path)
    elif filetype == "url":
        download_file(content, path)
    else:
        debugprint(f"File type {filetype} does not exist.")
    return    

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


validcommands = {
    "spew": None,
    "print": printexec,
    "shell": shellexec,
    "delete": removeexec,
    "mkdir": mkdirexec,
    "file": fileexec,
    "unzip": unzipexec,
    "alias": aliasexec,
    "delalias": delaliasexec,
}

def execute_file(filepath, flags1):
    try:
        global flags
        global kaboom 
        flags = flags1
        if flags["debug"] or flags["print_if_command_disabled"]:
            kaboom = True
        else: kaboom = False
        with open(filepath, "r") as file:
            for line in file:
                stripped = line.strip()
                if not stripped:
                    continue
                currentCommand = ((stripped.split()[0]).lower())
                if currentCommand in validcommands:
                    remove = (len(currentCommand) + 1)
                    content = stripped[remove:].strip()
                    currentFunction = validcommands.get(currentCommand)
                    if not currentFunction:
                        continue
                    if len(content) >= 2 and content[0] == content[-1] and content[0] in ("\"", "'"):
                        currentFunction(content[1:-1])
                    else:
                        currentFunction(content)
    except Exception as e:
        print("Error parsing file:", e)
        fancyexit()