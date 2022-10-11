N = int(input())
N_list = list(map(int, input().split(' ')))
N_list.sort()

M = int(input())
find=list(map(int, input().split(' ')))


def binary(x):
    start=0
    end=N-1

    while start<=end:
        key=(start+end)//2
        if N_list[key]==x:
            return True
        if x<N_list[key]:
            end = key-1
        elif x>N_list[key]:
            start=key+1


for i in range(M):
    if binary(find[i]):
        print(1)
    else:
        print(0)
