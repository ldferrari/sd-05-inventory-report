from datetime import datetime
from statistics import mode

class SimpleReport:
    def __init__(self):
        pass

    @classmethod
    def oldest(cls, list):
        fabricacao = min(
            [
                datetime.strptime(
                    data["data_de_fabricacao"], "%Y-%m-%d"
                ).date()
                for data in list
            ]
        )
        return fabricacao

    @classmethod
    def nearest(cls, list):
        hoje = datetime.today().strftime('%Y-%m-%d')
        validade = min (
            [
                datetime.strptime(
                    data["data_de_validade"], "%Y-%m-%d"
                ).date()
                for data in list
                if datetime.strptime(data["data_de_validade"], "%Y-%m-%d").date()
                > datetime.strptime(hoje, "%Y-%m-%d").date()
            ]
        )
        print(validade)
        return validade

    @classmethod
    def bigest_stock(cls, list):
        stock = mode([data["nome_da_empresa"] for data in list])
        return stock

    @classmethod
    def generate(cls, list):
        report = ""
        oldest_date = cls.oldest(list)
        report += (f"Data de fabricação mais antiga: {oldest_date}\n")
        validade_date = cls.nearest(list)
        report += (f"Data de validade mais próxima: {validade_date}\n")
        stock_date = cls.bigest_stock(list)
        report += (f"Empresa com maior quantidade de produtos estocados: {stock_date}\n")
        return report
