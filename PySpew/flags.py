# This file is intended for testing the runtime flags.
# It will be removed a few commits from now and just exists to prove my work is not AI-made.
# It's very stupid, but I really don't want to just spew a finished work of code in the main file
# And I dont wanna mess with branches right now. I just want to work.
import sys, os, requests
from PySpew.utils import path_setup, fancyexit, help_prompt, debugprint
from PySpew.execfile import printexec, shellexec, mkdirexec, removeexec, fileexec, unzipexec, aliasexec, delaliasexec
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

debugprint("DEBUG: Execution passed defs")

try:
    fullarguments = " ".join(sys.argv[1:])
    argument1 = sys.argv[1]
    debugprint(f"DEBUG: fullarguments = {fullarguments}")
    debugprint(f"DEBUG: argument1 = {argument1}")
except IndexError:
    help_prompt()
    fancyexit() 

debugprint("DEBUG: Execution passed the argument processing")

try:           
    if argument1 == "--help":
        help_prompt()
    elif os.path.isfile(argument1) and is_spew_file(argument1):
        debugprint("DEBUG: input is a file.")
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
            debugprint(f"Details: {e}")
    else:
        print(f"Error:{fullarguments} is invalid") 
except IndexError:
    raise IndexError
except Exception as e:
    debugprint(f"DEBUG: Execution halted: {e}")
    fancyexit()    
finally:
    fancyexit()
