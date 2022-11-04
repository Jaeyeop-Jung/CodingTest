
def solution(files):
    arr = []
    for i, file in enumerate(files):
        head, number, tail = '', '', ''
        index = 0
        while index < len(file) and not file[index].isnumeric():
            # if file[index] != ' ':
            head += file[index]
            index += 1
        while index < len(file) and file[index].isnumeric():
            # if file[index] != ' ':
            number += file[index]
            index += 1
        arr.append([i, head.lower(), int(number)])

    arr.sort(key=lambda x:(x[1], x[2], x[0]))
    return [files[i] for i, _, _ in arr]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(['f5', 'F5']))
print(solution(['muzi1.txt', 'MUZI1.txt', 'muzi001.txt', 'muzi1.TXT']))