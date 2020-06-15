# Prof Stick's Mostly Good PseudoExe Project

A project for Year 12 Software Design and Development which will allow students to explore:
* Machine code and the CPU
* Metalanguages
* Translation, specifically:
  * lexical analysis including token generation
  * syntactical analysis including parsing
  * code generation

## Motivation
Theoretical discussion of metalanguages, and lexical and syntactical analysis can be quite dry and often the importance is lost on students who wonder why the hell they are learning this stuff that they will never use. The intent here is to introduce these concepts through the challenge of developing their own executable language. It also addresses the issue that a syntactically rigid pseudocode like that specified in the SDD Course Specifications defeats the whole purpose of pseudocode (don't get me started)


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


## NOTES
ATM this project is completely untested - we are on this journey together