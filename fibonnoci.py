# def fibo(n, cache={}):
#     if n <= 1:
#         return n
#     elif n not in cache:
#         cache[n] = fibo(n-1) + fibo(n-2)
#         print("cache[n] = fibo(n-1)+fibo(n-2)",
#               cache[n], fibo(n-1), fibo(n-2))
#     return cache[n]


# # cache = {0: 0, 1: 1}
# print([fibo(n) for n in range(8)])


# def fibo(n):
#     if n <= 1:
#         return n
#     f_minus_2, f_minus_1 = 0, 1
#     for _ in range(1, n):
#         f = f_minus_2+f_minus_1
#         print("f = f_minus_2+f_minus_1 - ",
#               f, f_minus_2, f_minus_1)
#         f_minus_2, f_minus_1 = f_minus_1, f
#         print("f_minus_2, f_minus_1 = f_minus_1, f - ",
#               f_minus_2, f_minus_1)
#     return f_minus_1


# print(fibo(8))

# def maxSubArray(n):
#     max_sum = 0
#     for i in range(0, len(n)):
#         for j in range(1, len(n)):
#             sum = 0
#             for k in range(i, j):
#                 print("i", "j", "k", "sum")
#                 sum = sum + n[k]
#                 print(n[i], n[j], n[k], sum)

#             if max_sum < sum:
#                 max_sum = sum
#     return max_sum


# def maxSubArray_addtionalStorage(n):
#     max_sum = 0
#     for i in range(0, len(n)):
#         sum = 0
#         for j in range(i, len(n)):
#             sum = sum + n[j]
#             print("i", "j", "sum")
#             print(n[i], n[j], sum)

#             if sum > max_sum:
#                 max_sum = sum
#     return max_sum


# import itertools
# n = [904, 40, 523, 12, -335, -385, -124, 481, -31]
# n = [-1, -4, -5, 1, -22, -2]

# print(maxSubArray(n))
# print(maxSubArray_addtionalStorage(n))


# def divideandCon(n, l, r):
#     if l == r:
#         print("In if statement", n[l], "l", l, "r", r)
#         return n[l]
#     else:
#         mid = l + (r-l)//2
#         print("l", l, "r", r, "mid", mid)

#         left_sum = divideandCon(n, l, mid)
#         print("after_left_sum", l, mid)
#         right_sum = divideandCon(n, mid+1, r)
#         print("after_right_sum", mid+1, r)

#         crossing_Sum = maxCrossingSum(n, l, mid, r)
#         print("left_sum", left_sum, "right_sum",
#               right_sum, "crossing_Sum", crossing_Sum)

#     return max(left_sum, right_sum, crossing_Sum)


# def maxCrossingSum(n, l, mid, r):
#     sum = 0
#     lsum = 0
#     for i in range(l, mid):
#         sum = sum+n[i]
#         print("SUM in maxCrossingSum", sum)
#         if sum > lsum:
#             lsum = sum
#     sum = 0
#     rsum = 0
#     for i in range(mid, r):

#         sum = sum + n[i]
#         print("SUM in 2nd for loop maxCrossingSum", sum)

#         if sum > rsum:
#             rsum = sum
#     return lsum+rsum


# print(divideandCon(n, 0, len(n)-1))


# def find_max_subarray_dp(n):
#     array = [0] * len(n)
#     array[0] = n[0]
#     for i in range(1, len(n)-1):
#         if n[i] + array[i-1] > 0:
#             array[i] = n[i] + array[i-1]
#         else:
#             array[i] = n[i]
#     return array


# print(find_max_subarray_dp(n))

def combinationTargetSum(s, t):
    res = []

    def dfs(i, current, total):
        if total == t:
            res.append(current.copy())
            print("res in total = t", res)
            return
        if i >= len(s) or total > t:
            print("i >= len(s) or total > target", i)

            return

        current.append(s[i])
        dfs(i, current, total+s[i])
        print("1. i, current, total", i, current, total+s[i])
        current.pop()
        dfs(i+1, current, total)
        print("2. i, current, total", i+1, current, total)

    dfs(0, [], 0)
    return res


s = [2, 3, 6, 7]
t = 7
print(combinationTargetSum(s, t))
