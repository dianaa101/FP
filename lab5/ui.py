from service import *


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


def ui_read_id():
    id_ = None
    while True:
        try:
            id_ = int(input("ID: "))
            break
        except ValueError:
            continue
    return id_


def ui_read_month():
    m = None
    while True:
        try:
            m = int(input("Month: "))
            validate_month(m)
            break
        except ValueError:
            continue
    return m


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


def ui_add_travel(travels_list, op_list):
    start_date, end_date = ui_read_start_end_date()

    p = ui_read_price()

    d = ui_read_destination()

    t = service_create_travel(travels_list, op_list, start_date, end_date, d, p)
    print('Added')
    print(get_travel_string(t))


def ui_update_travel(travels_list, op_list):
    id_ = ui_read_id()
    start_date, end_date = ui_read_start_end_date()
    p = ui_read_price()
    d = ui_read_destination()

    try:
        t = service_update_travel(travels_list, op_list, id_, start_date, end_date, d, p)
    except:
        print('Error')
        return

    print('Updated')
    print(get_travel_string(t))


def ui_print_travels(travels_list):
    for t in travels_list:
        print(get_travel_string(t))


def ui_remove_travel(travels_list, op_list):
    id_ = None
    while True:
        try:
            id_ = int(input('Id: '))
            break
        except ValueError:
            continue
    t = service_remove_by_id(travels_list, op_list, id_)
    print('Removed')
    print(get_travel_string(t))


def ui_remove_travels_for_destination(travels_list, op_list):
    d = ui_read_destination()
    removed_travels = service_remove_travels_for_destination(travels_list, op_list, d)
    print('Removed')
    ui_print_travels(removed_travels)


def ui_remove_travels_with_price_bigger_than(travels_list, op_list):
    p = ui_read_price()
    removed_travels = service_remove_travels_with_price_bigger_than(travels_list, op_list, p)
    print('Removed')
    ui_print_travels(removed_travels)


def ui_remove_travels_for_duration_less_than(travels_list, op_list):
    d = ui_read_duration()
    removed_travels = service_remove_travels_for_duration_less_than(travels_list, op_list, d)
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


def ui_remove_travels_with_price_bigger_and_not_destination(travels_list, op_list):
    p = ui_read_price()
    d = ui_read_destination()
    removed_travels = service_remove_travels_with_price_bigger_and_not_destination(travels_list, op_list, p, d)
    print('Removed')
    ui_print_travels(removed_travels)


def ui_remove_travels_containing_month(travels_list, op_list):
    m = ui_read_month()
    removed_travels = service_remove_travels_containing_month(travels_list, op_list, m)
    print('Removed')
    ui_print_travels(removed_travels)


def ui_find_number_of_travels_with_destination(travels_list):
    d = ui_read_destination()
    found_travels = service_find_number_of_travels_with_destination(travels_list, d)
    print('Found', found_travels)


def ui_find_price_avg_of_travels_with_destination(travels_list):
    d = ui_read_destination()
    found_travels = service_find_price_avg_of_travels_with_destination(travels_list, d)
    print('Found', found_travels)


def ui_find_travels_between_dates_with_ascending_price(travels_list):
    start_date, end_date = ui_read_start_end_date()
    found_travels = service_find_travels_between_dates_with_ascending_price(travels_list, start_date, end_date)
    print('Found')
    ui_print_travels(found_travels)


def ui_run():
    travels_list = []
    op_list = []

    while True:
        print('1. Add travel')
        print('u. Update travel')
        print('z. Undo')
        print('2. Show travels')
        print('3. Remove travel')
        print('4. Remove travels for destination')
        print('5. Remove travels for price bigger')
        print('6. Remove travels for lower duration')
        print('7. Print travels with a destination and price lower')
        print('8. Print travels with end date')
        print('9. Print travels between start date and end date')
        print('10. Remove travels with price bigger but not destination')
        print('11. Remove travels containing month')
        print('12. Find number of travels for destination')
        print('13. Find price average of travels for destination')
        print('14. Find travels between dates with ascending price')
        print('15. Exit')
        o = input('o: ')
        if o == '1':
            ui_add_travel(travels_list, op_list)
        if o == 'u':
            ui_update_travel(travels_list, op_list)
        if o == 'z':
            service_undo(travels_list, op_list)
        if o == '2':
            travels = repo_get_list(travels_list)
            ui_print_travels(travels)
        if o == '3':
            ui_remove_travel(travels_list, op_list)
        if o == '4':
            ui_remove_travels_for_destination(travels_list, op_list)
        if o == '5':
            ui_remove_travels_with_price_bigger_than(travels_list, op_list)
        if o == '6':
            ui_remove_travels_for_duration_less_than(travels_list, op_list)
        if o == '7':
            ui_print_travels_with_destination_and_price(travels_list)
        if o == '8':
            ui_print_travels_with_end_date(travels_list)
        if o == '9':
            ui_print_travels_between_start_end_date(travels_list)
        if o == '10':
            ui_remove_travels_with_price_bigger_and_not_destination(travels_list, op_list)
        if o == '11':
            ui_remove_travels_containing_month(travels_list, op_list)
        if o == '12':
            ui_find_number_of_travels_with_destination(travels_list)
        if o == '13':
            ui_find_price_avg_of_travels_with_destination(travels_list)
        if o == '14':
            ui_find_travels_between_dates_with_ascending_price(travels_list)
        elif o == '15':
            break
