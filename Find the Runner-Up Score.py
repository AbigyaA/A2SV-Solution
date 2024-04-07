if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    first=arr[0]
    for i in range(1, len(arr)):
        if arr[i] != first:
            print(arr[i])
            break
