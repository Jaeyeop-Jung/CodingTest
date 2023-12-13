# TODO 틀림 정규표현식 부족

import re

def solution(word, pages):
    word = word.lower()
    pages = [i.lower() for i in pages]

    score = [[i] for i in range(len(pages))]
    for i in range(len(pages)):
        span = re.search('<meta property="og:url" content="[\S]*"/>', pages[i]).span()
        score[i].append(pages[i][span[0] + 33:span[1] - 3])

    for i in range(len(pages)):
        score[i].append(0)
        for w in re.findall('[a-z]+', pages[i]):
            if w == word:
                score[i][2] += 1
        score[i].append(0)
        score[i].append(0)

    for i in range(len(pages)):
        for j in re.finditer('<a href="[\S]*">', pages[i]):
            score[i][3] += 1

    for i in range(len(pages)):
        for j in re.finditer('<a href="[\S]*">', pages[i]):
            span = j.span()
            for k in range(len(pages)):
                if pages[i][span[0] + 9:span[1] - 2] in score[k]:
                    score[k][4] += score[i][2] / score[i][3]
                    break

    score.sort(key=lambda x: x[2] + x[4], reverse=True)
    return score[0][0]

# print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind 진주심연 sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
#                          "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
#                          "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
                        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))