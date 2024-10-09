"""docstring"""
import random
import string
import requests

# pylint: disable=too-few-public-methods

class Game:
    """docstring"""
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        grid = self.grid.copy()
        if word == '':
            return False
       
        for letter in word:
            if letter in string.ascii_uppercase and letter in grid:
                grid.remove(letter)
            else:
                return False
            
        res = requests.get(f'https://dictionary.lewagon.com/{word}').json()
        return res['found']
        