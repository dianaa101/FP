from travel_with_list import *
from list_repository import *
from travel_validator import *
from utils import *


def service_add_removed_to_op_list(op_list, removed_list):
    """
    Add a removal operation to the operation list.
    :param op_list: The operation list
    :param removed_list: The removed travels list
    """
    # Add a remove entry with the string rem and the list of removed travels
    op_list.append(["rem", removed_list])


def service_create_travel(l, op_list, start_date, end_date, destination, price):
    """
    Create a new travel, validate it and add it to the list.

    :param l: The list to add the travel to.
    :param op_list: The operations list.
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
    # Add an entry with the string add and the newly added travel
    op_list.append(["add", id_])
    return t


def service_remove_travels_for_destination(l, op_list, d):
    """
    Remove travels for a given destination.
    :param l: The list to remove the travels from.
    :param op_list: The operations list.
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
    service_add_removed_to_op_list(op_list, removed_travels)
    return removed_travels


def service_remove_travels_with_price_bigger_than(l, op_list, p):
    """
    Remove travels for with price bigger than a given price.
    :param l: The list to remove the travels from.
    :param op_list: The operations list.
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
    service_add_removed_to_op_list(op_list, removed_travels)
    return removed_travels


def service_remove_travels_for_duration_less_than(l, op_list, d):
    """
    Remove travels for duration.
    :param l: The list to remove the travels from.
    :param op_list: The operations list.
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
    service_add_removed_to_op_list(op_list, removed_travels)
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


def service_remove_travels_with_price_bigger_and_not_destination(l, op_list, p, d):
    """
    Remove travels for duration.
    :param l: The list to remove the travels from.
    :param op_list: The operations list.
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
    service_add_removed_to_op_list(op_list, removed_travels)
    return removed_travels


def service_remove_travels_containing_month(l, op_list, m):
    """
    Remove travels that contains a given month
    :param l: The list to remove travels from.
    :param op_list: The operations list.
    :param m: The month that needs to be contained.
    :return: The removed travels.
    """
    travels = repo_get_list(l)
    removed_travels = []
    for x in travels:
        if contains_month_between_dates(get_travel_start_date(x), get_travel_end_date(x), m):
            id_ = get_travel_id(x)
            repo_remove_by_id(l, id_)
            removed_travels.append(x)
    service_add_removed_to_op_list(op_list, removed_travels)
    return removed_travels


def service_find_number_of_travels_with_destination(l, d):
    """
    Find the number of travels with a given destination
    :param l: The list to find the travels in.
    :param d: The destination of the travels to look for.
    :return: The number of travels with the given destination.
    """
    travels = repo_get_list(l)
    found_travels = 0
    for x in travels:
        if get_travel_destination(x) == d:
            found_travels = found_travels + 1
    return found_travels


def service_find_price_avg_of_travels_with_destination(l, d):
    """
    Find the average price of travels with a given destination
    :param l: The list to find the travels in.
    :param d: The destination of the travels to look for.
    :return: The average price of the travels with the given destination.
    """
    travels = repo_get_list(l)
    found_travels = 0
    s = 0
    for x in travels:
        if get_travel_destination(x) == d:
            found_travels = found_travels + 1
            s = s + get_travel_price(x)
    return s / found_travels


# def fn(travel):
# return get_travel_price(travel)

def service_find_travels_between_dates_with_ascending_price(l, start_date, end_date):
    """
    Find the travels between dates in ascending order of price
    :param l: The list to find the travels in.
    :param start_date: The start date of the travel.
    :param end_date: The end date of the travel.
    :return: The travels found between the given dates in ascending order of price.
    """
    travels = repo_get_list(l)
    found_travels = []
    for x in travels:
        if get_duration_between_dates(start_date, get_travel_start_date(x)) >= 1 and \
                get_duration_between_dates(get_travel_end_date(x), end_date) >= 1:
            found_travels.append(x)
    found_travels.sort(key=lambda travel: get_travel_price(travel))
    # found_travels.sort(key=fn)
    return found_travels


def service_update_travel(l, op_list, id_, start_date, end_date, destination, price):
    """
    Update travels
    :param l: The list to update the travel to.
    :param op_list: The operations list.
    :param id_: The id of the travel.
    :param start_date: The start date of the travel.
    :param end_date: The end date of the travel.
    :param destination: The destination of the travel.
    :param price: The price of the travel.
    :return: The updated travel.
    """
    validate_start_end_date(start_date, end_date)
    validate_destination(destination)
    validate_price(price)

    t = repo_find_by_id(l, id_)

    start_date_old = get_travel_start_date(t)
    end_date_old = get_travel_end_date(t)
    destination_old = get_travel_destination(t)
    price_old = get_travel_price(t)

    set_travel_start_date(t, start_date)
    set_travel_end_date(t, end_date)
    set_travel_destination(t, destination)
    set_travel_price(t, price)

    # Add an entry with the sting upd and the old properties of the travel
    op_list.append(["upd", [id_, start_date_old, end_date_old, destination_old, price_old]])

    return t


def service_remove_by_id(l, op_list, id_):
    """
    Remove travel by id
    :param l: The list to remove the travels from.
    :param op_list: The operations list.
    :param id_: The id of the travel
    :return: The removed travels
    """
    t = repo_remove_by_id(l, id_)
    service_add_removed_to_op_list(op_list, [t])
    return t


def service_undo(l, op_list):
    """
    Undo the last operation
    :param l: The travels list to apply the undo to
    :param op_list: The operation list to take the last operation from

    """
    # Take the last operation
    op = op_list[-1]

    # If it is an add operation
    # op == ["add", id_]
    if op[0] == "add":
        # Remove the travel by the id from the entry
        repo_remove_by_id(l, op[1])
    # If it is an update operation
    # op == ["upd", [id_, start_date, end_date, destination, price]]
    elif op[0] == "upd":
        # Get the id and properties from the entry
        id_ = op[1][0]

        start_date = op[1][1]
        end_date = op[1][2]
        destination = op[1][3]
        price = op[1][4]

        # Find the travel by id
        t = repo_find_by_id(l, id_)

        # Set the old properties to the travel
        set_travel_start_date(t, start_date)
        set_travel_end_date(t, end_date)
        set_travel_destination(t, destination)
        set_travel_price(t, price)
    # If it is a remove operation
    # op == ["rem", removed_list]
    elif op[0] == "rem":
        # Get the removed travels from the entry
        removed_list = op[1]

        # Iterate over all the removed travels and add them back
        # into the travels list
        for x in removed_list:
            repo_add(l, x)

    # Remove the operation that we just undo-ed
    op_list.remove(op)
