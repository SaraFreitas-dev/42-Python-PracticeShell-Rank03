def group_anagrams(words: list[str]) -> list[list[str]]:
    anagram_dict: dict[str, list[str]] = {}
    res_lst: list[list[str]] = []

    for word in words:
        key = "".join(sorted(word.lower()))
        if key not in anagram_dict:
            anagram_dict[key] = [word]
        else:
            anagram_dict[key].append(word)

    for lst in anagram_dict.values():
        res_lst.append(lst)
    return res_lst


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(group_anagrams(["Listen", "silent", "enlist", "abc"]))       # [['Listen', 'silent', 'enlist'], ['abc']]
    print(group_anagrams(["abc", "def"]))                              # [['abc'], ['def']]
    print(group_anagrams(["a"]))                                       # [['a']]
    print(group_anagrams([]))                                          # []
