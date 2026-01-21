import sys, os, requests, subprocess
from utils import path_setup, fancyexit, help_prompt, debugprint
from execfile import printexec, shellexec, mkdirexec, removeexec

validcommands = ["mkdir", "file", "shell", "unzip", "print", "alias", "delete", "delalias"]

tempPath = path_setup()
tempFile = (f"{tempPath}spewfile.spew")

def execute_file(filepath):
    debugprint(f"DEBUG: Filepath is {filepath}")
    try:
        with open(filepath, "r") as file:
            for line in file:
                stripped = line.strip()
                if stripped.lower().startswith("spew "):
                    content = stripped[4:].strip()
                    if len(content) >= 2 and content[0] == content[-1] and content[0] in ("\"", "'"):
                        debugprint(f"DEBUG: Spew file is called '{content[1:-1]}'")
                    else:
                        debugprint(content)
                if stripped.lower().startswith("print "):
                    content = stripped[6:].strip()
                    if len(content) >= 2 and content[0] == content[-1] and content[0] in ("\"", "'"):
                        printexec(content[1:-1])
                    else:
                        printexec(content)
                elif stripped.lower().startswith("shell "):
                    content = stripped[6:].strip()
                    if len(content) >= 2 and content[0] == content[-1] and content[0] in ("\"", "'"):
                        shellexec(content[1:-1])
                    else:
                        shellexec(content)
                elif stripped.lower().startswith("mkdir "):
                    content = stripped[6:].strip()
                    if len(content) >= 2 and content[0] == content[-1] and content[0] in ("\"", "'"):
                        mkdirexec(content[1:-1])
                    else:
                        mkdirexec(content)
                elif stripped.lower().startswith("delete "):
                    content = stripped[7:].strip()
                    if len(content) >= 2 and content[0] == content[-1] and content[0] in ("\"", "'"):
                        removeexec(content[1:-1])
                    else:
                        removeexec(content)
                ## TO BE ADDED: IF LINE NOT IN [validcommands] GIVE ERROR AND HALT
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
