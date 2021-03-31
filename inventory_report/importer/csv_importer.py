import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def assign_data(self, data, header):
        results = []
        for row in data:
            article = {}
            counter = 0
            for keys in header:
                article[keys] = row[counter]
                counter += 1
            results.append(article)
        return results

    @classmethod
    def import_data(self, filepath):
        try:
            assert filepath.split('.')[1] == 'csv'
            with open(filepath) as file:
                beach_status_reader = csv.reader(
                  file, delimiter=",", quotechar='"'
                )
                header, *data = beach_status_reader
        except AssertionError:
            raise ValueError('Arquivo inválido')
        except FileNotFoundError:
            raise ValueError(f'Arquivo {filepath} não encontrado')
        else:
            return self.assign_data(data, header)
