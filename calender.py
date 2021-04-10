import datetime
import sys
import repos


def start_calender():
    while True:
        print("Menu".center(50, "*"))
        print("1. Show Year")
        print("2. Goto Certain Date")
        print("3. Change Date")
        print("4. Add Days to Your Date")
        print("5. Show Month")
        print("6. Exit")
        print("*".center(50, "*"))
        a = int(input())
        if len(sys.argv) == 1:
            print("Hey You Forgot to give date, I Show you")
            print("python calender.py [year] [month] [day]")
            sys.exit(0)
        elif a == 6:
            sys.exit(0)
        elif a == 1:
            y = int(sys.argv[1])
            m = int(sys.argv[2])
            da = int(sys.argv[3])
            dt = datetime.datetime(y, m, da)
            repos.show_year(dt)
        elif a == 2:
            y = int(input("Enter Year : "))
            m = int(input("Enter Month : "))
            da = int(input("Enter Day : "))
            dt = datetime.datetime(y, m, da)
            repos.show_day(dt)
        elif a == 3:
            y = int(input("Enter Year : "))
            m = int(input("Enter Month : "))
            da = int(input("Enter Day : "))
            sys.argv[1] = str(y)
            sys.argv[2] = str(m)
            sys.argv[3] = str(da)
            start_calender()
        elif a == 4:
            dt = datetime.datetime(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
            day_to_work = int(input("Enter Day : "))
            y, m, da = repos.add_days(dt, day_to_work)
            sys.argv[1] = str(y)
            sys.argv[2] = str(m)
            sys.argv[3] = str(da)
            repos.day_greet(day_to_work)
            start_calender()
        elif a == 5:
            y = int(sys.argv[1])
            m = int(sys.argv[2])
            da = int(sys.argv[3])
            dt = datetime.datetime(y, m, da)
            repos.show_month(dt)
        else:
            print("Invalid Option")


start_calender()
