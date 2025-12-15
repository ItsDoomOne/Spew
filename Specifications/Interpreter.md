# Spew Interpreter specification document
## Version 0.1, 2025-12-15

## Introduction
Spew is a DSL (Domain Specific Language) for installing and deploying files and directories to remote computers via Spewfiles.
Spewfiles are written in plaintext and are executed by one of the many Spew interpreters, such as PySpew, CSpew, or Spew.NET.

## Spew commands
Spew commands are the fundamental 'building blocks' of Spewfiles, used for various tasks and operations, such as creating directories, creating files via inline text, creating binaries using base64, downloading files from the internet and unziping files.

## Spew configuration
Spew configuration deeply depends on the Spew interpreter used to execute the Spewfile, but some configuration options should not be interpreter-specific, such as safety options to disable certain Spew commands, safety options to prompt the user before executing certain Spew commands, and safety options to prompt the user before deleting certain files or directories. Some useful options also include disabling the removal of the root path in Unix-Like systems, or the deletion of %WinDir% in Windows NT.

## Spew operation
Spew operation is the specification of how a Spew interpreter should execute a Spewfile. The Spew interpreter should read the Spewfile and execute the Spew commands in the order they are written, and do some other operations such as creating aliases for directories as the user requests (generally by adding an additional string after the MKDIR command). Other operations include accurately executing all the Spew commands in the Spewfile. The Spew interpreter shouldn't lack security features such as optionally disabling commands as the user desires, or prompting the user before executing certain commands.

## Spew security
The spew interpreter should be memory-safe, and should stop 3rd party software from tampering with the execution process, so that the Spewfile is executed as intended and the user is not affected. 

## Spew performance
Spew interpreters should be quite fast and efficient, and shouldn't take too much resources from the machine. It must be optimized enough so that the biggest performance bottleneck is the actual programming language behind the interpreter, and not the interpreter itself.

## Spew future work
Spew is currently in its early stages, and there are many features that could be added in the future, such as signing, encryption, compression, a better structure (currently, Spewfiles are plaintext, but it surely would be better if they were some sort of zip or tarballs with a password, a main file, and other files so that we can stop relying on base64 for binary files).

## Spew license
Spew is licensed under the GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007.

## Spew author
Spew is authored by Leonardo H. S., which goes for the username ItsDoomOne on GitHub. Spewfile, PySpew, CSpew, and Spew.NET are all open-source projects available at https://github.com/ItsDoomOne/Spew.

