from travel_with_list import *
from travel_validator import *
from list_repository import *
from service import *
from utils import *


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
    op_list = []

    travel = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)
    assert get_travel_id(travel) == 0

    travels = repo_get_list(travels_list)
    assert travels[0] == travel
    repo_remove_by_id(travels_list, get_travel_id(travel))

    travels = repo_get_list(travels_list)
    assert len(travels) == 0


def test_service_remove_travels_with_destination():
    travels_list = []
    op_list = []
    t1 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)
    t2 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Spain', 1000)
    t3 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)

    travels = service_remove_travels_for_destination(travels_list, op_list, "Italy")
    assert travels[0] == t1
    assert travels[1] == t3

    travels = repo_get_list(travels_list)
    assert travels[0] == t2


def test_service_remove_travels_with_price_bigger_than():
    travels_list = []
    op_list = []
    t1 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)
    t2 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 1000)
    t3 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)

    travels = service_remove_travels_with_price_bigger_than(travels_list, op_list, 1999)
    assert travels[0] == t1
    assert travels[1] == t3

    travels = repo_get_list(travels_list)
    assert travels[0] == t2


def test_service_remove_travels_for_duration_less_than():
    travels_list = []
    op_list = []
    t1 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 2000)
    t2 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 1000)
    t3 = service_create_travel(travels_list, op_list, [1, 2, 2024], [15, 2, 2024], 'Italy', 2000)
    travels = service_remove_travels_for_duration_less_than(travels_list, op_list, 13)
    assert travels[0] == t1
    assert travels[1] == t2

    travels = repo_get_list(travels_list)
    assert travels[0] == t3


def test_service_find_travels_for_destination_and_price_less_than():
    travels_list = []
    op_list = []
    t1 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Spain', 1999)
    t2 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 1999)
    t3 = service_create_travel(travels_list, op_list, [1, 2, 2024], [15, 2, 2024], 'Italy', 2000)
    travels = service_find_travels_for_destination_and_price_less_than(travels_list, 'Italy', 2000)
    assert travels[0] == t2


def test_service_find_travels_with_end_date():
    travels_list = []
    op_list = []
    t1 = service_create_travel(travels_list, op_list, [1, 2, 2024], [11, 2, 2024], 'Spain', 1999)
    t2 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 1999)
    t3 = service_create_travel(travels_list, op_list, [1, 2, 2024], [15, 2, 2024], 'Italy', 2000)
    travels = service_find_travels_with_end_date(travels_list, [12, 2, 2024])
    assert travels[0] == t2


def test_service_find_travels_between_start_and_end_date():
    travels_list = []
    op_list = []
    t1 = service_create_travel(travels_list, op_list, [1, 2, 2024], [11, 2, 2024], 'Spain', 1999)
    t2 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Italy', 1999)
    t3 = service_create_travel(travels_list, op_list, [1, 2, 2024], [15, 2, 2024], 'Italy', 2000)
    travels = service_find_travels_between_start_end_date(travels_list, [31, 1, 2024], [11, 2, 2024])
    assert travels[0] == t1


def test_service_remove_travels_with_price_bigger_and_not_destination():
    travels_list = []
    op_list = []
    t1 = service_create_travel(travels_list, op_list, [1, 2, 2024], [11, 2, 2024], 'Spain', 3000)
    t2 = service_create_travel(travels_list, op_list, [1, 2, 2024], [12, 2, 2024], 'Spain', 2000)
    t3 = service_create_travel(travels_list, op_list, [1, 2, 2024], [15, 2, 2024], 'Italy', 2000)
    travels = service_remove_travels_with_price_bigger_and_not_destination(travels_list, op_list, 2000, "Italy")
    assert len(travels) == 1
    assert travels[0] == t1


def test_service_remove_travels_containing_month():
    travels_list = []
    op_list = []
    t1 = service_create_travel(travels_list, op_list, [1, 2, 2024], [11, 2, 2024], 'Spain', 3000)
    t2 = service_create_travel(travels_list, op_list, [1, 5, 2024], [12, 5, 2024], 'Spain', 2000)
    t3 = service_create_travel(travels_list, op_list, [1, 10, 2024], [15, 2, 2025], 'Italy', 2000)
    t4 = service_create_travel(travels_list, op_list, [1, 1, 2024], [15, 3, 2025], 'Italy', 1000)
    travels = service_remove_travels_containing_month(travels_list, op_list, 2)
    assert len(travels) == 3
    assert travels[0] == t1
    assert travels[1] == t3
    assert travels[2] == t4


def test_service_find_number_of_travels_with_destination():
    travels_list = []
    op_list = []
    t1 = service_create_travel(travels_list, op_list, [1, 2, 2024], [11, 2, 2024], 'Spain', 3000)
    t2 = service_create_travel(travels_list, op_list, [1, 5, 2024], [12, 5, 2024], 'Italy', 2000)
    t3 = service_create_travel(travels_list, op_list, [1, 10, 2024], [15, 2, 2025], 'Italy', 2000)
    t4 = service_create_travel(travels_list, op_list, [1, 1, 2024], [15, 3, 2025], 'Italy', 1000)
    travels = service_find_number_of_travels_with_destination(travels_list, 'Italy')
    assert travels == 3


def test_service_find_price_avg_of_travels_with_destination():
    travels_list = []
    op_list = []
    t1 = service_create_travel(travels_list, op_list, [1, 2, 2024], [11, 2, 2024], 'Spain', 3000)
    t2 = service_create_travel(travels_list, op_list,[1, 5, 2024], [12, 5, 2024], 'Italy', 2000)
    t3 = service_create_travel(travels_list, op_list,[1, 1, 2024], [15, 3, 2025], 'Italy', 1000)
    avg = service_find_price_avg_of_travels_with_destination(travels_list, 'Italy')
    assert avg == 1500


def test_service_find_travels_between_dates_with_ascending_price():
    travels_list = []
    op_list = []
    t1 = service_create_travel(travels_list, op_list, [1, 2, 2024], [11, 2, 2024], 'Spain', 1296)
    t2 = service_create_travel(travels_list, op_list,[1, 2, 2024], [9, 2, 2024], 'Italy', 1111)
    t3 = service_create_travel(travels_list, op_list,[1, 2, 2024], [10, 2, 2024], 'Italy', 2000)
    t4 = service_create_travel(travels_list, op_list,[13, 1, 2024], [19, 1, 2024], 'Germany', 3000)
    t5 = service_create_travel(travels_list, op_list,[1, 2, 2024], [15, 6, 2024], 'Italy', 2000)
    t6 = service_create_travel(travels_list, op_list,[1, 2, 2024], [15, 5, 2024], 'Italy', 6000)
    travels = service_find_travels_between_dates_with_ascending_price(travels_list, [31, 1, 2024], [11, 2, 2024])
    assert travels[0] == t2
    assert travels[1] == t1
    assert travels[2] == t3


def test_service_undo():
    travels_list = []
    op_list = []
    t1 = service_create_travel(travels_list, op_list, [1, 2, 2024], [11, 2, 2024], 'Spain', 1296)
    service_update_travel(travels_list, op_list, 0, [1, 2, 2024], [15, 3, 2024], 'Italy', 1000)
    service_remove_by_id(travels_list, op_list, 0)
    travels = repo_get_list(travels_list)
    assert len(travels) == 0
    service_undo(travels_list, op_list)
    travels = repo_get_list(travels_list)
    assert len(travels) == 1

    assert get_travel_destination(travels[0]) == 'Italy'
    service_undo(travels_list, op_list)
    travels = repo_get_list(travels_list)
    assert len(travels) == 1
    assert get_travel_destination(travels[0]) == 'Spain'


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
    test_service_remove_travels_containing_month()
    test_service_find_number_of_travels_with_destination()
    test_service_find_price_avg_of_travels_with_destination()
    test_service_find_travels_between_dates_with_ascending_price()
    test_service_undo()
