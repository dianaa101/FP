from travel_with_list import *


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

    return t


def repo_find_by_id(l, id_):
    """
    Find a travel by id
    :param l: The list from which to find.
    :param id_: The id of the travel to look for.
    :return: The travel with the id.
    """
    t = None

    for x in l:
        if get_travel_id(x) == id_:
            t = x

    if t is None:
        raise ValueError('Id does not exist!!!!!!!!!')

    return t