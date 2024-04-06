"""This file implements the functions to cipher and decipher an Alphabet Cipher, as designed by Lewis Carol.
The approach to solve this challenge is by using a dequeue that contains the letters of the alphabet.
We will then rotate the deque by the index of the letter in the alphabet + the index of the key.
"""
from icecream import ic
from collections import deque


def main():
    ic(cipher("meet me on Tuesday evening at seven", "vigilance"))
    ic(cipher("'hmkb xe bp xpmylly rxiiqto lt fgzzv'", "vigilance", True))
    ic(cipher("the package has been delivered", "snitch"))
    ic(cipher("" ,""))

def cipher(original_message: str, key: str, decipher: bool = False) -> str:
    """Return the ciphered or deciphered message of the input message using the input key to alter the original message.
    The default behavior is to cipher, but if the flag is set to True, it will decipher the message.
    :param original_message: The original message to cipher or decipher.
    :param key: The key to use to cipher or decipher the message.
    :param decipher: A flag to indicate if the message should be deciphered or not.
    """
    # Validating if the message or key are valid strings (not empty, contain letters only (English alphabet))
    if validate_inputs(original_message, key) is True:
        return "Invalid input message or key."

    # We create a deque containing the alphabet letters (lowercase).
    alphabet_deque: deque = deque(map(chr, range(97, 123)))
    # We also create a deque containing the key letters since the length of the key is unknown.
    key_deque: deque = deque(key.lower())

    # A placeholder to store the ciphered message
    ciphered_message: str = ""

    # Add a counter to keep track of the position in the original message
    counter = 0

    # Now we iterate over our original message, get the index of the letter and we add the index of the key's letter at that point.
    # We will rotate our deques, and append the letter to the ciphered message.
    while counter < len(original_message):
        # We validate if the character is a letter to decide whether we rotate the deques or not
        if original_message[counter].isalpha():
            # Get the index of the letter in the original message
            index: int = alphabet_deque.index(original_message[counter].lower())
            # Get the index of the key, then rotate the deque
            key_index: int = alphabet_deque.index(key_deque[0].lower())
            key_deque.rotate(-1)

            # If the option to decipher is set, we need to change the key index to negative
            if decipher:
                key_index = -key_index

            new_index: int = (index + key_index)
            # Now we rotate the alphabet dequeue, and get the new letter
            alphabet_deque.rotate(-new_index)
            ciphered_message += alphabet_deque[0]
            # Get the alphabet deque back to its original state
            alphabet_deque.rotate(new_index)

        else:
            ciphered_message += original_message[counter]

        # Increase the counter
        counter += 1

    return ciphered_message


def validate_inputs(original_message: str, key: str) -> bool:
    """Validate if the input message and key are valid strings.
    :param original_message: The original message to cipher or decipher.
    :param key: The key to use to cipher or decipher the message.
    """
    if not original_message or not key:
        return True

    if not key.isalpha():
        return True

    return False

if __name__ == "__main__":
    main()
