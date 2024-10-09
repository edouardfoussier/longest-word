from longest_word.game import Game
import string
from unittest.mock import patch


class TestGame:
    
    def test_game_initialization(self):
        # setup
        game = Game()
        # exercise
        grid = game.grid
        # verify
        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase
        # teardown
            
    def test_empty_word_is_invalid(self):
        # setup
        new_game = Game()
        # verify
        assert new_game.is_valid('') is False
        
    # def test_player_input(self):
    #     # setup
    #     game = Game()
    #     # exercise
    #     grid = game.grid
    #     word = input("Enter word:")
    #     # verify
    #     assert isinstance(word, str)
    #     for letter in word:
    #         assert letter in string.ascii_uppercase
    #         assert letter in grid
    #         grid.pop(letter)
    #     # teardown
    
    def test_is_valid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'
        # exercice
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is True
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched

    def test_is_invalid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'
        # exerice
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is False
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched