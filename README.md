# Resolution Algorithm 
# Introduction
<p>This Python program provides a resolution solver implemented with a graphical user interface using Tkinter. The solver utilizes the resolution algorithm to determine the validity of a logical formula provided by the user.</p>
<p>The resolution algorithm is a method used in propositional logic to determine whether a given formula is logically valid. It works by attempting to derive the empty clause (a contradiction) from a set of clauses representing the negated form of the formula. If such a derivation is successful, the original formula is considered valid; otherwise, it is invalid.</p>

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

  <p>-Literal Handling: Each clause is then split into literals using the 'v' (or) as a delimiter.</p>

  <p>-Negation Handling: For each literal, the function checks if it starts with the negation symbol ¬. If it does, it negates the following literal and converts it to its corresponding integer representation using ASCII values.</p>

  <p>-Integer Representation: The function converts each literal to its integer representation by subtracting the ASCII value of 'A' and adding 1. This ensures that each literal is represented by a unique integer, making it easier to process in the resolution algorithm.</p>

  <p>-Processed Clauses: Finally, the function returns a list of processed clauses, where each clause is represented as a list of integers.</p>

  # 3-Resolution Function (resolution):
  The resolution function implements the resolution algorithm to determine the validity of the input logical formula.
  <b><i>Steps Involved:</i></b>
  <p>-Negation Conversion: The function starts by converting the input formula F into its negated form. This is done by negating each literal within each clause.</p> 
  <p>- Conversion to Clause Form: The negated formula is then converted into clause form, where each clause is represented as a list of integers.</p>
  <p>-Resolution Loop: The function enters a loop where it iteratively searches for resolvents by combining clauses until either the empty clause is derived (indicating invalidity) or no new resolvents can be found (indicating validity). 
  <p>-Searching for Resolvants: Within each iteration, the function searches for resolvants by comparing literals from different clauses and checking if they are complementary. If they are, a resolvant is formed by removing these literals from the clauses.</p>
  <p>-Adding New Resolvants: Any new resolvants that are found are added to the list of clauses, ensuring that duplicates are not added.</p>
  <p>-Empty Clause Check: At each iteration, the function checks if the empty clause [] is present within the list of clauses. If it is, the function returns "invalid," indicating that the original formula is invalid.</p>
  <p>-Validity Determination: If no new resolvants can be found and the empty clause is not present, the function returns "valid," indicating that the original formula is valid.</p>

# 4- User Friendy Interface: 
In our program, I used Tkinter to create a graphical user interface. It includes entry fields for formula input, a submit button to trigger the resolution, and a label to display the result. Additionally, there's a button to switch between English and French languages.


# Test The Algorithm

<p>1-Let's test the resolution solver with a specific example formula to observe how it determines the validity of the formula with the example formula {A v B}:</p>
The output given by the code after submitting this formula is <b>Valid</b>. To understand this result, I am going to use the truth table: 
<p><i>Truth Values of Variables:</i> We have two variables: A and B. Each variable can take on two truth values: True (T) or False (F).</p>
<p><i>Constructing the Truth Table:</i> We enumerate all possible combinations of truth values for variables A and B. There are 2^2 = 4 possible combinations.</p>
<p><i>Evaluating the Formula:</i> For each combination of truth values, we evaluate the formula {A v B}.</p>
<p><i>Determining the Result:</i> The result of the formula {A v B} depends on the truth values of A and B. The formula evaluates to True if at least one of A or B is True. Otherwise, it evaluates to False.</p>
In the truth table above: When both A and B are False, the formula evaluates to False. When A is False and B is True, or when A is True and B is False, the formula evaluates to True. When both A and B are True, the formula evaluates to True.
<table>
        <tr>
            <th>A</th>
            <th>B</th>
            <th>A v B</th>
        </tr>
        <tr>
            <td>False</td>
            <td>False</td>
            <td>False</td>
        </tr>
        <tr>
            <td>False</td>
            <td>True</td>
            <td>True</td>
        </tr>
        <tr>
            <td>True</td>
            <td>False</td>
            <td>True</td>
        </tr>
        <tr>
            <td>True</td>
            <td>True</td>
            <td>True</td>
        </tr>
    </table>
![validEx](https://github.com/sosth/Resolution-Algo/assets/91484223/94749195-17cd-4bd3-8a7e-1eab0f680920)

I also did a test with an unvalid formula {A v B, ¬B, A} wixh follows the same process:
![InvalidEx](https://github.com/sosth/Resolution-Algo/assets/91484223/600fd9d2-740f-45b3-a790-0120aa7e7e04)

# Usage 

<p>1-Clone the repository to your local machine.</p>
<p>2-Navigate to the Project Directory.</p>
<p>3-Run the Application.</p>
<p>4-Input Formula: Enter a logical formula in the input field.</p>
<p>5-Submit and Check: Click the "Submit" button to check the validity of the formula. The result will be displayed on the screen.</p>
<p>6-Switch Languages: Use the "Switch Language" button to toggle between English and French for the user interface.</p>
 







