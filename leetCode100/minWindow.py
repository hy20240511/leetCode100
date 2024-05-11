# 题目：最小覆盖子串
# 给你一个字符串s 、一个字符串t 。返回s中涵盖t所有字符的最小子串。如果s中不存在涵盖t所有字符的子串，则返回空字符串"" 。
# 注意：对于t中重复字符，我们寻找的子字符串中该字符数量必须不少于t中该字符数量。如果s中存在这样的子串，我们保证它是唯一的答案。
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串"BANC"包含来自字符串t的'A'、'B'和'C'。
#
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串s是最小覆盖子串。
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t中两个字符'a'均应包含在s的子串中，因此没有符合条件的子字符串，返回空字符串。
import collections


def minWindow(s,t):
    need = collections.defaultdict(int)
    for c in t:
        need[c] += 1
    needCnt = len(t)
    i = 0
    res = (0,float('inf'))
    for j,c in enumerate(s):
        if need[c] > 0:
            needCnt -= 1
        need[c] -= 1
        if needCnt == 0:
            while True:
                c = s[i]
                if need[c] == 0:
                    break
                need[c] += 1
                i += 1
            if j - i < res[1] - res[0]:
                res = (i,j)

            need[s[i]] += 1
            needCnt += 1
            i += 1

    return  "" if res[1] > len(s) else s[res[0]:res[1]+1]

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s,t))
