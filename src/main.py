"""
Module: main.py
Author: Sepehr Rafiei
Description: Given a JSONL sample, translate a language to another, get BLEU score, and save translation to file
"""


from utils.data_utils import extract_language
from utils.data_utils import get_example
from utils.gpt_utils import get_translation
from utils.gpt_utils import gpt_output_to_array
from src.metrics import calculate_bleu
from src.prompts import Prompt
from utils.data_utils import get_batches
from src.context import Context
from utils.data_utils import create_output
from utils.file_utils import save_as_jsonl



def translate(context, debug=False):
    """
    Given Translate the given context
    :param context: detailed information about translation task
    :param debug: boolean whether to show debugging text
    :return: None
    """
    original = extract_language(context.original_language, context.size)
    ref = extract_language(context.to, context.size)
    batched_original = get_batches(original, context.batch_size)
    example = get_example(2, context)
    translation = []
    for batch in batched_original:
        prompt = Prompt(batch, context.original_language, context.to, example)
        translation_string = get_translation(prompt, context.model)
        translation_array = gpt_output_to_array(translation_string)
        translation.extend(translation_array)
        if debug:
            print(f"Prompt: {prompt.selected_prompt}\n\n"
                  f"{len(translation_array)} Batch Translation: {translation_string}\n")


    if debug:
        print(f"Ref Count: {len(ref)}, Translation Count: {len(translation)}")
        for i, j in zip(ref, translation):
            print(f"Reference: {i}\nTranslation: {j}\n\n")

    bleu_score = calculate_bleu(ref, translation)
    print(f"BLEU Score: {bleu_score}")
    output = create_output(original, translation, context)
    print(output)
    save_as_jsonl(output, f"{context.original_language[:2]}->{context.to[:2]}-{context.model}.jsonl")


def spanish_to_english_4o():
    """
    Translate spanish to english using gpt40
    :return: None
    """
    context = Context("spanish", "english", "gpt-4o-mini", 0.3, 96,10, 2)
    translate(context)


def spanish_to_english_3_5():
    """
    Translate spanish to english using gpt3.5
    :return: None
    """
    context = Context("spanish", "english", "gpt-3.5-turbo", 0.3, 96,10, 2)
    translate(context)


def english_to_spanish_4o():
    """
    Translate english to spanish using gpt40
    :return: None
    """
    context = Context("english", "spanish", "gpt-4o-mini", 0.3, 96,10, 2)
    translate(context)


def english_to_spanish_3_5():
    """
    Translate spanish to english using gpt3.5
    :return: None
    """
    context = Context("english", "spanish", "gpt-3.5-turbo", 0.3, 96,6, 2)
    translate(context, True)


def spanish_to_english_4o_small():
    """
    Translate spanish to english using gpt40
    :return: None
    """
    context = Context("spanish", "english", "gpt-4o-mini", 0.3, 20,10, 2)
    translate(context)

english_to_spanish_4o()



