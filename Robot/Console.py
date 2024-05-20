from Service import Service


class Console:
    def __init__(self, activity_service: Service):
        self.__activity_service = activity_service

    def run(self):
        print("""
1. Print activities containing description
2. Print robot activities
        """)
        while True:
            try:
                o = int(input("o: "))
            except ValueError:
                continue
            match o:
                case 1:
                    self.print_activities_containing_description()
                case 2:
                    self.print_robot_activities()
                case 3:
                    break

    def print_activities_containing_description(self):
        try:
            part = input('Part: ')
            activities = self.__activity_service.get_activities_containing_part(part)
            if len(activities) == 0:
                print('Nonexistent activity')
            for a in activities:
                print(a)
        except ValueError as e:
            print(e)

    def print_robot_activities(self):
        try:
            x = int(input('X: '))
            y = int(input('Y: '))
            activities = self.__activity_service.robot_activities(x, y)
            for a in activities:
                print(f'{a[0]}: <{a[1]},{a[2]}>, {a[3]}')
        except ValueError as e:
            print(e)
