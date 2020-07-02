# Prof Stick's Mostly Good PseudoExe Project

A project for Year 12 Software Design and Development which will allow students to explore:
* Machine code and the CPU
* Metalanguages
* Translation, specifically:
  * lexical analysis including token generation
  * syntactical analysis including parsing
  * code generation

## Motivation
Theoretical discussion of metalanguages, and lexical and syntactical analysis can be quite dry and often the importance is lost on students who wonder why the hell they are learning this stuff that they will never use. The intent here is to introduce these concepts through the challenge of developing their own executable language. It also addresses the issue that a syntactically rigid pseudocode like that specified in the [SDD Course Specifications](https://educationstandards.nsw.edu.au/wps/wcm/connect/44325629-51c6-4330-8bf8-662d5cfbe5fb/software-design-development-course-specs.pdf?MOD=AJPERES&CVID=) defeats the whole purpose of pseudocode (don't get me started)

## The Task
The initial task is to write an executable version of pseudocode that can print out the first 20 numbers in the fibonacci series. The PseudoExe files will have a suffix of *.pse and the code for the initial challenge `fibonacci.pse` is:

```
BEGIN starter

Let currentNumber = 0

Display currentNumber

Let lastNumber = currentNumber
Let currentNumber = lastNumber + 1

Display currentNumber

FOR Let counter = 0 TO 20 STEP 1
    Let tempNumber = currentNumber
    Let currentNumber = currentNumber + lastNumber
    Let lastNumber = tempNumber
    Display currentNumber
NEXT counter

END starter
```

## Resources
This project is very heavily based on Marcelo Andrade's work [Writing your own programming language and compiler with Python](https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df)

You will need to install the following:
* [LLVMLite](http://llvmlite.pydata.org) A lightweight LLVM python binding for writing JIT compilers
  
```
pip install llvmlite
```

* [RPLY](https://pypi.org/project/rply/) A pure Python parser generator

```
pip install rply
```

* [LLC](https://llvm.org/docs/CommandGuide/llc.html) An LLVM static compiler
* [GCC](https://gcc.gnu.org/) or other linking tool

### Other useful references

* [PLY documentation](https://www.dabeaz.com/ply/ply.html#ply_nn3)
* [Using RPython and RPly to build a language interpreter, part 1](https://joshsharp.com.au/blog/rpython-rply-interpreter-1.html)
* [RPLY ReadTheDocs](https://rply.readthedocs.io/en/latest/users-guide/lexers.html)

## NOTES
ATM this project is completely untested - we are on this journey together

## TODO
