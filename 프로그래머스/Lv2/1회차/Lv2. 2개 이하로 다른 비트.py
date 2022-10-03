
def solution(numbers):
    result = []
    for i in numbers:
        binary = bin(i)[2:]
        if '0' not in binary:
            binary = '10' + binary[1:]
        else:
            binary = binary[-1::-1]
            for j in range(len(binary)):
                if j == 0 and binary[j] == '0':
                    binary = '1' + binary[1:]
                    break
                elif binary[j] == '0':
                    binary = binary[:j - 1] + '01' + binary[j + 1:]
                    break
            binary = binary[-1::-1]
        result.append(int('0b' + binary, 2))
    return result

print(solution([29]))