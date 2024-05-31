from collections import defaultdict
def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagram_map[sorted_str].append(s)
    return list(anagram_map.values())
input = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(input)
print(output)
