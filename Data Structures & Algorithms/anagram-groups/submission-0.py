class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_group = {}

        for st in strs:
            key = ''.join(sorted(st))


            anagram_group[key] = anagram_group.get(key, []) + [st]

        
        return list(anagram_group.values())



