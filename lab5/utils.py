def is_leap_year(y):
    """
    Find if the given year is a leap year or not.
    :param y: Year
    :return: Whether the given year is a leap year or not.
    """
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


def get_year_days(y):
    """
    Find the number of days in a year.
    :param y: Year
    :return: The number of days in a year.
    """
    if is_leap_year(y):
        return 366
    else:
        return 365


def get_month_days(y, m):
    """
    Find the number of days in a month.
    :param y: Year
    :param m: Month
    :return: The number of days in a month.
    """
    if m == 2:
        if is_leap_year(y):
            return 29
        else:
            return 28

    d = {
        1: 31,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    return d[m]


def get_duration_between_dates(s, e):
    """
    Get the number of days between a start date and an end date.
    :param s: Start date
    :param e: End date
    :return: The number of days between a start date and an end date.
    """
    sd, sm, sy = s
    ed, em, ey = e

    # n - number of days
    n = 0

    # iterate over all the full years following the start year and before the end year
    # 1.3.2000 -> 1.3.2002 will add all the days of the year 2001
    for y in range(sy + 1, ey):
        n = n + get_year_days(y)

    # 1.3.2000 -> 1.3.2001
    # will add months 4, 5, 6, 7, 8, 9, 10, 11, 12 from the year 2000
    # and months 1, 2 from the year 2001
    if ey > sy:
        # iterate over the full months following the start month and before the end of the year
        for m in range(sm + 1, 13):
            n = n + get_month_days(sy, m)
        # iterate over the full months since the start of the end year until the end month
        for m in range(1, em):
            n = n + get_month_days(ey, m)

    # if the end year is bigger than the start year
    # or the end year is the same as the start year
    # and the start month is before the end month
    # 1.3.2000 -> 10.4.2001 will add days 1 through 31 of month 3
    # and days 1 through 10 of month 4
    # 1.3.2000 -> 10.4.2000 will add days 1 through 31 of month 3
    # and days 1 through 10 of month 4
    if ey > sy or (ey == sy and em > sm):
        # add the number of days since the start day to the end of the month
        n = n + get_month_days(sy, sm) - sd + 1
        # add the number of days since the start of the month until the end day
        n = n + ed
    # else, if the start year is the same as the end year and the start month is
    # the same as the end month
    # that means that the start date and the end date are in the same month
    # 1.3.2000 -> 10.3.2000 will add days 1 through 10
    elif sy == ey and sm == em:
        # add the number of days between the start day and end day
        n = n + ed - sd + 1
    return n


def contains_month_between_dates(s, e, m):
    """
    Check if there is a specific month present between dates
    :param s: Start date
    :param e: End date
    :param m: Month
    :return: Whether there is a specific month
    """
    sd, sm, sy = s
    ed, em, ey = e

    if sm == m or em == m:
        return True

    if ey > sy:
        # iterate over the full months following the start month and before the end of the year
        for x in range(sm + 1, 13):
            if x == m:
                return True
        # iterate over the full months since the start of the end year until the end month
        for x in range(1, em):
            if x == m:
                return True

    if ey > sy + 1:
        return True

    return False