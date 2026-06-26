class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)  #注意与普通字典的区别

        for st in strs:
            key = "".join(sorted(st))    #sorted返回的是列表，需要转化成字符串作为key
            mp[key].append(st)
        
        return list(mp.values())		#返回list而不是value类型
