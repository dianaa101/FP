from Service import Service


class Console:
    def __init__(self, evidence_service: Service):
        self.__evidence_service = evidence_service

    def run(self):
        print("""
1. Print evidences containing suspect
2. Print identified criminals
        """)
        while True:
            try:
                o = int(input("o: "))
            except ValueError:
                continue
            match o:
                case 1:
                    self.print_evidences_containing_suspect()
                case 2:
                    self.print_identified_criminals()
                case 3:
                    break

    def print_evidences_containing_suspect(self):
        try:
            part = input('Part: ')
            evidences = self.__evidence_service.get_evidences_containing_part(part)
            if len(evidences) == 0:
                print('Nonexistent evidence')
            for e in evidences:
                print(e)
        except ValueError as e:
            print(e)

    def print_identified_criminals(self):
        try:
            criminals = self.__evidence_service.identify_criminals()
            for x in criminals:
                print(f'{x[0]}: {x[1]},{x[2]},{x[3]}')
        except ValueError as e:
            print(e)
