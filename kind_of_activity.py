age=input('Сколько Вам лет? ')

def kind_of_activity(age):
    age=int(age)
    if age <= 6:
        print('Пора на горшок и спать')
    elif age <= 18:
        print('Неси дневник учителю!')
    elif age <= 24:
        print('Пиши курсовую, сессия на носу')
    elif age <= 65:
        print('А завтра снова на работу.')
    job=kind_of_activity(age)
    return job

job=kind_of_activity(age)  
print(job)