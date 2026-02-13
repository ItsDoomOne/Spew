import sys, requests
from utils import path_setup, fancyexit, help_prompt, debugprint, is_spew_file
from pathlib import Path
from config import flags, check_flags
from execfile import execute_file
# IMPORT OTHER FILES AND LIB

try:
    tempFile = (f"{path_setup()}spewfile.spew")
    argument1 = sys.argv[1]
    check_flags(" ".join(sys.argv[1:]))
    debug = flags["debug"]
    debugprint(debug, f"DEBUG: fullarguments = {" ".join(sys.argv[1:])}")
    debugprint(debug, f"DEBUG: argument1 = {argument1}")
except IndexError:
    help_prompt()
    fancyexit() 
            
debugprint(debug, "DEBUG: Execution passed defs")

try:           
    if argument1 == "--help":
        help_prompt()
    elif Path(argument1).is_file() and is_spew_file(argument1):
        debugprint(debug, "DEBUG: input is a file.")
        execute_file(argument1, flags)
    elif (argument1.startswith("http://") or argument1.startswith("https://")):
        if not (argument1.endswith(".spew") or (argument1.endswith(".spw"))):
            fancyexit(f"The URL {argument1} is not a spewfile")
        try:
            with open(tempFile, "wb") as file:
                response = requests.get(argument1)
                file.write(response.content)
            if not is_spew_file(tempFile): fancyexit(f"The URL {argument1} is not a spewfile")
            execute_file(tempFile, flags)
            fancyexit("cu")             
        except requests.exceptions.RequestException as e:
            print("Error: either the protocol is incorrect or the URL is unreachable")
            debugprint(debug, f"Details: {e}")
    else:
        print(f"Error: {argument1} is invalid") 
except IndexError:
    raise IndexError
    fancyexit()
except Exception as e:
    debugprint(debug, f"DEBUG: Execution halted: {e}")
    fancyexit()    