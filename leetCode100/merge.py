# 题目：合并区间
# 以数组intervals表示若干个区间的集合，其中单个区间为
# intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
# 输入：intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# 输出：[[1, 6], [8, 10], [15, 18]]
#
# 输入：intervals = [[1, 4], [4, 5]]
# 输出：[[1, 5]]
# 解释：区间[1, 4]和[4, 5]可被视为重叠区间。
def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1],interval[1])
    return merged
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))