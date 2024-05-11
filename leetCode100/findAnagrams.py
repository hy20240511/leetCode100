# 题目：找到字符串中所有字母异位词
# 给定两个字符串s和p，找到s中所有p的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 异位词指由相同字母重排列形成的字符串（包括相同的字符串）。
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0, 6]
# 解释:起始索引等于0的子串是"cba", 它是"abc"的异位词。起始索引等于6的子串是"bac", 它是"abc"的异位词。
#
# 输入: s = "abab", p = "ab"
# 输出: [0, 1, 2]
# 解释:起始索引等于0的子串是"ab", 它是"ab"的异位词。起始索引等于1的子串是"ba", 它是"ab"的异位词。起始索引等于2的子串是"ab", 它是"ab"的异位词。

def findAnagrams(s,p):
    s_len = len(s)
    p_len = len(p)
    ans = []
    s_count = [0]*26
    p_count = [0]*26
    if s_len < p_len:
        return []
    for i in range(p_len):
        s_count[ord(s[i])-97] += 1
        p_count[ord(p[i])-97] += 1

    if s_count == p_count:
        ans.append(0)

    for i in range(s_len-p_len):
        s_count[ord(s[i])-97] -= 1
        s_count[ord(s[i+p_len])-97] += 1

        if s_count == p_count:
            ans.append(i+1)
    return ans

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s,p))
