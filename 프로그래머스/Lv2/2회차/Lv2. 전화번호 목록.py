
def solution(phone_book):
    phone_book.sort()
    dic = {}
    dic[phone_book[0]] = 1
    length = len(phone_book[0])

    for i in range(1, len(phone_book)):
        if phone_book[i][:length] in dic:
            return False
        dic[phone_book[i]] = 1
        length = len(phone_book[i])
    return True


print(solution(["119", "97674223", "1195524421"]))