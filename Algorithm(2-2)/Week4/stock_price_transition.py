# def count(stock_prices):
#     res = [0] * len(stock_prices)
#     enum = list(enumerate(stock_prices))

#     merge_sort(enum, 0, len(enum) - 1, res)
#     return res

# def merge_sort(enum, left, right, res):
#     if left >= right:
#         return

#     mid = left + (right - left) // 2
#     merge_sort(enum, left, mid, res)
#     merge_sort(enum, mid + 1, right, res)
#     merge(enum, left, mid, right, res)

# def merge(enum, left, mid, right, res):
#     i, j = left, mid + 1
#     count = 0
#     temp = []

#     while i <= mid and j <= right:
#         if enum[i][1] <= enum[j][1]:
#             temp.append(enum[i])
#             res[enum[i][0]] += count
#             i += 1
#         else:
#             temp.append(enum[j])
#             count += 1
#             j += 1
    
#     while i <= mid:
#         temp.append(enum[i])
#         res[enum[i][0]] += count
#         i += 1
    
#     while j <= right:
#         temp.append(enum[j])
#         j += 1

#     enum[left:right + 1] = temp

# # Test the function
# stock_prices = [1, 2, 3, 4, 3, 2, 1]
# print(count(stock_prices))


def count_lower_future_prices(prices):
    n = len(prices)
    result = [0] * n
    
    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if prices[j] < prices[i]:
                count += 1
        result[i] = count
    
    return result

# 예제 테스트
print(count_lower_future_prices([5, 2, 6, 1, 2, 3, 5]))  # 예상 출력: [4, 1, 4, 0, 0, 0, 0]
print(count_lower_future_prices([1, 2, 3, 4, 3, 2, 1]))  # 예상 출력: [0, 1, 2, 3, 2, 1, 0]