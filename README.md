# **Scientific Calculator**

[image link]

A robust and user-friendly scientific calculator application built with Python's Tkinter for the graphical interface and NumPy for powerful numerical and matrix operations. This project aims to provide a comprehensive calculator experience, offering basic arithmetic, advanced scientific functions, and linear algebra capabilities.

## ✨ Features
* Basic Arithmetic: Perform standard operations like addition, subtraction, multiplication, and division.

* Scientific Functions:
  - Trigonometry: sin, cos, tan, asin, acos, atan (and their hyperbolic counterparts: sinh, cosh, tanh, asinh, acosh, atanh).
  - Logarithms: Natural log (ln), base-10 log (log), and base-2 log (log2).
  - Powers & Roots: Exponentiation (^), square root (sqrt), and cube root (cbrt).
  - Special Functions: Absolute value (abs), ceiling (ceil), floor (floor), Gamma function (gam), and Factorial (!).

- Mathematical Constants: Access to pi, e, and tau.

- Unit Conversions: Convert angles between degrees (deg) and radians (rad).

- Matrix Operations: Leverage NumPy for powerful linear algebra functions:
  - Determinant (det())
  - Inverse (inv())
  - Transpose (T or transpose())
  - Dot Product (dot())

- Intuitive UI: A clean, dark-themed graphical interface with distinct button colors for enhanced usability.

- Robust Error Handling: Provides clear and informative messages for invalid expressions or operations.

## 🚀 Getting Started
**For End-Users (Windows Executable)**
You don't need to install Python to run this application on Windows!
1. Download the Executable:
     - Go to the Releases section of this GitHub repository.
     - Download the calculator_gui.zip file containing the calculator_gui.exe from the latest release.
2. Extract the File:
     - Unzip the downloaded calculator_gui.zip file.
3. Run the Application:
     - Navigate to the directory where you extracted calculator_gui.exe.
     - **Double-click** on the executable.
     - The Scientific Calculator window should appear.

### Troubleshooting for Executable:
- Antivirus Warning: Your antivirus software might flag the .exe file. This is common for applications compiled with PyInstaller. If prompted, choose to "Allow" or "Run Anyway."
- Permissions: Ensure you have execution permissions in the download directory. Try moving the .exe to your Desktop or Documents folder if issues persist.

### For Developers (Running from Source)
If you want to explore, modify, or contribute to the code, follow these steps:

### Prerequisites
- Python 3.8+ is installed on your system.
- Git is installed on your system.

### Setup Instructions
1. Clone the Repository:

`git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git`
`cd YOUR_REPO_NAME # Navigate into the project directory`

(Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual GitHub username and repository name.)

Create and Activate a Virtual Environment (Recommended):

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

This isolates your project's dependencies from your global Python installation.

Install Dependencies:

pip install numpy
pip install pyinstaller # Needed if you want to re-package the executable

Run the Application:

python calculator_gui.py

⚙️ How It Works
This calculator is designed with a clear separation of concerns between its user interface and its core mathematical logic.

Architecture Overview
calculator.py (Backend): The "brain" of the calculator. It handles all mathematical computations, expression parsing, and error validation.

calculator_gui.py (Frontend): The "face" of the calculator. It provides the interactive graphical user interface (GUI) and sends user input to the backend for processing, then displays the results.

Key Components
calculator.py (Backend)
ScientificCal Class:

__init__: Initializes dictionaries for constants (e.g., pi, e) and functions (mapping mathematical function names to their callable objects from math or numpy).

_prepare_exp(expression): This crucial method pre-processes the raw input string. It performs:

Constant substitution (e.g., "pi" becomes 3.14159...).

Function mapping (e.g., "sin(" becomes self.functions["sin"]( or np.sin( for NumPy functions).

Operator conversion (e.g., ^ to ** for power, mod to % for modulo, T to .T for matrix transpose).

evaluate_expression(expression): The core evaluation engine. It uses Python's built-in eval() function, but with a strictly controlled namespace (__builtins__ set to None) to prevent arbitrary code execution and enhance security. It only allows access to explicitly defined functions and constants.

Error Handling: Comprehensive try-except blocks are implemented to catch various exceptions (e.g., ZeroDivisionError, ValueError, SyntaxError, numpy.linalg.LinAlgError for matrix issues), returning user-friendly error messages.

factorial(num): A dedicated method for factorial calculation with robust input validation (only non-negative integers).

calculator_gui.py (Frontend)
CalculatorApp Class:

__init__: Sets up the main Tkinter window, initializes the display entry widget, and creates an instance of the ScientificCal backend.

create_buttons(): Dynamically generates all calculator buttons.

Styling: Buttons are visually categorized using distinct background and foreground colors (numbers, operators, scientific functions).

Layout: Utilizes Tkinter's grid layout manager. grid_columnconfigure and grid_rowconfigure are strategically used to ensure buttons expand proportionally and maintain a clean, aligned appearance across the grid. Buttons can also span multiple columns (columnspan) for a more traditional calculator look.

on_button_click(button_text): This is the event handler for all button presses.

It appends the button's text to the self.expression string.

When the = button is pressed, it triggers the evaluate_expression method of the backend.

It handles error messages returned from the backend by displaying them in a tkinter.messagebox pop-up, providing clear user feedback without crashing the application.

Includes special logic for the ! (factorial) button to ensure proper input handling.

Packaging (PyInstaller)
The application can be packaged into a single executable file for Windows using PyInstaller. This bundles all Python scripts, dependencies (like tkinter, numpy), and the Python interpreter itself into one .exe file, allowing the application to run on machines without a Python installation.

Command: pyinstaller --onefile --windowed --icon=calculator_icon.ico calculator_gui.py

The --icon flag embeds a custom .ico file into the executable.

💡 Usage Examples
Here are some examples of expressions you can enter:

Basic: (15 + 3) * 2 / 4

Scientific: sin(rad(90)) + log(100) + e

Factorial: 5! (enter 5 then !)

Cube Root: cbrt(27)

Matrix Transpose: [[1,2],[3,4]]T

Matrix Determinant: det([[1,2],[3,4]])

Matrix Inverse: inv([[1,2],[3,4]])

Matrix Dot Product: dot([[1,2],[3,4]],[[5,6],[7,8]])

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m 'Add new feature X').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgements
Built with Python and Tkinter.

Utilizes the powerful NumPy library for numerical operations.
