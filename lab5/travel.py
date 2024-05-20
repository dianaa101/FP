def init_travel(id_, start_date, end_date, destination, price):
    """
    Initialize a travel using the given parameters.
    :param id_: The id of the travel.
    :param start_date: The start date of the travel.
    :param end_date: The end date of the travel.
    :param destination: The destination of the travel.
    :param price: The price of the travel.
    :return: Travel.
    """
    return {
        "id_": id_,
        "start_date": start_date,
        "end_date": end_date,
        "destination": destination,
        "price": price,
    }


def get_travel_id(travel):
    """
    Get travel id.
    :param travel:
    :return: The id of the travel.
    """
    return travel["id_"]


def get_travel_start_date(travel):
    """

    :param travel:
    :return: The start date of the travel
    """
    return travel["start_date"]


def get_travel_end_date(travel):
    """

    :param travel:
    :return: The end date of the travel.
    """
    return travel["end_date"]


def get_travel_destination(travel):
    """

    :param travel:
    :return: The destination of the travel.
    """
    return travel["destination"]


def get_travel_price(travel):
    """

    :param travel:
    :return: The price of the travel.
    """
    return travel["price"]


def get_travel_string(travel):
    """

    :param travel:
    :return: A string representation of the travel.
    """
    s = f'Id: {get_travel_id(travel)}\n'

    start_date_str = [str(x) for x in get_travel_start_date(travel)]
    end_date_str = [str(x) for x in get_travel_end_date(travel)]

    s = s + f'Start date: { "/".join(start_date_str) }\n'
    s = s + f'End date: { "/".join(end_date_str) }\n'
    s = s + f'Destination: {get_travel_destination(travel)}\n'
    s = s + f'Price: {get_travel_price(travel)}\n'
    return s


def set_travel_start_date(travel, start_date):
    """
    Set the start date of the travel
    :param travel:
    :param start_date:
    :return:
    """
    travel["start_date"] = start_date


def set_travel_end_date(travel, end_date):
    """
    Set the end date of the travel.
    :param travel:
    :param end_date:
    :return:
    """
    travel["end_date"] = end_date


def set_travel_destination(travel, destination):
    """
    Set the destination of the travel.
    :param travel:
    :param destination:
    :return:
    """
    travel["destination"] = destination


def set_travel_price(travel, price):
    """
    Set the price of the travel.
    :param travel:
    :param price:
    :return:
    """
    travel["price"] = price

