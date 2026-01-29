import sys, requests
from utils import path_setup, fancyexit, help_prompt, debugprint, debugmenu
from execfile import printexec, shellexec, mkdirexec, removeexec, fileexec, unzipexec, aliasexec, delaliasexec
from pathlib import Path
from config import flags, check_flags

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
tempPath = path_setup()
tempFile = (f"{tempPath}spewfile.spew")

try:
    fullarguments = " ".join(sys.argv[1:])
    argument1 = sys.argv[1]
    check_flags(fullarguments)
    debug = flags["debug"]
    debugprint(debug, f"DEBUG: fullarguments = {fullarguments}")
    debugprint(debug, f"DEBUG: argument1 = {argument1}")
except IndexError:
    help_prompt()
    fancyexit() 

def execute_file(filepath):
    try:
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

debugprint(debug, "DEBUG: Execution passed defs")

try:           
    if argument1 == "--help":
        help_prompt()
    elif Path(argument1).is_file() and is_spew_file(argument1):
        debugprint(debug, "DEBUG: input is a file.")
        execute_file(argument1)
    elif (argument1.startswith("http://") or argument1.startswith("https://")):
        try:
            with open(tempFile, "wb") as file:
                response = requests.get(argument1)
                file.write(response.content)
                is_spew_file(tempFile)
                execute_file(tempFile)             
        except requests.exceptions.RequestException as e:
            print("Error: either the protocol is incorrect or the URL is unreachable")
            debugprint(debug, f"Details: {e}")
    else:
        print(f"Error:{fullarguments} is invalid") 
except IndexError:
    raise IndexError
except Exception as e:
    debugprint(debug, f"DEBUG: Execution halted: {e}")
    fancyexit()    
finally:
    fancyexit()
