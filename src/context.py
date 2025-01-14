"""
Module: Context.py
Author: Sepehr Rafiei
Description: Stores specific details regarding a translation task
"""


class Context:
    def __init__(self, original_language, to, model, temp, size, batch_size, ex_size):
        self.original_language = original_language
        self.to = to
        self.model = model
        self.temp = temp
        self.size = size
        self.batch_size = batch_size
        self.ex_size = ex_size