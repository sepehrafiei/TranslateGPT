"""
Module: data_utils.py
Author: Sepehr Rafiei
Description: Provides different functions for manipulating data
"""


import json
import random
from utils.file_utils import read_jsonl


def create_output(original_text, translation, context):
    """
    Creates JSON output of texts and their translations
    :param original_text: list of original text
    :param translation: list of translated text
    :param context: information regarding the translation, ex: original language, new language
    :return: JSON format of input texts and their corresponding translation
    """
    output = []
    # Check if there are equal number of translations as to samples
    assert len(original_text)==len(translation), f"Number of original texts {len(original_text)} does not equal the number of translated texts{len(translation)}"
    for i,j in zip(original_text, translation):
        output.append({context.original_language: i, context.to: j})
    return output


def extract_language(language, n=96):
    """
    Extract n number of samples of selected language
    :param language: selected language for samples
    :param num_samples: number of samples
    :return: list of n text samples of selected language
    """

    try:
        jsonl_data = read_jsonl("../../TranslateGPT/data/esen_sample.jsonl")
        assert n <= len(jsonl_data), "Number of samples exceed sample size"
        return [data[language] for data in jsonl_data[:n]]

    except Exception as e:
        print(f"An error occurred while extracting language: {e}")


def get_batches(data, n):
    """
    Turn a list of samples into batches of size up to n
    :param data: list of text samples
    :param n: number of samples in each batch(up to)
    :return: list of b batches of up to n samples
    """
    return [[item for item in data[i:i + n]] for i in range(0, len(data), n)]


def get_example(num_samples, context):
    """
    Creates n random example input and output translations
    :param num_samples:
    :return: string showing input and expected output for translation
    """

    try:
        jsonl_data = read_jsonl("../../TranslateGPT/data/esen_sample.jsonl")
        assert num_samples <= len(jsonl_data), "Number of samples exceed sample size"
        sample = random.sample(jsonl_data, num_samples)
        original = [data[context.original_language] for data in sample]
        output = [f"{data[context.to]}" for data in sample]
        output = f"{{ \"translations\": {json.dumps(output)} }}"
        return f"Example Input: {str(original)}\nExample Output: {output}"
    except Exception as e:
        print(f"An error occurred while extracting language: {e}")

