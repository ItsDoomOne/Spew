# Spew Language/Spewfiles specification document
## Version 0.1.1, 2026-01-17

## Introduction
Spewfiles are basically plaintext files which contain instructions for the Spew interpreter to execute, such as creating directories, creating files via inline text, creating binaries using base64, downloading files from the internet and unziping files. Spewfiles are executed by Spew interpreters, such as PySpew, CSpew, or Spew.NET. They are the base for the Spew project as a whole.
Alias are used as standard bash aliases, although not connected, so a Spew alias won't show up in shell, but a shell alias can be used if implemented correctly. The correct way to use aliases is by using $ALIASNAME, which cannot contain spaces, punctuation or any non-alfanumerical character.

## Available commands and syntax

### MKDIR 
MKDIR is a command prominent in Operating Systems, with every major OS having it in some form. It is used to create directories, and Spew has it as well. The syntax is as follows:

MKDIR <path> <alias>

Where <path> is the path to the directory to create, and <alias> is the optional alias to use for the directory throughout the file's execution.

### FILE
FILE is a command used to create files via inline text, base64 or a URL. The syntax is as follows:

FILE <path> <type> <content> <alias>

Where <path> is the path to the file to create, <type> is inline, b64 or URL, <content> is the URL, inline text or base64 to use as the file's content, and <alias> is the optional alias to use for the file throughout the file's execution. FILE can also be used for multiline inline text, by using brackets as follows:

FILE <path> <type> {
    <content line 1>
    <content line 2>
    ...
} <alias>

### SHELL
SHELL is a command used to execute shell commands and files. It must use the shell specified by the configuration file for the Spew interpreter. Shells include PowerShell, pwsh (Powershell Core), cmd and bash. The syntax is as follows

SHELL <command> <extra>

Where <command> is the command or the file to be ran, and <extra> are the extra arguments to pass to the shell. Extra arguments are optional. Both <command> and <extra> can be aliases defined by other commands, such as FILE.

### UNZIP
UNZIP is a command used to unzip zip files or tarballs. The syntax is as follows:

UNZIP <file> <destination> <alias>

Where <file> is the path to the file to unzip, <destination> is the path to the directory to unzip the file to, and <alias> is the optional alias for the destination directory.

### ALIAS
ALIAS is a command used to create aliases for directories and files. The syntax is as follows:

ALIAS <alias> <path>

Where <alias> is the alias to create, and <path> is the path to the directory or file to alias.

### DELETE
DELETE is a command used to delete directories and files. It shouldn't delete the root in UNIX-like systems or %WinDir% in Windows NT as the Intepreter should prevent that (PySpew does that by default).The syntax is as follows:

DELETE <path>

Where <path> is the path to the file or directory to delete.

### DELALIAS
DELALIAS is a command used to delete aliases for directories and files. The syntax is as follows:

DELALIAS <alias>

Where <alias> is the alias to delete. Note that it will not delete the files or directories associated with the alias, but only the reference to it used throughout the Spewfile.

### PRINT
PRINT is a command that simply prints text in the console. The syntax is as follows:

PRINT <text>

Where <text> is a valid string of alphanumerical characters and symbols. Possibly even emojis if the interpreter supports it.


