import sys, os, requests, subprocess
from utils import path_setup, fancyexit
import config as cfg

validcommands = ["mkdir", "file", "shell", "unzip", "print", "alias", "delete", "delalias"]

tempPath = path_setup()
tempFile = (f"{tempPath}spewfile.spew")
def debugprint(text):
    if cfg.debug:
        print(text)

def shellexec(shellexec):
    if not cfg.disable_shell:
        subprocess.run(shellexec, shell=True)
    else:
        debugprint(f"Shell is disabled. Tried to run {shellexec}")
def mkdirexec(mkdirexec):
    if not cfg.disable_mkdir:
        os.mkdir(mkdirexec)
    else:
        debugprint(f"Mkdir is disabled. Tried to create {mkdirexec}")
def printexec(printexec):
    if not cfg.disable_print:
        print(printexec)
    else:
        debugprint(f"Print is disabled. Tried to print {printexec}")

def removeexec(removepath):
    if not cfg.disable_delete:
        debugprint(f"Path to be removed is {removepath}")
        if not os.path.exists(removepath):
            debugprint(f"DEBUG: Path {removepath} does not exist")
            fancyexit()
        if os.path.isfile(removepath):
            debugprint(f"Path {removepath} appears to be a file")
            os.remove(removepath)
        else:
            debugprint(f"Path {removepath} appears to be a folder")
            os.rmdir(removepath) #currently only deletes empty directories. 
    else:
        debugprint(f"Delete is disabled. Tried to delete {removepath}")

def execute_file(filepath):
    debugprint(filepath)
    try:
        with open(filepath, "r") as file:
            for line in file:
                stripped = line.strip()
                if stripped.lower().startswith("spew "):
                    content = stripped[4:].strip()
                    if len(content) >= 2 and content[0] == content[-1] and content[0] in ("\"", "'"):
                        debugprint(f"Spew file is called '{content[1:-1]}'")
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

debugprint("DEBUG: Execução passou dos DEFs")

try:
    fullarguments = " ".join(sys.argv[1:])
    argument1 = sys.argv[1] 
    debugprint(f"DEBUG: fullarguments = {fullarguments}")
    debugprint(f"DEBUG: argument1 = {argument1}")
except IndexError:
        print("Usage: spew [OPTION]... <path or url>")
        print("Display information about a Spew file.")
        print()
        print("Options:")
        print("  --help     display this info and exit")   
        fancyexit() 

debugprint("DEBUG: Execução passou do teste de argumentos")

try:           
    if argument1 == "--help":
        print("Usage: spew [OPTION]... <path or url>")
        print("Display information about a Spew file.")
        print()
        print("Options:")
        print("  --help     display this info and exit")
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
        print("Spew: "+fullarguments+" is invalid") 
except IndexError:
    raise IndexError
except Exception as e:
    debugprint(f"DEBUG: Detaalhes: {e}")
    fancyexit()
    
finally:
    fancyexit()
