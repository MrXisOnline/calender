import datetime


def check_leap_year(year):
    if year % 4 == 0:
        return True


def weekday_counter_forward(cur_year):
    ref_year = 1970
    r = cur_year - ref_year
    weekday_num = 0
    for i in range(1, r + 1):
        if check_leap_year(ref_year + i - 1):
            weekday_num += 2
        else:
            weekday_num += 1
    return weekday_num


def give_weekday_forward(week_num):
    week_days = ["m", "tu", "w", "th", "f", "s", "su"]
    ref_week_days = 3
    cur_week_day = week_days[ref_week_days]
    for j in range(week_num):
        if ref_week_days == 6:
            ref_week_days = 0
            cur_week_day = week_days[ref_week_days]
        else:
            ref_week_days += 1
            cur_week_day = week_days[ref_week_days]
    return cur_week_day


def weekday_counter_backward(cur_year):
    ref_year = 1970
    r = ref_year - cur_year
    weekday_num = 0
    for i in range(1, r + 1):
        if check_leap_year(ref_year - i):
            weekday_num += 2
        else:
            weekday_num += 1
    return weekday_num


def give_weekday_backward(week_num):
    week_days = ["m", "tu", "w", "th", "f", "s", "su"]
    ref_week_days = 3
    cur_week_day = week_days[ref_week_days]
    for j in range(week_num):
        if ref_week_days == 0:
            ref_week_days = 6
            cur_week_day = week_days[ref_week_days]
        else:
            ref_week_days -= 1
            cur_week_day = week_days[ref_week_days]
    return cur_week_day


def check_ref(year):
    if year > 1970:
        return True
    else:
        return False


def give_weekday_index(weekday):
    week_days = ["m", "tu", "w", "th", "f", "s", "su"]
    for i in range(len(week_days)):
        if week_days[i] == weekday:
            return i


def give_no_of_days(day, month, year):
    month_data = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    total_days = 0
    if check_leap_year(year):
        month_data[2] = 29
        for i in month_data.keys():
            if i < month:
                total_days = total_days + month_data[i]
        total_days = total_days + day
        return total_days
    else:
        for i in month_data.keys():
            if i < month:
                total_days = total_days + month_data[i]
        total_days = total_days + day
        return total_days


def give_weekday_of_days(date):
    year = date.year
    month = date.month
    day = date.day
    week_days = ["m", "tu", "w", "th", "f", "s", "su"]
    if check_ref(year):
        index = give_weekday_index(give_weekday_forward((weekday_counter_forward(year)))) - 1
        days_to_go = give_no_of_days(day, month, year)
        cur_weekday = week_days[index]
        for i in range(days_to_go):
            if index == 6:
                index = 0
                cur_weekday = week_days[index]
            else:
                index += 1
                cur_weekday = week_days[index]
        return cur_weekday
    else:
        index = give_weekday_index(give_weekday_backward((weekday_counter_backward(year)))) - 1
        days_to_go = give_no_of_days(day, month, year)
        cur_weekday = week_days[index]
        for i in range(days_to_go):
            if index == 6:
                index = 0
                cur_weekday = week_days[index]
            else:
                index += 1
                cur_weekday = week_days[index]
        return cur_weekday


def check_day_digits_give(day):
    d = str(day)
    if len(d) == 2:
        return d
    elif len(d) == 1:
        return "0" + d


def give_year_data(year):
    month_data = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if check_leap_year(year):
        month_data[2] = 29
        return month_data
    else:
        return month_data


def format_month(d):
    week_days = ["m ", "tu", "w ", "th", "f ", "s ", "su"]
    space = "".rjust(3, " ")
    for weekday in week_days:
        print(weekday + space, end="")
    print()
    for week in d.keys():
        for day in d[week]:
            print(day + space, end="")
        print()


def show_year(date):
    year = date.year
    month_name_data = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
                       7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    month_day_data = give_year_data(year)
    print(str(year).center(50, "*"))
    if check_ref(year):
        index = give_weekday_index(give_weekday_forward((weekday_counter_forward(year))))
        for month in month_day_data.keys():
            week = 1
            month_structure = {1: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               2: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               3: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               4: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               5: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               6: ["  ", "  ", "  ", "  ", "  ", "  ", "  "]
                               }
            month_name = month_name_data[month]
            print(month_name + "\n")
            for day in range(1, month_day_data[month] + 1):
                if index == 6:
                    month_structure[week][index] = check_day_digits_give(day)
                    # print(month_name,day)
                    index = 0
                    week += 1
                else:
                    month_structure[week][index] = check_day_digits_give(day)
                    index += 1
            format_month(month_structure)
    else:
        index = give_weekday_index(give_weekday_backward((weekday_counter_backward(year)))) - 1
        for month in month_day_data.keys():
            week = 1
            month_structure = {1: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               2: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               3: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               4: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               5: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                               6: ["  ", "  ", "  ", "  ", "  ", "  ", "  "]
                               }
            month_name = month_name_data[month]
            print(month_name + "\n")
            for day in range(1, month_day_data[month] + 1):
                if index == 6:
                    month_structure[week][index] = check_day_digits_give(day)
                    index = 0
                    week += 1
                else:
                    month_structure[week][index] = check_day_digits_give(day)
                    index += 1
            format_month(month_structure)


def show_month(date):
    month = date.month
    year = date.year
    month_name_data = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
                       7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    month_day_data = give_year_data(year)
    pp_str = month_name_data[month] + " of " + str(year)
    print(pp_str.center(50, "*"))
    dt_1 = datetime.datetime(year, month, 1)
    index = give_weekday_index(give_weekday_of_days(dt_1))
    week = 1
    month_structure = {1: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                       2: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                       3: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                       4: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                       5: ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
                       6: ["  ", "  ", "  ", "  ", "  ", "  ", "  "]
                       }
    for day in range(1, month_day_data[month] + 1):
        if index == 6:
            month_structure[week][index] = check_day_digits_give(day)
            # print(month_name,day)
            index = 0
            week += 1
        else:
            month_structure[week][index] = check_day_digits_give(day)
            index += 1
    format_month(month_structure)


def give_weekday_name(weekday):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week_days = ["m", "tu", "w", "th", "f", "s", "su"]
    index = 0
    for w_days in range(len(week_days)):
        if weekday == week_days[w_days]:
            index = w_days
            break
    return weekdays[index]


def show_day(date):
    year = date.year
    month = date.month
    day = date.day
    weekday = give_weekday_of_days(date)
    print("Date".center(10, "*"))
    print(day, month, year, sep="/", end="")
    print(" - " + give_weekday_name(weekday))


def add_days(date, day):
    dt_obj = datetime.timedelta(days=day)
    dt_last = date + dt_obj
    year = dt_last.year
    month = dt_last.month
    day = dt_last.day
    return year, month, day


def day_greet(day):
    print("*".center(10, "*"))
    print(day, "Days Are Added")
    print("*".center(10, "*"))
