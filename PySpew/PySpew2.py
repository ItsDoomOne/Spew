import sys, requests
from utils import path_setup, fancyexit, help_prompt, debugprint, is_spew_file, nothing
from pathlib import Path
from config import flags, check_flags
from execfile import execute_file

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
    for argument in sys.argv[1:]:
        if argument == "--help":
            help_prompt()
            fancyexit()
        elif Path(argument).is_file() and is_spew_file(argument):
            debugprint(debug, "DEBUG: input is a file.")
            execute_file(argument, flags)
            fancyexit()
        elif (argument.startswith("http://") or argument.startswith("https://")):
            if not (argument.endswith(".spew") or (argument.endswith(".spw"))):
                fancyexit(f"The URL {argument} is not a spewfile")
            try:
                with open(tempFile, "wb") as file:
                    response = requests.get(argument)
                    file.write(response.content)
                    if not is_spew_file(tempFile): fancyexit(f"The URL {argument} is not a spewfile")
                    execute_file(tempFile, flags)
                    fancyexit("cu")             
            except requests.exceptions.RequestException as e:
                print("Error: either the protocol is incorrect or the URL is unreachable")
                debugprint(debug, f"Details: {e}")
        elif "=" in argument :
            nothing()
        else:
            print(f"Error: {argument} is invalid") 
except IndexError as e:
    print(f"IndexError {e} occurred")
    fancyexit()
except Exception as e:
    debugprint(debug, f"DEBUG: Execution halted: {e}")
    fancyexit()    