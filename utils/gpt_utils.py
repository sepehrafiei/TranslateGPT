"""
Module: gpt_utils.py
Author: Sepehr Rafiei
Description: functions to interact with gpt and formatting its output
"""


import os
import openai
from dotenv import load_dotenv
import json


# Load API key
load_dotenv()
openai.api_key = os.getenv("GPT_API_KEY")


def get_translation(p, model, temp=0.3):
    """
    Call gpt API
    :param p: prompt class
    :param model: model to use
    :param temp: temperature to use
    :return: string output of gpt content
    """
    prompt = p.selected_prompt
    sys_prompt = f"You are a professional {p.original_language}-to-{p.to} translator."
    try:
        response = openai.ChatCompletion.create(
            model = model,
            messages = [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens = 500,
            temperature = temp
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Error generating summary with GPT: {e}")
        return "Error generating summary."


def gpt_output_to_array(gpt_output):
    """
    Convert gpt output string to list of translated strings
    :param gpt_output: gpt output string
    :return: list of translated strings
    """
    try:
        response_json = json.loads(gpt_output)
        return response_json["translations"]
    except KeyError:
        try:
            return response_json["translation"]
        except KeyError:
            raise KeyError("The response JSON does not contain 'translations' or 'translation' keys.")