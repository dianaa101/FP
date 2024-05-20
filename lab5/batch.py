from service import *
from travel import *


def batch_parse_date(arg):
    date_str = arg.split("/")
    return [int(x) for x in date_str]


def batch_parse_add(args, travels_list, op_list):
    start_date = batch_parse_date(args[0])
    end_date = batch_parse_date(args[1])
    destination = args[2]
    price = int(args[3])
    t = service_create_travel(travels_list, op_list, start_date, end_date, destination, price)
    print('Added')
    print(get_travel_string(t))


def batch_parse_update(args, travels_list, op_list):
    id_ = int(args[0])
    start_date = batch_parse_date(args[1])
    end_date = batch_parse_date(args[2])
    destination = args[3]
    price = int(args[4])

    t = service_update_travel(travels_list, op_list, id_, start_date, end_date, destination, price)
    print('Updated')
    print(get_travel_string(t))


def batch_parse_remove(args, travels_list, op_list):
    id_ = int(args[0])
    t = service_remove_by_id(travels_list, op_list, id_)
    print('Removed')
    print(get_travel_string(t))


def batch_parse_filter(args, travels_list, op_list):
    destination = args[0]
    price = int(args[1])
    removed_travels = service_remove_travels_with_price_bigger_and_not_destination(travels_list, op_list, price, destination)
    print('Removed')
    for x in removed_travels:
        print(get_travel_string(x))


def batch_parse_undo(travels_list, op_list):
    service_undo(travels_list, op_list)


def batch_parse_one(batch, travels_list, op_list):
    params = batch.strip().split(" ")
    if len(params) == 0:
        return
    cmd = params[0]
    args = params[1:]
    if cmd == "add" and len(args) == 4:
        batch_parse_add(args, travels_list, op_list)
        print(travels_list)
    elif cmd == "update" and len(args) == 5:
        batch_parse_update(args, travels_list, op_list)
        print(travels_list)
    elif cmd == "remove" and len(args) == 1:
        batch_parse_remove(args, travels_list, op_list)
        print(travels_list)
    elif cmd == "filter" and len(args) == 2:
        batch_parse_filter(args, travels_list, op_list)
        print(travels_list)
    elif cmd == "undo" and len(args) == 0:
        batch_parse_undo(travels_list, op_list)
        print(travels_list)
    else:
        raise ValueError("cmd invalid!")


def batch_run():
    travels_list = []
    op_list = []
    print("format: cmd; cmd; ...")
    print("cmd:")
    print("add start_date end_date destination price")
    print("update id start_date end_date destination price")
    print("remove id")
    print("filter destination price")
    print("undo")
    while True:
        line = input("cmd: ")
        batches = line.split(";")
        for b in batches:
            try:
                batch_parse_one(b, travels_list, op_list)
            except Exception as e:
                print(e)
