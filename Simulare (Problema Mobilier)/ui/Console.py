from service import MobilierService


class Console:
    def __init__(self, service_furniture: MobilierService):
        self.service_furniture = service_furniture

    def run(self):
        print("""
1. Find furniture by type
2. Buy furniture
3. Exit
        """)
        while True:
            try:
                o = int(input("o: "))
            except ValueError:
                continue
            match o:
                case 1:
                    self.find_furniture_by_type()
                case 2:
                    self.buy_furniture()
                case 3:
                    break

    def find_furniture_by_type(self):
        try:
            type_ = input('Type: ')
            furniture = self.service_furniture.find_by_type(type_)
            for f in furniture:
                print(f)
        except ValueError as e:
            print(e)

    def buy_furniture(self):
        try:
            id_ = input('Id: ')
            requested_stock = int(input('Requested stock: '))
            data = self.service_furniture.buy_furniture(id_, requested_stock)
            print('Bought')
            print('Name: ', data[0])
            print('Total price: ', data[1])
            print('Remaining stock: ', data[2])
        except ValueError as e:
            print(e)
