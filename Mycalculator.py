import tkinter as tk

# --- Create main window ---
root = tk.Tk()
root.title("My Calculator")
root.geometry("350x500")
root.config(bg="#222")

# --- Global variable for expression ---
expression = ""

# --- Functions ---
def add_to_expression(value):
    global expression
    expression += str(value)
    entry_var.set(expression)

def clear_expression():
    global expression
    expression = ""
    entry_var.set(expression)

def calculate_result():
    global expression
    try:
        result = str(eval(expression))
        entry_var.set(result)
        expression = result  # allow continuous calculations
    except Exception:
        entry_var.set("Error")
        expression = ""

# --- Entry display ---
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 24), justify='right',
                 bg="#333", fg="white", bd=0, relief="flat")
entry.pack(pady=20, ipadx=8, ipady=8, fill="x", padx=10)

# --- Frame for buttons ---
button_frame = tk.Frame(root, bg="#222")
button_frame.pack()

# --- Helper function to create buttons ---
def create_button(text, bg_color, fg_color, row, col, command=None, width=5):
    if not command:
        command = lambda t=text: add_to_expression(t)
    btn = tk.Button(button_frame, text=text, bg=bg_color, fg=fg_color,
                    font=('Arial', 18, 'bold'), bd=0, relief="flat", width=width, height=2,
                    command=command, activebackground="#444", activeforeground="white")
    btn.grid(row=row, column=col, padx=6, pady=6)

# --- Buttons Layout ---
create_button("7", "#2c2c54", "white", 1, 0)
create_button("8", "#2c2c54", "white", 1, 1)
create_button("9", "#2c2c54", "white", 1, 2)
create_button("/", "#ffb142", "white", 1, 3)

create_button("4", "#2c2c54", "white", 2, 0)
create_button("5", "#2c2c54", "white", 2, 1)
create_button("6", "#2c2c54", "white", 2, 2)
create_button("*", "#ffb142", "white", 2, 3)

create_button("1", "#2c2c54", "white", 3, 0)
create_button("2", "#2c2c54", "white", 3, 1)
create_button("3", "#2c2c54", "white", 3, 2)
create_button("-", "#ffb142", "white", 3, 3)

create_button("0", "#2c2c54", "white", 4, 0)
create_button(".", "#2c2c54", "white", 4, 1)
create_button("C", "#ff5252", "white", 4, 2, command=clear_expression)
create_button("+", "#ffb142", "white", 4, 3)

create_button("Calculate", "#33d9b2", "black", 5, 0, command=calculate_result, width=22)
# Span the "=" button across multiple columns
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(3, weight=1)
# Adjust "=" button position manually
button_frame.grid_slaves(row=5, column=0)[0].grid(columnspan=4)

# --- Run the GUI loop ---
root.mainloop()