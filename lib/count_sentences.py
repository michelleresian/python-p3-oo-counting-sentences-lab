#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value = ""):
      self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value

    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        cleaned_value = self.value.replace('..', '.').replace('!!', '!').replace('??', '?')
        sentences = [sentence for sentence in re.split(r'[.!?]', cleaned_value) if sentence]
        return len(sentences)