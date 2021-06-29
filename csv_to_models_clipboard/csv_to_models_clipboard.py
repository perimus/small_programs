import csv
import argparse
import os
import pyperclip

from typing import List, Any

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


def convert_csv_to_models(csv_values: List[List[Any]], model_name: str) -> None:
    """
    """
    list_model_initialization_lines = []
    for model_params in csv_values:
        # Add brackets to string values.
        model_params_one_line = ", ".join([param if isfloat(param) or param == "null" else f'"{param}"' for param in model_params ])
        
        # Replace null values in the string with None.
        model_params_one_line = model_params_one_line.replace("null", "None")

        list_model_initialization_lines.append(f"{model_name.title()}({model_params_one_line}),")
    
    copy_string_to_clipboard(list_model_initialization_lines)


def copy_string_to_clipboard(list_model_initialization_lines: List[str]) -> None:
    """
    """
    clipboard_text = "\n".join(list_model_initialization_lines)
    pyperclip.copy(clipboard_text)

    print("The lines have been copied to your clipboard now.")
    


def get_csv_date(file_path: str) -> List[List[Any]]:
    """
    """
    csv_values: List[List[Any]] = []

    with open(file_path, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            csv_values.append(row)
    
    return csv_values


def main() -> None:
    print("-"*30)
    print("Script has started.")
    print("-"*30)
    print("\n")

    parser = argparse.ArgumentParser(
        description="""
                        This script will convert a csv with values in a list of model initialization lines. 
                        \n Provide the path to the csv and the name of the model as arguments.
                    """
        )
    parser.add_argument("file_path", help="The path to the csv file.")
    parser.add_argument("model_name", help="The name of the model that needs to be initialized.")
    args = parser.parse_args()

    try:
        csv_values = get_csv_date(args.file_path)
        convert_csv_to_models(csv_values, args.model_name)
    except Exception as e:
        print(e)
    finally:
        print("\n")
        print("-"*30)
        print("Script has ended.")
        print("-"*30)


if __name__ == "__main__":
    main()
