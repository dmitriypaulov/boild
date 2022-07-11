import csv


class i18nBlock():
    def __init__(self, path, language, language_verbal):
        self.path = path
        self.language = language
        self.language_verbal = language_verbal
        self.type = path.split(".")[-1]

    def get(self):
        terms = {}
        if self.type == "csv":
            terms = self._get_csv()
        return {self.language: terms}

    def _get_csv(self):
        terms = {}
        with open(self.path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                terms[row["term"]] = row["translation"]
        return terms
