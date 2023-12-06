"""CLI interface for pr_test project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
from calculation import Calc


def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m pr_ai_test` and `$ pr_ai_test `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    print("This will do something")
    a = 5
    b = 0
    calculator =Calc()
    print('Add:', calculator.add(a,b))
    print('Div:', calculator.div(a, b))
    
