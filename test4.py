from demo import check_task
import datetime


tasksdict = {}

with open('tasks.txt') as tasks:
    for line in tasks:
        line2 = line.replace('\n','').split(', ')
        key = int(line2[0])
        tasksdict[key] = int(line2[1])     
    print(tasksdict)


for key in tasksdict:
    eta = datetime.datetime.now() + datetime.timedelta(seconds=tasksdict[key])
    check_task.schedule((key, tasksdict[key]), eta=eta)



