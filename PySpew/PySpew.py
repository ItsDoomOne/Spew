import sys, os, requests, subprocess
from utils import path_setup, fancyexit
tempPath = path_setup()
print(tempPath)


try:
    fullarguments = " ".join(sys.argv[1:])
    argument1 = sys.argv[1] 
except IndexError:
        print("Usage: spew [OPTION]... <path or url>")
        print("Display information about a Spew file.")
        print()
        print("Options:")
        print("  --help     display this info and exit")   
        fancyexit() 

def execute_file(filepath):
    try:
        with open(filepath, "r") as file:
            for line in file:
                stripped = line.strip()
                if stripped.lower().startswith("print "):
                    content = stripped[6:].strip()
                    if len(content) >= 2 and content[0] == content[-1] and content[0] in ("\"", "'"):
                        print(content[1:-1])
                    else:
                        print(content)
                elif stripped.lower().startswith("shell "):
                    content = stripped[6:].strip()
                    if len(content) >= 2 and content[0] == content[-1] and content[0] in ("\"", "'"):
                        subprocess.run(content[1:-1], shell=True)
                    else:
                        subprocess.run(content, shell=True)
                elif stripped.lower().startswith("mkdir "):
                    content = stripped[6:].strip()
                    if len(content) >= 2 and content[0] == content[-1] and content[0] in ("\"", "'"):
                        os.mkdir(content[1:-1])
                    else:
                        os.mkdir(content)
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

try:           
    try:
        if argument1 == "--help":
            print("Usage: spew [OPTION]... <path or url>")
            print("Display information about a Spew file.")
            print()
            print("Options:")
            print("  --help     display this info and exit")
        elif os.path.isfile(argument1):
            if is_spew_file(argument1):
                print("input is a file.")
                execute_file(argument1)
        elif argument1.startswith("http://") or argument1.startswith("https://"):
            try:
                with open(tempPath, "wb") as file:
                    response = requests.get(argument1)
                    file.write(response.content)
                    is_spew_file(tempPath)
                    execute_file(tempPath)             
            except requests.exceptions.RequestException as e:
                print("Error: either the protocol is incorrect or the URL is unreachable")
                print(f"Details: {e}")
        else:
            print("Spew: "+fullarguments+" is invalid") 
    except IndexError:
        raise IndexError
    except Exception as e:
        print("Erro:", e)
        fancyexit()
    
finally:
    fancyexit()