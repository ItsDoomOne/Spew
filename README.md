# Spew
Domain Specific Language for installing files and various interpreters \
Currently WIP, and only PySpew is being actively developed

## Language/Interpreter are currently 'dangerous'
What I mean is that PySpew, the current interpreter, does not have any good security features to stop execution of dangerous code. \
It's still being implemented, and down here you can find what was implemented and what is WIP. \
Shell execution is dangerous and even with commands blacklisting, it can still be used for bad stuff. Please review what code you are executing.

## PySpew Implementation list

Print ✅ \
Shell ✅ \
Mkdir ✅ \
File ✅ (partially, no inline) \
Unzip ❌ \
Alias ❌ \
Delete ✅ \
Unalias ❌ \
IF, ELSE and ELIF logic ❌ \
SpewFile 2 ❌ \
Specification for Config file ❌ \
Specification for SpewFile 2 ❌

## Some information I must add
As I speak two languages, English and Portuguese, I find myself various times writing code in both, accidentally. Maybe that is because I'm so focused I do not even acknowledge in what language I'm writing in print statements. \
Most of the time, those are commit messages and debugging texts. I'm extra careful in Specifications because its text-writing and not code-writing. 

## To-Do

1. Make a documentation file for the config file.


## Brief planning

I really, really want to ditch the python interpreter for CSpew, and thats for two good reasons:
1. PySpew being an interpreter writing in a interpreted language
2. I need to train my C skills for LerDOS. I can't just jump into a moving train without accelerating.
Bonus reason: PySpew sucks
