# Number Pairs Finder Program

This program finds pairs of numbers in a list that sum to a target value. The program can take the list and the target value from a file or as command-line arguments.

## Installation

Before running the program, ensure that you have Python and the pandas library installed on your system. If you haven't installed them yet, you can follow these steps:

1. **Install Python**: If you don't have Python 3 installed, you can download it from [the official Python website](https://www.python.org/downloads/).

2. **Install pandas**: Use `pip` to install the pandas library:

## How to Run the Program

### Option 1: Execution from the Command Line

You can run the program from the command line by providing a list of comma-separated numbers and the target value as arguments. For example:


This command will search for pairs in the list [1, 5, 6, 7, 8] that sum to 7 and display the found pairs.
### run
python app.py 1,5,6,7,8 7

### Option 2: Execution with Randomly Generated Data

If you prefer not to provide arguments in the command line, you can follow these steps:

1. **Generate Data**: Run the list generator to create a `list_numbers.csv` file that contains a randomly generated list of numbers and a target value. To do this, execute the following command:
### run
python app.py 


This will generate a random list and save it in the `list_numbers.csv` file.

2. **Run the Program**: Once you have the `list_numbers.csv` file, you can execute the main program without arguments using the following command:


## Running the Number Pairs Finder Function

To execute the Number Pairs Finder function, follow these steps:

1. Make sure you have Python installed on your system. If you don't have Python installed, you can download it from the official Python website: [Download Python](https://www.python.org/downloads/).

2. Open a terminal or command prompt on your operating system.

3. Save the provided code into a Python file. You can name the file as you like, for example, "find_pairs.py."

4. Run the Python file from the terminal using the `python` command followed by the file name. For example, if the file is named "find_pairs.py," type the following and press Enter:

   ```bash
   python find_pairs.py