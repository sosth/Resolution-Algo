# Resolution Algorithm 
# Introduction
This Python program provides a resolution solver implemented with a graphical user interface using Tkinter. The solver utilizes the resolution algorithm to determine the validity of a logical formula provided by the user.
The resolution algorithm is a method used in propositional logic to determine whether a given formula is logically valid. It works by attempting to derive the empty clause (a contradiction) from a set of clauses representing the negated form of the formula. If such a derivation is successful, the original formula is considered valid; otherwise, it is invalid.
# Features
<p>-Supports both English and French languages.</p>
<p>-Validates logical formulas using the resolution method.</p>
<p>-Provides feedback on whether the formula is valid or invalid.</p>

# 1-Language Strings
The program supports both English and French languages. Language strings are defined to display messages and labels in the chosen language.

# 2-Parsing Input Function (parse_formula_input):
The parse_formula_input function is responsible for extracting clauses and literals from the input formula string. It handles negation and converts literals to integers for processing.

<b><i>Steps Involved:</i></b>
  <p>-Input String Parsing: The function starts by parsing the input string using regular expressions to extract clauses enclosed within curly braces {}.</p>

  <p>-Clause Separation: Once the clauses are extracted, the function splits them into individual clauses using the comma , as a delimiter.</p>

  <p>Literal Handling: Each clause is then split into literals using the 'v' (or) as a delimiter.</p>

  <p>Negation Handling: For each literal, the function checks if it starts with the negation symbol ¬. If it does, it negates the following literal and converts it to its corresponding integer representation using ASCII values.</p>

  <p>Integer Representation: The function converts each literal to its integer representation by subtracting the ASCII value of 'A' and adding 1. This ensures that each literal is represented by a unique integer, making it easier to process in the resolution algorithm.</p>

  <p>Processed Clauses: Finally, the function returns a list of processed clauses, where each clause is represented as a list of integers.</p>
