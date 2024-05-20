#
# Utils
#

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

#
# Travel
#


def init_travel(id_, start_date, end_date, destination, price):
    """
    Initialize a travel using the given parameters.
    :param id_:
    :param start_date:
    :param end_date:
    :param destination:
    :param price:
    :return:
    """
    return [id_, start_date, end_date, destination, price]


def get_travel_id(travel):
    """
    Get travel id.
    :param travel:
    :return:
    """
    return travel[0]


def get_travel_start_date(travel):
    return travel[1]


def get_travel_end_date(travel):
    return travel[2]


def get_travel_destination(travel):
    return travel[3]


def get_travel_price(travel):
    return travel[4]


def get_travel_string(travel):
    s = f'Id: {get_travel_id(travel)}\n'

    start_date_str = [str(x) for x in get_travel_start_date(travel)]
    end_date_str = [str(x) for x in get_travel_end_date(travel)]

    s = s + f'Start date: { "/".join(start_date_str) }\n'
    s = s + f'End date: { "/".join(end_date_str) }\n'
    s = s + f'Destination: {get_travel_destination(travel)}\n'
    s = s + f'Price: {get_travel_price(travel)}\n'
    return s


#
# Validator
#


def validate_date(d):
    """
    Validate a date.
    :param d: The date to validate.
    :raise ValueError: if the date is not a list, or if it doesn't have 3 elements
                       or if the elements are not valid days and months
    """
    if not isinstance(d, list):
        raise ValueError('Date is not list')
    if len(d) != 3:
        raise ValueError('Date has invalid number of elements')
    if d[0] < 1 or d[1] < 1 or d[1] > 12:
        raise ValueError('Invalid date')
    if d[0] > get_month_days(d[2], d[1]):
        raise ValueError('Invalid date')


def validate_start_end_date(s, e):
    """
    Validate a start and end date.
    :param s: The start date.
    :param e: The end date.
    :raise ValueError: if the start date is after the end date
    """
    if e[2] > s[2]:
        return
    if e[2] < s[2]:
        raise ValueError('End date is before start date')

    if e[1] > s[1]:
        return
    if e[1] < s[1]:
        raise ValueError('End date is before start date')

    if e[0] > s[0]:
        return
    if e[0] < s[0]:
        raise ValueError('End date is before start date')


def validate_price(p):
    """
    Validate a price.
    :param p: The price.
    :raise ValueError: if the price is not a number
    """
    if not isinstance(p, int):
        raise ValueError('Price is not a number')


def validate_destination(d):
    """
    Validate a destination.
    :param d: The destination.
    :raise ValueError: if the destination is not a string
    """
    if not isinstance(d, str):
        raise ValueError('Destination is invalid')


def validate_travel(t):
    """
    Validate a travel and its start date, end date, price and destination.
    :param t: The travel.
    :raise ValueError: if the travel is not a Travel or if the start date,
                       end date, price or destination are invalid
    """
    if not isinstance(t, list):
        raise ValueError('Travel is not of travel type')

    validate_date(get_travel_start_date(t))
    validate_date(get_travel_end_date(t))
    validate_price(get_travel_price(t))
    validate_destination(get_travel_destination(t))

#
# Repository
#


def repo_add(l, t):
    """
    Add travel to list.
    :param l: The list to add the travel to.
    :param t: The travel to be added.
    :raise ValueError: If the id already exists.
    """
    for x in l:
        if get_travel_id(x) == get_travel_id(t):
            raise ValueError('Id already exists!')

    l.append(t)


def repo_get_available_id(l):
    """
    Get the highest unused id in the list.
    :param l: The list to be iterated.
    :return: The highest unused id.
    """
    available_id = 0

    for x in l:
        available_id = max(available_id, get_travel_id(x) + 1)

    return available_id


def repo_get_list(l):
    """
    :param l: The list to copy.
    Returns a copy of the list containing all the travels.
    :return: The list containing all the travels.
    """
    return l[:]


def repo_remove_by_id(l, id_):
    """
    Removes travel by id.
    :param l: The list from which to remove.
    :param id_: The id of the travel to be removed.
    :return: The removed travel.
    :raise ValueError: If id doesn't exist.
    """
    t = None

    for x in l:
        if get_travel_id(x) == id_:
            t = x

    if t is None:
        raise ValueError('Id does not exist!!!!!!!!!')

    l.remove(t)

#
# Service
#


def service_create_travel(l, start_date, end_date, destination, price):
    """
    Create a new travel, validate it and add it to the list.

    :param l: The list to add the travel to.
    :param start_date: The start date of the new travel.
    :param end_date: The end date of the new travel.
    :param destination: The destination of the new travel.
    :param price: The price of the new travel.
    :return: The newly created travel.
    """
    id_ = repo_get_available_id(l)
    t = init_travel(id_, start_date, end_date, destination, price)
    validate_travel(t)
    repo_add(l, t)
    return t


def service_remove_travels_for_destination(l, d):
    """
    Remove travels for a given destination.
    :param l: The list to remove the travels from.
    :param d: The destination to look for.
    :return: The removed travels.
    """
    travels = repo_get_list(l)
    removed_travels = []
    for x in travels:
        if get_travel_destination(x) == d:
            id_ = get_travel_id(x)
            repo_remove_by_id(l, id_)
            removed_travels.append(x)
    return removed_travels


def service_remove_travels_with_price_bigger_than(l, p):
    """
    Remove travels for with price bigger than a given price.
    :param l: The list to remove the travels from.
    :param p: The price to look for.
    :return: The removed travels.
    """
    travels = repo_get_list(l)
    removed_travels = []
    for x in travels:
        if get_travel_price(x) > p:
            id_ = get_travel_id(x)
            repo_remove_by_id(l, id_)
            removed_travels.append(x)
    return removed_travels


def service_remove_travels_for_duration_less_than(l, d):
    """
    Remove travels for duration.
    :param l: The list to remove the travels from.
    :param d: The duration of the travel to look for.
    :return: The removed travels.
    """
    travels = repo_get_list(l)
    removed_travels = []
    for x in travels:
        start_date = get_travel_start_date(x)
        end_date = get_travel_end_date(x)
        if get_duration_between_dates(start_date, end_date) < d:
            id_ = get_travel_id(x)
            repo_remove_by_id(l, id_)
            removed_travels.append(x)
    return removed_travels


def service_find_travels_for_destination_and_price_less_than(l, d, p):
    """
    Find travels for a given destination and price less than a given price
    :param l: The list to find the travels in.
    :param d: The destination of the travels to look for.
    :param p: The price of the travels to look for.
    :return: The found travels.
    """
    travels = repo_get_list(l)
    found_travels = []
    for x in travels:
        if get_travel_destination(x) == d and get_travel_price(x) < p:
            found_travels.append(x)
    return found_travels


def service_find_travels_with_end_date(l, d):
    """
    Find travels with a given end date.
    :param l: The list to find the travels in.
    :param d: The end date of the travels to look for.
    :return: The found travels.
    """
    travels = repo_get_list(l)
    found_travels = []
    for x in travels:
        if get_travel_end_date(x) == d:
            found_travels.append(x)
    return found_travels


def service_find_travels_between_start_end_date(l, start_date, end_date):
    """
    Find travels between a given start date and end date.
        :param l: The list to find the travels in.
    :param start_date: The start date of the travels to look for.
    :param end_date: The end date of the travels to look for.
    :return: The found travels.
    """
    travels = repo_get_list(l)
    found_travels = []
    for x in travels:
        if get_duration_between_dates(start_date, get_travel_start_date(x)) >= 1 and \
                get_duration_between_dates(get_travel_end_date(x), end_date) >= 1:
            found_travels.append(x)
    return found_travels


def service_remove_travels_with_price_bigger_and_not_destination(l, p, d):
    """
    Remove travels for duration.
    :param l: The list to remove the travels from.
    :param p: The price of the travel to look for.
    :param d: The destination of the travel to look for.
    :return: The removed travels.
    """
    travels = repo_get_list(l)
    removed_travels = []
    for x in travels:
        if get_travel_price(x) > p and get_travel_destination(x) != d:
            id_ = get_travel_id(x)
            repo_remove_by_id(l, id_)
            removed_travels.append(x)
    return removed_travels

#
# Tests
#


def test_travel():
    t = init_travel(0, [1, 2, 2024], [12, 2, 2024], 'France', 1000)
    assert get_travel_id(t) == 0
    assert get_travel_start_date(t) == [1, 2, 2024]
    assert get_travel_end_date(t) == [12, 2, 2024]
    assert get_travel_destination(t) == 'France'
    assert get_travel_price(t) == 1000


def test_validator():
    t = init_travel(0, [1, 2, 2024], [12, 2, 2024], 'France', 1000)
    validate_date([1, 2, 2024])
    validate_start_end_date([1, 2, 2024], [12, 2, 2024])
    validate_destination('France')
    validate_price(1000)
    validate_travel(t)

    try:
        validate_date([32, 3, 2023])
        assert False
    except ValueError as e:
        assert str(e) == 'Invalid date'


def test_repo():
    travels_list = []
    t = init_travel(0, [1, 2, 2024], [12, 2, 2024], 'France', 1000)

    repo_add(travels_list, t)
    ts = repo_get_list(travels_list)
    assert ts[0] == t

    t2 = init_travel(1, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)
    repo_add(travels_list, t2)
    ts = repo_get_list(travels_list)
    assert ts[0] == t
    assert ts[1] == t2

    repo_remove_by_id(travels_list, get_travel_id(t2))
    ts = repo_get_list(travels_list)
    assert len(ts) == 1
    assert ts[0] == t


def test_duration_utils():
    assert get_duration_between_dates([1, 5, 2020], [1, 6, 2020]) == 32
    assert get_duration_between_dates([1, 5, 2020], [1, 5, 2020]) == 1
    assert get_duration_between_dates([1, 5, 2020], [2, 5, 2020]) == 2
    assert get_duration_between_dates([1, 1, 2020], [1, 1, 2021]) == 367
    assert get_duration_between_dates([2, 4, 2000], [1, 3, 2000]) == 0


def test_service():
    travels_list = []

    travel = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)
    assert get_travel_id(travel) == 0

    travels = repo_get_list(travels_list)
    assert travels[0] == travel
    repo_remove_by_id(travels_list, get_travel_id(travel))

    travels = repo_get_list(travels_list)
    assert len(travels) == 0


def test_service_remove_travels_with_destination():
    travels_list = []
    t1 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)
    t2 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Spain', 1000)
    t3 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)

    travels = service_remove_travels_for_destination(travels_list, "Italy")
    assert travels[0] == t1
    assert travels[1] == t3

    travels = repo_get_list(travels_list)
    assert travels[0] == t2


def test_service_remove_travels_with_price_bigger_than():
    travels_list = []
    t1 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)
    t2 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 1000)
    t3 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)

    travels = service_remove_travels_with_price_bigger_than(travels_list, 1999)
    assert travels[0] == t1
    assert travels[1] == t3

    travels = repo_get_list(travels_list)
    assert travels[0] == t2


def test_service_remove_travels_for_duration_less_than():
    travels_list = []
    t1 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)
    t2 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 1000)
    t3 = service_create_travel(travels_list, [1, 2, 2024], [15, 2, 2024], 'Italy', 2000)
    travels = service_remove_travels_for_duration_less_than(travels_list, 13)
    assert travels[0] == t1
    assert travels[1] == t2

    travels = repo_get_list(travels_list)
    assert travels[0] == t3


def test_service_find_travels_for_destination_and_price_less_than():
    travels_list = []
    t1 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Spain', 1999)
    t2 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 1999)
    t3 = service_create_travel(travels_list, [1, 2, 2024], [15, 2, 2024], 'Italy', 2000)
    travels = service_find_travels_for_destination_and_price_less_than(travels_list, 'Italy', 2000)
    assert travels[0] == t2


def test_service_find_travels_with_end_date():
    travels_list = []
    t1 = service_create_travel(travels_list, [1, 2, 2024], [11, 2, 2024], 'Spain', 1999)
    t2 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 1999)
    t3 = service_create_travel(travels_list, [1, 2, 2024], [15, 2, 2024], 'Italy', 2000)
    travels = service_find_travels_with_end_date(travels_list, [12, 2, 2024])
    assert travels[0] == t2


def test_service_find_travels_between_start_and_end_date():
    travels_list = []
    t1 = service_create_travel(travels_list, [1, 2, 2024], [11, 2, 2024], 'Spain', 1999)
    t2 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 1999)
    t3 = service_create_travel(travels_list, [1, 2, 2024], [15, 2, 2024], 'Italy', 2000)
    travels = service_find_travels_between_start_end_date(travels_list, [31, 1, 2024], [11, 2, 2024])
    assert travels[0] == t1


def test_service_remove_travels_with_price_bigger_and_not_destination():
    travels_list = []
    t1 = service_create_travel(travels_list, [1, 2, 2024], [11, 2, 2024], 'Spain', 3000)
    t2 = service_create_travel(travels_list, [1, 2, 2024], [12, 2, 2024], 'Spain', 2000)
    t3 = service_create_travel(travels_list, [1, 2, 2024], [15, 2, 2024], 'Italy', 2000)
    travels = service_remove_travels_with_price_bigger_and_not_destination(travels_list, 2000, "Italy")
    assert len(travels) == 1
    assert travels[0] == t1


def run_tests():
    test_travel()
    test_validator()
    test_repo()
    test_service()
    test_service_remove_travels_with_destination()
    test_service_remove_travels_with_price_bigger_than()
    test_service_remove_travels_for_duration_less_than()
    test_service_find_travels_for_destination_and_price_less_than()
    test_service_find_travels_with_end_date()
    test_service_find_travels_between_start_and_end_date()
    test_service_remove_travels_with_price_bigger_and_not_destination()


#
# UI
#


def ui_read_destination():
    d = None
    while True:
        try:
            d = input("Destination: ")
            validate_destination(d)
            break
        except ValueError:
            continue
    return d


def ui_read_price():
    p = None
    while True:
        try:
            p = int(input("Price: "))
            validate_price(p)
            break
        except ValueError:
            continue
    return p


def ui_read_duration():
    d = None
    while True:
        try:
            d = int(input("Duration: "))
            break
        except ValueError:
            continue
    return d


def ui_read_date():
    date = None

    while True:
        try:
            print("Date:")
            day = int(input("Day: "))
            month = int(input("Month: "))
            year = int(input("Year: "))
            date = [day, month, year]
            validate_date(date)
            break
        except ValueError:
            continue
    return date


def ui_read_start_end_date():
    start_date = None
    end_date = None

    while True:
        try:
            print("Start date:")
            day = int(input("Day: "))
            month = int(input("Month: "))
            year = int(input("Year: "))
            start_date = [day, month, year]
            validate_date(start_date)
            break
        except ValueError:
            continue

    while True:
        try:
            print("End date:")
            day = int(input("Day: "))
            month = int(input("Month: "))
            year = int(input("Year: "))
            end_date = [day, month, year]
            validate_date(end_date)
            validate_start_end_date(start_date, end_date)
            break
        except ValueError:
            continue

    return start_date, end_date


def ui_add_travel(travels_list):
    start_date, end_date = ui_read_start_end_date()

    p = ui_read_price()

    d = ui_read_destination()

    t = service_create_travel(travels_list, start_date, end_date, d, p)
    print('Added')
    print(get_travel_string(t))


def ui_print_travels(travels_list):
    for t in travels_list:
        print(get_travel_string(t))


def ui_remove_travel(travels_list):
    id_ = None
    while True:
        try:
            id_ = int(input('Id: '))
            break
        except ValueError:
            continue
    t = repo_remove_by_id(travels_list, id_)
    print('Removed')
    print(get_travel_string(t))


def ui_remove_travels_for_destination(travels_list):
    d = ui_read_destination()
    removed_travels = service_remove_travels_for_destination(travels_list, d)
    print('Removed')
    ui_print_travels(removed_travels)


def ui_remove_travels_with_price_bigger_than(travels_list):
    p = ui_read_price()
    removed_travels = service_remove_travels_with_price_bigger_than(travels_list, p)
    print('Removed')
    ui_print_travels(removed_travels)


def ui_remove_travels_for_duration_less_than(travels_list):
    d = ui_read_duration()
    removed_travels = service_remove_travels_for_duration_less_than(travels_list, d)
    print('Removed')
    ui_print_travels(removed_travels)


def ui_print_travels_with_destination_and_price(travels_list):
    p = ui_read_price()
    d = ui_read_destination()
    found_travels = service_find_travels_for_destination_and_price_less_than(travels_list, d, p)
    print('Found')
    ui_print_travels(found_travels)


def ui_print_travels_with_end_date(travels_list):
    d = ui_read_date()
    found_travels = service_find_travels_with_end_date(travels_list, d)
    print('Found')
    ui_print_travels(found_travels)


def ui_print_travels_between_start_end_date(travels_list):
    start_date, end_date = ui_read_start_end_date()
    found_travels = service_find_travels_between_start_end_date(travels_list, start_date, end_date)
    print('Found')
    ui_print_travels(found_travels)


def ui_remove_travels_with_price_bigger_and_not_destination(travels_list):
    p = ui_read_price()
    d = ui_read_destination()
    removed_travels = service_remove_travels_with_price_bigger_and_not_destination(travels_list, p, d)
    print('Removed')
    ui_print_travels(removed_travels)


def ui_run():
    travels_list = []

    while True:
        print('1. Add travel')
        print('2. Show travels')
        print('3. Remove travel')
        print('4. Remove travels for destination')
        print('5. Remove travels for price bigger')
        print('6. Remove travels for lower duration')
        print('7. Print travels with a destination and price lower')
        print('8. Print travels with end date')
        print('9. Print travels between start date and end date')
        print('10. Remove travels with price bigger but not destination')
        print('11. Exit')
        o = input('o: ')
        if o == '1':
            ui_add_travel(travels_list)
        if o == '2':
            travels = repo_get_list(travels_list)
            ui_print_travels(travels)
        if o == '3':
            ui_remove_travel(travels_list)
        if o == '4':
            ui_remove_travels_for_destination(travels_list)
        if o == '5':
            ui_remove_travels_with_price_bigger_than(travels_list)
        if o == '6':
            ui_remove_travels_for_duration_less_than(travels_list)
        if o == '7':
            ui_print_travels_with_destination_and_price(travels_list)
        if o == '8':
            ui_print_travels_with_end_date(travels_list)
        if o == '9':
            ui_print_travels_between_start_end_date(travels_list)
        if o == '10':
            ui_remove_travels_with_price_bigger_and_not_destination(travels_list)
        elif o == '11':
            break


run_tests()
ui_run()
