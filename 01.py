def solve(n, l, k, a, c):
    keep = 0
    i = 0
    num = 0
    while i <= n:
        if i == n:
            if l - keep >= c:
                return True
            else:
                return False
        if a[i] >= keep + c:
            if num >= k:
                return True
            keep = a[i]
            num += 1
        i += 1
        

if __name__ == '__main__':
    n, l = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split()))

    c = 1
    while True:
        if solve(n, l, k, a, c) == False:
            print(c-1)
            break
        c += 1