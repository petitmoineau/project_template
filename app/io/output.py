import pandas as pd

def console_output(text):
    """prints text to the console"""
    print(text)

def write_to_file(filepath, content):
    """writes content to a file using built-in python functions"""
    with open(filepath, 'w') as file:
        file.write(content)

def write_to_file_pandas(filepath, df):
    """writes pandas DataFrame to a file using the pandas library"""
    df.to_csv(filepath, index=False)