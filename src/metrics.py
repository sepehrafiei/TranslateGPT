"""
Module: metrics.py
Author: Sepehr Rafiei
Description: Provides metrics for scoring translations
"""


import sacrebleu


def calculate_bleu(candidates, references):
    """
    Calcualates BLEU score
    :param candidate: translated text
    :param references: gold-standard reference of translation
    :return:
    """
    return sacrebleu.corpus_bleu(candidates, references).score