
data = []
for i in range(9):
    data.append(int(input()))

data.sort()

breakBool = False
result = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        for k in range(j + 1, len(data)):
            for a in range(k + 1, len(data)):
                for b in range(a + 1, len(data)):
                    for c in range(b + 1, len(data)):
                        for d in range(c + 1, len(data)):
                            if data[a] + data[b] + data[c] + data[d] + data[i] + data[j] + data[k] == 100:
                                result = [data[a],data[b],data[c],data[d],data[i],data[j],data[k]]
                                breakBool = True
                                break
                        if breakBool is True:
                            break
                    if breakBool is True:
                        break
                if breakBool is True:
                    break

            if breakBool is True:
                break

        if breakBool is True:
            break

    if breakBool is True:
        break

result.sort()
for i in result:
    print(i)