#!/bin/python3


# Complete the getWays function below.
def getWays(n, c):
    memo = [0 for i in range(n+1)]
    memo[0] = 1

    for coin in c:
        for m in range(coin,n+1):
            memo[m] += memo[m - coin]

    return memo[n]




if __name__ == '__main__':


    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    print(ways)


