from Service import Service


class Console:
    def __init__(self, residence_service: Service):
        self.__residence_service = residence_service

    def run(self):
        print("""
1. Show residences by price and city.
2. Rent a residence.
3. Exit.
        """)
        while True:
            try:
                o = input("o: ")
            except ValueError:
                continue
            match o:
                case '1':
                    self.show_residences_by_price_and_city()
                case '2':
                    self.rent_a_residence()
                case '3':
                    break

    def show_residences_by_price_and_city(self):
        try:
            price = int(input('Price: '))
            city = input('City: ')
            residences = self.__residence_service.find_residences_by_price_and_city(price, city)
            for r in residences:
                print(r)
        except ValueError as e:
            print(e)

    def rent_a_residence(self):
        try:
            id_ = input('Id: ')
            data = self.__residence_service.rent_a_residence(id_)
            print('Rented')
            print('Address: ', data[0])
            print('City: ', data[1])
            print('Total price: ', data[2])
        except ValueError as e:
            print(e)
