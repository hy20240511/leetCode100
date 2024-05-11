# 题目：无重复字符的最长子串
# 给定一个字符串s ，请你找出其中不含有重复字符的最长子串的长度。
# 示例
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"abc"，所以其长度为3。
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是"b"，所以其长度为1
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"wke"，所以其长度为3。
# 请注意，你的答案必须是子串的长度，"pwke"是一个子序列，不是子串。

def lengthOfLongestSubstring(str):
    lookup = set()
    max_len = 0
    cur_len = 0
    left = 0
    for s in str:
        cur_len += 1
        while s in lookup:
            cur_len -= 1
            lookup.remove(str[left])
            left += 1
        lookup.add(s)
        if cur_len > max_len:
            max_len = cur_len
    return max_len

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
