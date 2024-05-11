# 题目：字母异位词分组
# 给你一个字符串数组，请你将字母异位词组合在一起。可以按任意顺序返回结果列表。
# 字母异位词：是由重新排列源单词的所有字母得到的一个新单词。
#
# 示例
#
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
#
# 输入: strs = [""]
# 输出: [[""]]
#
# 输入: strs = ["a"]
# 输出: [["a"]]
import collections

def groupAnagrams(strs):
    mp = collections.defaultdict(list)
    for st in strs:
        key = "".join(sorted(st))
        mp[key].append(st)
    return list(mp.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))