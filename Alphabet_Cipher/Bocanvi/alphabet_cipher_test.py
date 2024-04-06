"""This file is used to test the Alphabet Cipher implementation for different test cases."""
from alphabet_cipher import cipher
import pytest


# Testing valid inputs
@pytest.mark.parametrize("original_message, key, ciphered_message", [
    ("meet me on Tuesday evening at seven", "vigilance", "hmkb xe bp xpmylly rxiiqto lt fgzzv"),
    ("the package has been delivered", "snitch", "lum icjcnox jhk omxp kwyqogywq")
])
def test_valid_cipher(original_message, key, ciphered_message):
    result = cipher(original_message, key)
    assert result == ciphered_message


@pytest.mark.parametrize("ciphered_message, key, original_message", [
    ("hmkb xe bp xpmylly rxiiqto lt fgzzv", "vigilance", "meet me on tuesday evening at seven"),
    ("lum icjcnox jhk omxp kwyqogywq", "snitch", "the package has been delivered")
])
def test_valid_decipher(ciphered_message, key, original_message):
    result = cipher(ciphered_message, key, True)
    assert result == original_message


# Testing edge cases for invalid inputs
@pytest.mark.parametrize("original_message, key, expected_result", [
    ("", "vigilance", "Invalid input message or key."),  # Empty message
    ("meet me on Tuesday", "", "Invalid input message or key."),  # Empty key
    ("meet me on Tuesday", "vigil1ance", "Invalid input message or key."),  # Numbers in key
    ("meet me on Tuesday", "vigilance!", "Invalid input message or key.")   # Special char in key
])
def test_edge_cases_invalid_keys(original_message, key, expected_result):
    result = cipher(original_message, key)
    assert result == expected_result


# Testing cases where the message contains special characters and numbers (valid scenario)
@pytest.mark.parametrize("original_message, key, ciphered_message", [
    ("meet me on 4Tuesday evening at seven!", "vigilance", "hmkb xe bp 4xpmylly rxiiqto lt fgzzv!"),
    ("000the package has been delivered!", "snitch", "000lum icjcnox jhk omxp kwyqogywq!")
])
def test_special_characters_numbers(original_message, key, ciphered_message):
    result = cipher(original_message, key)
    assert result == ciphered_message