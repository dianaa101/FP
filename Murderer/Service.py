from datetime import datetime

from repositories.Repository import Repository


class Service:
    def __init__(self, repo: Repository):
        self.__repo = repo

    def get_evidences_containing_part(self, part):
        evidences = []

        for e in self.__repo.get_all():
            if part in e.get_suspect():
                evidences.append(e)
        evidences.sort(key=lambda e: (e.get_date()[0], e.get_date()[1], e.get_date()[2]), reverse=True)

        return evidences

    def get_suspects(self):
        suspects = []
        for e in self.__repo.get_all():
            s = e.get_suspect()
            if s not in suspects:
                suspects.append(s)
        return suspects

    def get_evidences_for_suspect(self, suspect):
        evidences = []
        for e in self.__repo.get_all():
            if e.get_suspect() == suspect:
                evidences.append(e)
        return evidences

    def get_number_of_unique_evidences(self, evidences):
        unique_evidences = []
        for e in evidences:
            if e.get_type() not in unique_evidences:
                unique_evidences.append(e)
        return len(unique_evidences)

    def get_duration_between_evidences(self, evidences):
        min_date = None
        max_date = None
        for e in evidences:
            d = e.get_date()
            dp = datetime(d[0], d[1], d[2])
            if min_date is None or dp < min_date:
                min_date = dp
            if max_date is None or dp > max_date:
                max_date = dp
        return (max_date - min_date).days

    def identify_criminals(self):
        results = []
        suspects = self.get_suspects()
        for s in suspects:
            es = self.get_evidences_for_suspect(s)
            nues = self.get_number_of_unique_evidences(es)
            d = self.get_duration_between_evidences(es)
            if len(es) >= 3:
                c = "criminal"
            else:
                c = "inocent"
            results.append([s, nues, d, c])

        return results
