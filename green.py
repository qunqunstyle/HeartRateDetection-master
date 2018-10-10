import datetime
import os

# from heavy import special_commit


def modify():
    file = open('C:/Users/qunqun/Documents/GitHub/HeartRateDetection-master/zero.md', 'r')
    flag = int(file.readline()) == 0
    file.close()
    file = open('C:/Users/qunqun/Documents/GitHub/HeartRateDetection-master/zero.md', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()


def commit():
    os.system('git commit -a -m change the green point')


def set_sys_time(year, month, day):
    os.system('date -s %04d%02d%02d' % (year, month, day))


def trick_commit(year, month, day):
    set_sys_time(year, month, day)
    modify()
    commit()


def daily_commit(start_date, end_date):
    for i in range((end_date - start_date).days + 1):
        cur_date = start_date + datetime.timedelta(days=i)
        trick_commit(cur_date.year, cur_date.month, cur_date.day)


if __name__ == '__main__':
    daily_commit(datetime.date(2016,2,10), datetime.date(2016,11,5))
