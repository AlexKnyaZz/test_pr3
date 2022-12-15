headache = None
high_temperature = None
muscle_pain = None
cough = None


def get_questions_test():
    global headache
    print("Вы чувствуете головную боль? (1 - да, 2 - нет)")
    answer = int(input())
    if answer == 1:
        headache = True
    else:
        headache = False

get_questions_test()
print(headache)