from datetime import datetime
from statistics import mode

date_time = "%Y-%m-%d"


class SimpleReport:
    def __init__(self):
        pass

    @classmethod
    def oldest(cls, list):
        manufact = min(
            [
                datetime.strptime(data["data_de_fabricacao"], date_time).date()
                for data in list
            ]
        )
        return manufact

    @classmethod
    def neardest(cls, list):
        now = datetime.today().strftime(date_time)
        valid = min(
            [
                datetime.strptime(data["data_de_validade"], date_time).date()
                for data in list
                if datetime.strptime(
                    data["data_de_validade"], date_time
                ).date()
                > datetime.strptime(now, date_time).date()
            ]
        )

        return valid

    @classmethod
    def bigest_stock(cls, list):
        stock = mode([data["nome_da_empresa"] for data in list])
        return stock

    @classmethod
    def generate(cls, list):
        report = ""
        oldest_date = cls.oldest(list)
        report += (f"Data de fabricação mais antiga: {oldest_date}\n")
        valid_date = cls.neardest(list)
        report += (f"Data de validade mais próxima: {valid_date} \n")
        stock = cls.bigest_stock(list)
        report += (
            f"Empresa com maior quantidade de produtos estocados: {stock}\n"
        )
        return report
