from huey import SqliteHuey
from huey import crontab
import datetime


huey = SqliteHuey(filename='huey_test.db')
# huey.immediate = True


@huey.task()
def add(a, b):
    return a + b



# периодически вывываемая функция
@huey.periodic_task(crontab(minute='*/1'))
def every_one_minutes():
    # словарь ключ id задачи, значение задержка до вызова
    tasksdict = {} 
    # считаваем задачи из текстового файла в словарь 
    with open('tasks.txt') as tasks:
        for line in tasks:
            line2 = line.replace('\n','').split(', ')
            key = int(line2[0])
            tasksdict[key] = int(line2[1])     

    idtaskslistold = huey.get('test1')
    print(f'Список задач был: {idtaskslistold}')
    idtaskslist = list(tasksdict.keys())
    print(f'Список задач стал: {idtaskslist}')
    huey.put('test1', idtaskslist)

    if idtaskslistold == None:
        idtaskslistold = []
    [tasksdict.pop(key) for key in idtaskslistold]
    print(f'Эти задачи будут запланированы: {tasksdict}')

    for key in tasksdict:
        eta = datetime.datetime.now() + datetime.timedelta(seconds=tasksdict[key])
        check_task.schedule((key, tasksdict[key]), eta=eta)

    print('This task runs every one minutes')



@huey.task()
def check_task(n,t):
    print(f'Задача номер {n}, выполнена через {t} секунд')