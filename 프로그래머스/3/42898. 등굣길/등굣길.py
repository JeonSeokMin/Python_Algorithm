def solution(m, n, puddles):

    map = []
    for _ in range(n + 1):
        map.append([0] * (m+1))

    map[1][1] = 1


    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i,j) == (1, 1):
                continue
            if not ([j, i] in puddles):
                map[i][j] = (map[i][j-1] + map[i - 1][j]) % 1000000007
        
    return (map[n][m]) % 1000000007    