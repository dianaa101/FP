from repositories.Repository import Repository


class Service:
    def __init__(self, repo: Repository):
        self.__repo = repo

    def get_activities_containing_part(self, part):
        activities = []

        for a in self.__repo.get_all():
            if part in a.get_description():
                activities.append(a)
        activities.sort(key=lambda a: a.get_battery_percentage(), reverse=True)
        return activities

    def robot_activities(self, x, y):
        results = []
        activities = self.__repo.get_all()

        for a in activities:
            x1 = x
            y1 = y
            battery = a.get_battery_percentage()
            for i in a.get_instructions():
                if i == 'halt':
                    battery = battery + 5
                    continue

                if battery < 10:
                    break

                if i == 'up':
                    y1 = y1 + 1
                    battery = battery - 10
                elif i == 'down':
                    y1 = y1 - 1
                    battery = battery - 10
                elif i == 'left':
                    x1 = x1 - 1
                    battery = battery - 10
                elif i == 'right':
                    x1 = x1 + 1
                    battery = battery - 10
            results.append([a.get_id(), x1, y1, battery])
        return results

