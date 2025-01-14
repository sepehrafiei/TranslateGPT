"""
Module: prompts.py
Author: Sepehr Rafiei
Description: Stores different prompts for GPT to use
"""


class Prompt():
    def __init__(self, batch, original_language, to, example):
        self.batch = batch
        self.original_language = original_language
        self.to = to
        self.example = example

        self.prompt1 = (
                f"Translate the following text from {self.original_language} to {self.to}. "
                f"You are a professional {self.original_language}-to-{self.to} translator with expertise in producing high-quality, grammatically accurate, and contextually appropriate translations. "
                f"Your task is to provide a faithful and precise translation of the input text, preserving the meaning, tone, and style of the original. "
                f"Ensure that the number of translations in the output matches the number of inputs, and that they are provided in the same order as the input. "
                f"Return only the list of translations in the exact format: "
                "{\"translation\": [\"translation1\", \"translation2\", ...]}"
                f"Example input and output:\n"
                f"{self.example}\n\n"
                "Now, please translate the following:\n"
                f"{self.batch}"
            )

        self.prompt2 = (
                f"Translate the following text from {self.original_language} to {self.to} as literally and accurately as possible. "
                f"You are a professional translator with expertise in {self.original_language}-to-{self.to} translation. "
                "Your objective is to produce a clear, faithful translation that preserves the original meaning, tone, and sentence structure "
                "without omitting or adding extra information. Do not rephrase or paraphrase more than necessary. "
                "Be sure to retain punctuation, names, and references exactly as in the source text. "
                "Ensure that the number of translations in the output matches the number of inputs, and they appear in the same order. "
                "Return the translation in valid JSON with the following structure:\n\n"
                "{\"translation\": [\"translation1\", \"translation2\", ...]}"
                "Example input and output:\n"
                f"{example}\n\n"
                "Now, please translate the following:\n"
                f"{batch}"
        )

        self.prompt3 = (
            f"Translate the following text from {self.original_language} to {self.to}. "
            f"You are a professional {self.original_language}-to-{self.to} translator with expertise in producing high-quality, grammatically accurate, and contextually appropriate translations. "
            f"Your task is to provide a faithful and precise translation of the input text, preserving the meaning, tone, and style of the original without adding or removing conversational elements unnecessarily. "
            f"Pay special attention to:\n"
            f"- Avoiding conversational additions unless explicitly present in the original.\n"
            f"- Matching the exact meaning and tone of ambiguous or figurative terms (e.g., 'botanical').\n"
            f"- Preserving demonstrative pronouns ('this,' 'that') and context-specific words.\n"
            f"- Keeping the output in the same order as the input text.\n"
            f"Return only the list of translations in the exact format: "
            f"{{\"translation\": [\"translation1\", \"translation2\", ...]}}\n\n"
            f"Example input and output:\n"
            f"{self.example}\n\n"
            f"Now, please translate the following:\n"
            f"{self.batch}"
        )

        self.prompt4 = (
            f"Translate the following text from {self.original_language} to {self.to}. "
            f"As a professional {self.original_language}-to-{self.to} translator, your primary goal is to produce translations that are not only grammatically accurate but also preserve the original text's meaning, tone, style, and cultural nuances. "
            f"You should approach this task with the same meticulous attention to detail and expertise as a certified translator working on a professional project. "
            f"Your task is to ensure that each translation is faithful and precise, maintaining the intent and flow of the source material. "
            f"Please format your response as a JSON object in the exact format: "
            "{\"translation\": [\"translation1\", \"translation2\", ...]} "
            f"Ensure the number of translations matches the number of input sentences and retain their order. "
            f"Example input and output:\n"
            f"{self.example}\n\n"
            "Now, please translate the following:\n"
            f"{self.batch}"
        )

        self.selected_prompt = self.prompt1

