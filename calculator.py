import math
import re
import numpy as np # Import numpy for matrix operations

class ScientificCal:
    def __init__(self):
        # Constants like pi, e, and tau
        self.constants = {
            'pi': math.pi,
            'e': math.e,
            'tau': math.tau
        }
        # Dictionary of mathematical functions
        self.functions = {
            # Trigonometric functions (radians)
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin, # Arcsin
            'acos': math.acos, # Arccos
            'atan': math.atan, # Arctan
            # Hyperbolic trigonometric functions
            'sinh': math.sinh,
            'cosh': math.cosh,
            'tanh': math.tanh,
            'asinh': math.asinh,
            'acosh': math.acosh,
            'atanh': math.atanh,
            # Roots and powers
            'sqrt': math.sqrt,
            'cbrt': lambda x: x**(1/3), # Cube root
            # Logarithmic functions
            'log': math.log10,  # Log base 10
            'ln': math.log,     # Natural logarithm (base e)
            'log2': math.log2,  # Log base 2
            'exp': math.exp,    # e to the power of x
            # Absolute value, ceiling, floor
            'abs': math.fabs,
            'ceil': math.ceil,
            'floor': math.floor,
            # Angle conversions
            'rad': math.radians, # Degrees to radians
            'deg': math.degrees, # Radians to degrees
            # Gamma function
            'gam': math.gamma,
            # Matrix-related functions from numpy
            'det': np.linalg.det,       # Determinant of a matrix
            'inv': np.linalg.inv,       # Inverse of a matrix
            'transpose': np.transpose,  # Transpose of a matrix
            'dot': np.dot               # Dot product of two arrays/matrices
        }
        # Custom operators (handled separately or converted)
        self.operators = {
            '!': self.factorial, # Factorial operator
            'mod': lambda a, b: a % b, # Modulo operator
            '^': lambda a, b: a ** b # Power operator
        }

    def factorial(self, num):
        """Calculates the factorial of a non-negative integer."""
        # Check if the number is valid for factorial calculation
        if not isinstance(num, (int, float)) or num < 0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        if num != int(num): # Check if it's a whole number
            raise ValueError("Factorial is only defined for whole numbers.")
        
        return math.factorial(int(num)) # Convert to integer before calculation
    
    def combinations(self, n, k):
        """Calculates combinations (nCk)."""
        if k > n or k < 0:
            return 0
        return math.comb(n, k) # math.comb is for combinations
    
    def permutations(self, n, k):
        """Calculates permutations (nPk)."""
        if k > n or k < 0:
            return 0
        return math.perm(n, k) # math.perm is for permutations

    def _prepare_exp(self, expression):
        """
        Prepares the expression string for evaluation by replacing constants,
        function names, and custom operators with their Python equivalents.
        """
        expression = expression.lower() # Convert to lowercase for consistent parsing

        # Replace constants (e.g., 'pi' with its numerical value)
        for const_name, value in self.constants.items():
            expression = re.sub(fr'\b{re.escape(const_name)}\b', str(value), expression)

        # Replace function names with their callable forms (e.g., 'sin(' with 'self.functions["sin"](')
        for func_name, _ in self.functions.items():
            # For numpy functions, we need to prefix them with 'np.'
            if func_name in ['det', 'inv', 'transpose', 'dot']:
                expression = re.sub(fr'\b{re.escape(func_name)}\b', f'np.{func_name}', expression)
            else:
                expression = re.sub(fr'\b{re.escape(func_name)}\b', f'self.functions["{func_name}"]', expression)
        
        # Handle the transpose operator 'T' (e.g., '[[1,2],[3,4]]T' becomes '[[1,2],[3,4]].T')
        expression = expression.replace('T', '.T')
        
        # Convert custom operators to Python's native operators
        expression = expression.replace('^', '**') # Power operator
        expression = expression.replace('mod', '%') # Modulo operator

        return expression
    
    def evaluate_expression(self, expression):
        """
        Evaluates the prepared mathematical expression using a restricted 'eval' namespace.
        This is safer than a bare eval() as it limits accessible functions.
        """
        try:
            prepared_exp = self._prepare_exp(expression)
            
            # Define a safe namespace for eval.
            # '__builtins__': None prevents access to built-in Python functions.
            # 'np': np allows access to numpy functions.
            # 'math': math allows access to math module functions.
            # 'self': self allows access to instance methods like factorial.
            safe_locals = {'np': np, 'math': math, 'self': self}
            
            result = eval(prepared_exp, {"__builtins__": None}, safe_locals)
            
            # If the result is a numpy array, convert it to a user-friendly string representation
            if isinstance(result, np.ndarray):
                return str(result).replace('\n', '') # Remove newlines for single-line display
                
            return result
        
        # Specific error handling for common mathematical and parsing issues
        except (ValueError, np.linalg.LinAlgError) as e:
            # np.linalg.LinAlgError catches errors like singular matrix for inverse
            return f"Error: Invalid value or matrix operation ({e})"
        except ZeroDivisionError:
            return "Error: Division by zero"
        except SyntaxError as e:
            return f"Error: Invalid syntax ({e})"
        except TypeError as e:
            return f"Error: Type mismatch ({e})"
        except NameError as e:
            return f"Error: Undefined name or function ({e})"
        except Exception as e:
            # Catch any other unexpected errors
            return f"Error: An unexpected error occurred ({e})"

