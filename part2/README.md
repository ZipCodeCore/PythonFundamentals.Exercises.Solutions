# Part 2

## Accompanying resources
* Slide deck: https://zipcoder.github.io/reveal-slides.data-engineering/zcw_content/python/fundamentals-part2.html

## Exercise 1

Using the Python interpreter:

* Define a function called *greet* that meets the following criteria: 
    * Takes an argument called *name*.
    * Prints a greeting using the *name* parameter.
* Invoke the *greet* function using your name as the argument.
* Invoke the *greet* function using the value "Darth Vader" as the argument.
* Invoke the *greet* function using the value "Guido van Rossum" as the argument.

## Exercise 2

Create a script called *greet.py*.

* Define a function called *greet* that meets the following criteria: 
    * Takes an argument called *name*.
    * Prints a greeting using the *name* parameter.
* Define another function called *name_input* that meets the following criteria:
    * Takes no arguments.
    * Prints a message to the screen requesting the user to provide a name.
    * Returns a string with the value equals to that of the provided name.
* Using these two functions, prompt the user for a name and print it to the screen.
* Each function must have an appropriate docstring.

## Exercise 3

Create a script called *exponentiator.py*

* Define a function named *exponentiate* with the following criteria:
    * Takes two integers as arguments.
    * Returns the value of the first integer raised to the power of the second integer.
    * Make sure the function has an appropriate docstring.
* Define a function named *raise_to_fourth_power* with the following criteria:
    * Takes one integer as an argument.
    * Calls the *exponentiate* function to raise the given paremeter to the 4th power.
    * Make sure the function has an appropriate docstring.
* Create a variable called *square*. The value assigned to this variable should be a lambda expression that utilizes the *exponentiate* function to raise a number to the power of 2.
* Create a variable called *cube*. The value assigned to this variable should be a lambda expression that utilizes the *exponentiate* function to raise a number to the power of 3.
* In the main part of your script, print the output of square(2).
* In the main part of your script, print the output of cube(3).
* In the main part of your script, print the output of raise_to_fourth_power(4).

* When executed, your script should provide the following output. 

4   
8   
16  

