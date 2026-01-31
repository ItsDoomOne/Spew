import sys, requests
from utils import path_setup, fancyexit, help_prompt, debugprint, is_spew_file
from pathlib import Path
from config import flags, check_flags
from execfile import execute_file

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