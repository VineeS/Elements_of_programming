import collections
def find_anagrams(word_list):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for i in word_list:
        sorted_string_to_anagrams[''.join(sorted(i))].append(i)

    return sorted_string_to_anagrams
    # return [
    #     group for group in sorted_string_to_anagrams.values() if len(group) >1
    # ]

word_list = ["listen", "hello", "world", "act", "cat", "god", "dog", "money", "honey","silent"]
anagrams = find_anagrams(word_list)

for key, value in anagrams.items():
    if len(value) > 1:
        print(f"Anagrams for '{key}': {', '.join(value)}")