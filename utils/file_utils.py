"""
Module: file_utils.py
Author: Sepehr Rafiei
Description: Reading and writing JSONL files
"""


import json
import os
import re

def read_jsonl(file_path):
    """
    Reads a JSONL file and returns a list of dictionaries.
    :param file_path: (str) Path to the JSONL file.
    :return: list: List of dictionaries representing JSON objects.
    """

    try:
        data = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                data.append(json.loads(line.strip()))
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON in file {file_path}: {e}")


def save_as_jsonl(data, file_name="output.jsonl"):
    """
    Takes in JSON format data and saves it to output directory
    :param data: JSON data
    :param file_name: name to save the file as, if one exists, adjusts name
    :return: full directory where the file is saved
    """
    # Ensure the output directory exists
    output_dir = "../output"
    os.makedirs(output_dir, exist_ok=True)

    # Sanitize file name to remove invalid characters
    file_name = re.sub(r'[<>:"/\\|?*]', '_', file_name)

    # Check if the file already exists and adjust the file name if necessary
    base_name, ext = os.path.splitext(file_name)
    counter = 1
    full_path = os.path.join(output_dir, file_name)

    while os.path.exists(full_path):
        full_path = os.path.join(output_dir, f"{base_name}_{counter}{ext}")
        counter += 1

    # Write the data to a JSONL file
    with open(full_path, "w", encoding="utf-8") as f:
        for entry in data:
            json_line = json.dumps(entry)  # Convert the dictionary to a JSON string
            f.write(json_line + "\n")  # Write the JSON string followed by a newline

    print(f"JSONL file has been saved at: {full_path}")
    return full_path


