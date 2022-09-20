
def solution(files):
    fileList = []
    for i, j in enumerate(files):
        idx = 0
        head = []
        for k in range(len(j)):
            if not j[k].isnumeric():
                head.append(j[k])
            else:
                idx = k
                break
        number = []
        for k in range(idx, len(j)):
            if j[k].isnumeric():
                number.append(j[k])
            else:
                break
        fileList.append([i, ''.join(head).lower(), int(''.join(number))])
    fileList.sort(key=lambda x:(x[1], x[2]))
    return [files[fileList[i][0]] for i in range(len(fileList))]


# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))