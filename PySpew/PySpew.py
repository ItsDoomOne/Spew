import sys, requests
from utils import path_setup, fancyexit, help_prompt, debugprint, debugmenu
from execfile import printexec, shellexec, mkdirexec, removeexec, fileexec, unzipexec, aliasexec, delaliasexec
from pathlib import Path

validflags = ["disable_print","disable_shell","disable_mkdir","disable_file","disable_download","disable_unzip","disable_alias","disable_delete","print_if_command_disabled","prompt_user_for_big_downloads","big_download_size_mb","prompt_user_for_every_command","prompt_user_for_dangerous_commands","allowed_shell_commands","blacklisted_shell_commands","ignore_all_safety_measures_including_disabling_and_shell_command_blacklisting_very_dangerous","log_file_path","max_log_file_size_mb","allow_executing_of_different_os_commands","debug","unzip_backend_windows","unzip_backend_linux","unzip_backend_osx","shell_used_on_linux","shell_used_on_osx","shell_used_on_windows"]
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

def check_flags(string):
    debugprint(f"DEBUG: CFString is {string}")
    for word in string.split():
        if word.lower() in validflags:
            debugprint(f"{word} was used and is a valid flag")
        elif word.lower() == "debugmenu":
            debugmenu()

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
    check_flags(fullarguments)
except IndexError:
    help_prompt()
    fancyexit() 

debugprint("DEBUG: Execution passed the argument processing")

try:           
    if argument1 == "--help":
        help_prompt()
    elif Path(argument1).is_file() and is_spew_file(argument1):
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
