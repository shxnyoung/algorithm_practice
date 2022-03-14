import sys
#sys.stdin = open("input.txt", "rt")

C = int(input())
for i in range(C):

    N, s, e, k = map(int, input().split())
    lst = list(map(int, input().split()))
    sorted_lst = lst[s-1:e]
    sorted_lst.sort()
    # print("#", i+1, " ", sorted_lst[k-1], sep='')
    print("#%d %d" % (i+1, sorted_lst[k-1]))
