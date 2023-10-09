def recoverSecret(triplets):
    ans = []
    for i in range(len(triplets)):
        for j in range(len(triplets[i])):
            if lic.count(triplets[i][j]) < 1:
                lic.append(triplets[i][j])
    ans = list(ans)
    while True:
        cnt = 0
        for i in range(len(triplets)):
            for j in range(len(triplets[i]) - 1):
                a = triplets[i][j]
                b = triplets[i][j + 1]
                index_a = ans.index(a)
                index_b = ans.index(b)
                if index_a > index_b:
                    temp = ans[index_b]
                    ans[index_b] = ans[index_a]
                    ans[index_a] = temp
                    cnt += 1
        if cnt == 0:
            return ''.join(ans)