from collections import defaultdict


def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        
        for ch in word:
            count =[0] * 26
            count[ord(ch) - ord('a')] += 1
        anagrams[tuple(count)].append(word)
    return list(anagrams.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(strs)
print(result)
