#arr = [5, 3, 8, 1]

#for i in range(len(arr)):
   # for j in range(len(arr) - 1 - i):
  #      if arr[j] > arr[j + 1]:
 #           arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#print(arr)

#def merge_sort(arr):
  #  if len(arr) <= 1:
 #       return arr
#
   # mid = len(arr) // 2
  #  left = merge_sort(arr[:mid])
 #   right = merge_sort(arr[mid:])
#
  #  result = []
 #   i = j = 0
#
   # while i < len(left) and j < len(right):
      #  if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# print(merge_sort([5, 3, 8, 1]))

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quick_sort(left) + middle + quick_sort(right)

# print(quick_sort([5, 3, 8, 1]))

# arr = [5, 3, 8, 1]

# for i in range(len(arr)):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]

# print(arr)