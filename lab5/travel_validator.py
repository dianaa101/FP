from travel_with_list import *
from utils import *


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


def validate_month(m):
    """
    Validate a month.
    :param m: The month.
    :raise ValueError: if the month is invalid.
    """
    if not isinstance(m, int):
        raise ValueError('Month is not a number')
    if m < 1 or m > 12:
        raise ValueError('Invalid month')


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
