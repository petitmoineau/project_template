from app.io import input as input_module
from app.io import output as output_module

def main():
    text = input_module.console_input()
    output_module.console_output(text)
    output_module.write_to_file('data/console_output.txt', text)
    
    content = input_module.read_from_file('data/content.txt')
    output_module.write_to_file('data/read_from_file.txt', content)

    content_pandas_df = input_module.read_from_file_pandas('data/content.csv')
    output_module.write_to_file_pandas('data/read_from_file_pandas.csv', content_pandas_df)

if __name__ == "__main__":
    main()