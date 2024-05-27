"""Write a function which finds all the anagrams in a vector of words. A word x is an anagram of word y if all the
letters in x can be rearranged in a different order to form y. Your function should return a set of sets, where each
sub-set is a group of words which are anagrams of each other. Each sub-set should have at least two words. Words without
any anagrams should not be included in the result."""


def main() -> None:
    possible_anagrams: list[str] = ["veer", "lake", "item", "kale", "mite", "ever"]
    anagrams: list[set] = anagram_finder(possible_anagrams)
    print(anagrams)


def anagram_finder(possible_anagrams_) -> list[set]:
    """This solution transforms the list of words and calculates its ord value. It then compares it to the current"""
    final_anagrams: list[set] = []
    while possible_anagrams_:
        anagram_list_found: set = set()
        current_word: str = possible_anagrams_.pop()
        for word in possible_anagrams_:
            if len(current_word) == len(word) and sum(map(ord, current_word)) == sum(map(ord, word)):
                anagram_list_found.add(word)
                anagram_list_found.add(current_word)
                possible_anagrams_.remove(word)
        final_anagrams.append(set(anagram_list_found))
        final_anagrams = list(filter(lambda x: len(x) > 1, final_anagrams))
    return final_anagrams


if __name__ == "__main__":
    main()
