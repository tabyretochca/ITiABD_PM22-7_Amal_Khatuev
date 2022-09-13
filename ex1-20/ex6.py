arr = [int(input()) for i in range(int(input()))]

k, l = int(input()), int(input())
if arr.index(k) <= arr.index(l):
    print(sum(arr[arr.index(k): arr.index(l) +1]))
else:
    print(sum(arr[arr.index(l): arr.index(k) +1]))
