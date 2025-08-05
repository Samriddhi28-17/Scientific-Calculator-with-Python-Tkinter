import tkinter as tk
from tkinter import messagebox
from calculator import ScientificCal # Import the ScientificCal class from calculator.py

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator (with Matrices)")
        master.geometry("700x850") # Adjusted height for the new layout
        master.resizable(False, False) # Make window non-resizable for consistent layout
        master.configure(bg="#2E2E2E") # Dark background for the main window

        self.calculator = ScientificCal() # Create an instance of the backend calculator
        self.expression = "" # Stores the current expression entered by the user

        # --- Display Area ---
        display_frame = tk.Frame(master, bg="#1C1C1C", bd=5, relief=tk.SUNKEN)
        display_frame.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew") # Columnspan 6 now

        self.display = tk.Entry(display_frame, font=('Sans-serif', 28, 'bold'),
                                bg="#1C1C1C", fg="#FFFFFF", # Dark background, white text
                                bd=0, insertwidth=2, width=20, # No border for entry, adjusted width
                                justify='right', cursor="arrow") # Right-align text, change cursor
        self.display.pack(expand=True, fill=tk.BOTH, padx=5, pady=5) # Pack to fill the frame

        # --- Button Area ---
        buttons_frame = tk.Frame(master, bg="#2E2E2E")
        buttons_frame.grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky="nsew") # Columnspan 6 now

        # Define button styles and colors
        num_btn_style = {'bg': '#4A4A4A', 'fg': '#FFFFFF', 'font': ('Sans-serif', 16), 'relief': tk.RAISED, 'bd': 2}
        op_btn_style = {'bg': '#FF9500', 'fg': '#FFFFFF', 'font': ('Sans-serif', 16, 'bold'), 'relief': tk.RAISED, 'bd': 2}
        clear_btn_style = {'bg': '#A6A6A6', 'fg': '#000000', 'font': ('Sans-serif', 16), 'relief': tk.RAISED, 'bd': 2}
        sci_btn_style = {'bg': '#6A6A6A', 'fg': '#FFFFFF', 'font': ('Sans-serif', 14), 'relief': tk.RAISED, 'bd': 2}
        
        # --- NEW BUTTON LAYOUT ---
        # Each tuple is (button_text, style, columnspan)
        # Columnspan is 1 by default, specify if > 1
        button_layout = [
            # Row 1: Clear, Special Ops, Basic Operators
            ('mod', sci_btn_style), ('^', sci_btn_style), ('!', sci_btn_style),  ('/', op_btn_style), ('AC', clear_btn_style), ('C', clear_btn_style),
            # Row 2: Numbers, Operators, Brackets
            ('7', num_btn_style), ('8', num_btn_style), ('9', num_btn_style), ('*', op_btn_style), ('(', num_btn_style), (')', num_btn_style),
            # Row 3: Numbers, Operators, Constants
            ('4', num_btn_style), ('5', num_btn_style), ('6', num_btn_style), ('-', op_btn_style), ('pi', sci_btn_style), ('e', sci_btn_style),
            # Row 4: Numbers, Operators, Constants/Comma
            ('1', num_btn_style), ('2', num_btn_style), ('3', num_btn_style), ('+', op_btn_style), ('tau', sci_btn_style), (',', num_btn_style),
            # Row 5: Numbers, Decimal, Equals, Matrix Brackets, Transpose
            ('0', num_btn_style, 2), # Span 2 columns
            ('.', num_btn_style),
            ('=', op_btn_style),
            ('[', num_btn_style), (']', num_btn_style), ('T', sci_btn_style),
            # Row 6: Matrix Operations
            ('det(', sci_btn_style), ('inv(', sci_btn_style), ('dot(', sci_btn_style), ('sqrt(', sci_btn_style), ('cbrt(', sci_btn_style), ('abs(', sci_btn_style),
            # Row 7: Basic Trigonometric Functions
            ('sin(', sci_btn_style), ('cos(', sci_btn_style), ('tan(', sci_btn_style), ('asin(', sci_btn_style), ('acos(', sci_btn_style), ('atan(', sci_btn_style),
            # Row 8: Hyperbolic Trigonometric Functions
            ('sinh(', sci_btn_style), ('cosh(', sci_btn_style), ('tanh(', sci_btn_style), ('asinh(', sci_btn_style), ('acosh(', sci_btn_style), ('atanh(', sci_btn_style),
            # Row 9: Logarithmic Functions
            ('ln(', sci_btn_style), ('log(', sci_btn_style), ('log2(', sci_btn_style), ('exp(', sci_btn_style), ('ceil(', sci_btn_style), ('floor(', sci_btn_style),
            # Row 10: Gamma and Angle Conversions
            ('gam(', sci_btn_style), ('deg(', sci_btn_style), ('rad(', sci_btn_style)
        ]

        row_val = 0
        col_val = 0
        max_cols = 6 # Now using 6 columns as the standard

        for item in button_layout:
            button_text = item[0]
            style = item[1]
            colspan = item[2] if len(item) > 2 else 1 # Get columnspan if specified

            btn = tk.Button(buttons_frame, text=button_text, height=2,
                            command=lambda b=button_text: self.on_button_click(b), **style)
            
            # Adjust width based on columnspan for better visual consistency
            if colspan > 1:
                # Calculate width based on average button width + padding
                btn.config(width=(6 * colspan + (5 * (colspan - 1)))) # Approximate width
            else:
                btn.config(width=6) # Default width

            btn.grid(row=row_val, column=col_val, columnspan=colspan, padx=5, pady=5, sticky="nsew")
            
            col_val += colspan # Increment column by columnspan
            if col_val >= max_cols:
                col_val = 0
                row_val += 1
        
        # --- Crucial for Alignment: Configure column weights for buttons_frame ---
        for i in range(max_cols): # Iterate through all 6 columns
            buttons_frame.grid_columnconfigure(i, weight=1)
        
        # Configure row weights for responsive button sizing within the frame
        for i in range(row_val + 1): # Iterate through all created rows
            buttons_frame.grid_rowconfigure(i, weight=1)

        # Configure main window grid to expand the button frame and display frame
        self.master.grid_rowconfigure(0, weight=0) # Display row doesn't need to expand much vertically
        self.master.grid_rowconfigure(1, weight=1) # Button frame row should expand vertically
        for i in range(max_cols):
            self.master.grid_columnconfigure(i, weight=1) # Main window's columns should expand horizontally


    def on_button_click(self, button):
        """Handles the logic when a calculator button is clicked."""
        if button == 'AC': # All Clear
            self.expression = ""
            self.display.delete(0, tk.END)
        elif button == 'C': # Clear last character
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        elif button == '=': # Evaluate the expression
            result = self.calculator.evaluate_expression(self.expression)
            
            # Check if the result indicates an error from the backend
            if str(result).startswith("Error:"):
                messagebox.showerror("Calculation Error", result) # Show error in a message box
                self.expression = "" # Clear expression on error
                self.display.delete(0, tk.END) # Clear display on error
            else:
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.expression = str(result) # Keep result for chained operations
        elif button == '!': # Handle factorial separately as a postfix operator
            try:
                num = float(self.expression)
                result = self.calculator.factorial(num)
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.expression = str(result)
            except (ValueError, TypeError, IndexError) as e:
                messagebox.showerror("Factorial Error", e)
                self.expression = ""
                self.display.delete(0, tk.END)
        else:
            self.expression += button
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
