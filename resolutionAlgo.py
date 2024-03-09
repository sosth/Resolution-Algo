import re
import tkinter as tk

# Dictionary for language strings
language_strings = {
    'english': {
        'title': 'Resolution Solver',
        'enter_formula': 'Enter the formula:',
        'submit_button': 'Submit',
        'result_prefix': 'Result: ',
        'invalid_format': 'Invalid input format. Please use the format {¬P v ¬Q v R, ¬R, P, ¬T v Q, T}',
        'valid': 'F is valid',
        'invalid': 'F is invalid'
    },
    'french': {
        'title': 'Résolveur de Résolution',
        'enter_formula': 'Entrez la formule:',
        'submit_button': 'Soumettre',
        'result_prefix': 'Résultat : ',
        'invalid_format': 'Format invalide. Veuillez utiliser le format {¬P v ¬Q v R, ¬R, P, ¬T v Q, T}',
        'valid': 'F est valide',
        'invalid': 'F est invalide'
    }
}

current_language = 'english'  # Default language

def parse_formula_input(input_string):
    # Extract clauses from the input string
    clauses_match = re.findall(r'\{(.*?)\}', input_string)
    if not clauses_match:
        raise ValueError(language_strings[current_language]['invalid_format'])

    # Split each clause into literals
    clauses = [re.split(r'\s*v\s*', clause) for clause in clauses_match[0].split(',')]

    # Process literals to handle negation (¬) and convert to integers
    processed_clauses = []
    for clause in clauses:
        processed_clause = []
        for literal in clause:
            literal = literal.strip()
            if literal.startswith("¬"):
                processed_clause.append(-ord(literal[1]) + ord("A") + 1)
            else:
                processed_clause.append(ord(literal) - ord("A") + 1)
        processed_clauses.append(processed_clause)

    return processed_clauses

def resolution(F):
    def negation(F):
        if isinstance(F[0], list):
            return [[-literal for literal in clause] for clause in F]
        else:
            return [-F]

    def mettre_sous_forme_de_clauses(F):
        return [F] if isinstance(F[0], int) else F

    def chercher_clauses_resolvantes(clauses):
        result = []
        for i in range(len(clauses)):
            for j in range(i+1, len(clauses)):
                for literal_i in clauses[i]:
                    for literal_j in clauses[j]:
                        if abs(literal_i) == abs(literal_j):  # Check if the literals are complementary
                            resolvant = [literal for literal in clauses[i] if literal != literal_i] + \
                                        [literal for literal in clauses[j] if literal != literal_j]
                            if resolvant not in result:  # Check if the resolvant is already present
                                result.append(resolvant)
        return result

    neg_F = negation(F)
    clauses = mettre_sous_forme_de_clauses(neg_F)
    while True:
        new_resolvantes = chercher_clauses_resolvantes(clauses)
        if not new_resolvantes:
            return language_strings[current_language]['valid']

        # Add new resolvants to the clauses
        for resolvant in new_resolvantes:
            if all(lit not in clauses for lit in resolvant):  # Check if the resolvant is already present
                clauses.append(resolvant)

        # Check for an empty clause
        if [] in clauses:
            return language_strings[current_language]['invalid']

def run_resolution(formula_input):
    try:
        formula = parse_formula_input(formula_input)
        result = resolution(formula)
        return result
    except ValueError as e:
        return str(e)

def on_submit():
    formula_input = entry.get()
    result = run_resolution(formula_input)
    result_label.config(text=language_strings[current_language]['result_prefix'] + result)

def switch_language():
    global current_language
    if current_language == 'english':
        current_language = 'french'
    else:
        current_language = 'english'
    update_language()

def update_language():
    root.title(language_strings[current_language]['title'])
    input_label.config(text=language_strings[current_language]['enter_formula'])
    submit_button.config(text=language_strings[current_language]['submit_button'])

# Create the GUI
root = tk.Tk()
root.title(language_strings[current_language]['title'])  # Set the window title
root.geometry('400x210')  # Setting initial window size
root.configure(background='#344955')  # Set background color

# Center the window on the screen
window_width = 400
window_height = 210
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

# Create and pack the widgets
input_label = tk.Label(root, text=language_strings[current_language]['enter_formula'], background='#344955', font=('Arial', 15, 'bold'), fg='white')  # Set background color and font size
input_label.pack()

entry_frame = tk.Frame(root, bg='#344955')  # Create a frame for entry widget
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, width=30, font=('Arial', 10, 'bold'))  # Set font size
entry.pack(padx=5, pady=5, ipady=3)  # Centered and smaller width

submit_button = tk.Button(root, text=language_strings[current_language]['submit_button'], command=on_submit, background='#50727B', font=('Arial', 13, 'bold'), fg='white')  # Set background color and font size
submit_button.pack()

result_label = tk.Label(root, text="", background='#344955', font=('Arial', 12, 'bold'), fg='white')  # Set background color and font size
result_label.pack()

# Language switch button
switch_language_button = tk.Button(root, text="Switch Language", command=switch_language, background='#50727B', font=('Arial', 13, 'bold'), fg='white')  # Set background color and font size
switch_language_button.pack(pady=5)

# Copyright information
copyright_label = tk.Label(root, text="© BECHCHAA Safa", background='#344955', font=('Arial', 10, 'bold'), fg='white')  # Set background color and font size
copyright_label.pack()

root.mainloop()
