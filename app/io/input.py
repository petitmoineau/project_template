import pandas as pd

def console_input():
    """reads input from the console"""
    return input("Enter some text: ")

def read_from_file(filepath):
    """reads content from a file using built-in python functions"""
    with open(filepath, 'r') as file:
        content = file.read()
    return content

def read_from_file_pandas(filepath):
    """reads content from a file using the pandas library"""
    df = pd.read_csv(filepath)
    return df