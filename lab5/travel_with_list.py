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


def set_travel_start_date(travel, start_date):
    travel[1] = start_date


def set_travel_end_date(travel, end_date):
    travel[2] = end_date


def set_travel_destination(travel, destination):
    travel[3] = destination


def set_travel_price(travel, price):
    travel[4] = price


