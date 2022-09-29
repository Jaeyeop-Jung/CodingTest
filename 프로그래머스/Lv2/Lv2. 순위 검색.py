
import bisect

lang = ['cpp', 'java', 'python']
job = ['backend', 'frontend']
career = ['junior', 'senior']
food = ['chicken', 'pizza']

def solution(info, query):
    result = []

    apply = {}
    for i in lang:
        apply[i] = {}
        for j in job:
            apply[i][j] = {}
            for k in career:
                apply[i][j][k] = {}
                for f in food:
                    apply[i][j][k][f] = []
    for i in range(len(info)):
        applyLang, applyJob, applyCareer, applyFood, score = info[i].split()
        apply[applyLang][applyJob][applyCareer][applyFood].append(int(score))

    for i in lang:
        for j in job:
            for k in career:
                for f in food:
                    apply[i][j][k][f].sort()

    for i in range(len(query)):
        count = 0
        applyLang, d1, applyJob, d2, applyCareer, d3, applyFood, score = query[i].split()
        score = int(score)
        langList, jobList, careerList, foodList = [], [], [], []
        if applyLang == '-':
            langList = lang[:]
        else:
            langList.append(applyLang)
        if applyJob == '-':
            jobList = job[:]
        else:
            jobList.append(applyJob)
        if applyCareer == '-':
            careerList = career[:]
        else:
            careerList.append(applyCareer)
        if applyFood == '-':
            foodList = food[:]
        else:
            foodList.append(applyFood)
        for langg in langList:
            for jobb in jobList:
                for careerr in careerList:
                    for foodd in foodList:
                        left = bisect.bisect_left(apply[langg][jobb][careerr][foodd], score)
                        if left == 0 and len(apply[langg][jobb][careerr][foodd]) == 0:
                            continue
                        elif left == 0 and len(apply[langg][jobb][careerr][foodd]) != 0:
                            count += len([sco for sco in apply[langg][jobb][careerr][foodd] if score <= sco])
                        else:
                            count += len(apply[langg][jobb][careerr][foodd]) - left
        result.append(count)
    return result



print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
