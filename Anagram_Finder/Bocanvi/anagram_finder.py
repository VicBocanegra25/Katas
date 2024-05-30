"""Write a function which finds all the anagrams in a vector of words. A word x is an anagram of word y if all the
letters in x can be rearranged in a different order to form y. Your function should return a set of sets, where each
sub-set is a group of words which are anagrams of each other. Each sub-set should have at least two words. Words without
any anagrams should not be included in the result."""


def main() -> None:
    possible_anagrams: list[str] = ["veer", "lake", "item", "kale", "mite", "ever"]
    possible_anagrams_2: list[str] = ["meat", "mat", "team", "mate", "eat"]
    print(anagram_finder(possible_anagrams))
    print(anagram_finder(possible_anagrams_2))


def anagram_finder(possible_anagrams_list: list[str]) -> list[list[str]]:
    """This second version takes a list of strings. It takes the strings, sorts them, and compares them to each other
    to create a list of anagrams."""
    possible_anagram_dict: dict = {}
    # The keyword in looks for keys in the dictionary.
    for word in possible_anagrams_list:
        sorted_word = "".join(sorted(word))
        possible_anagram_dict.setdefault(sorted_word, []).append(word)

    return [anagram_group for anagram_group in possible_anagram_dict.values() if len(anagram_group) > 1]


if __name__ == "__main__":
    main()
