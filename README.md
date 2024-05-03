# what_is_name_eq_main

This repository contains examples to deepen understanding on how : if __name__ == '__main__' works in Python.

A short answer is:

# It's boilerplate code that protects users from accidentally invoking the script when they didn't intend to. 

"""

Whenever the Python interpreter reads a source file, it does two things:

- it sets a few special variables like __name__, and then

- it executes all of the code found in the file.

"""

1. # When Your Module Is the Main Program

If you are running your module (the source file) as the main program, e.g.

python bar.py 

the interpreter will assign the hard-coded string "__main__" to the __name__ variable, i.e.

# It's as if the interpreter inserts this at the top
# of your module when run as the main program.

    __name__ = "__main__"


2. # When Your Module Is Imported By Another

On the other hand, suppose some other module is the main program and it imports your module. This means there's a statement like this in the main program, or in some other module the main program imports:

# Suppose this is in some other main program.
import bar
The interpreter will search for your bar.py file (along with searching for a few other variants), and prior to executing that module, it will assign the name "bar" from the import statement to the __name__ variable, i.e.

# It's as if the interpreter inserts this at the top
# of your module when it's imported from another module.
__name__ = "bar"



--------------------------------------------------------------------------------------------------------------------------

# Loading the math module and assigns it to a variable called math. This is equivalent to replacing import math with the following (note that __import__ is a low-level function in Python that takes a string and triggers the actual import):

# Find and load a module given its string name, "math",
# then assign it to a local variable called math.
math = __import__("math")