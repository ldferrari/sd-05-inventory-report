from datetime import datetime
from statistics import mode


class SimpleReport:
    def __init__(self):
        pass

    @classmethod
    def generate(cls, list):
        now = datetime.today()

        now_formatted = f"{now.year}-{now.month}-{now.day}"

        date_making = min(
            [
                datetime.strptime(item["data_de_fabricacao"], "%Y-%m-%d").date()
                for item in list
            ]
        )

        date_expiration = min(
            [
                datetime.strptime(item["data_de_validade"], "%Y-%m-%d").date()
                for item in list
                if datetime.strptime(
                    item["data_de_validade"], "%Y-%m-%d"
                ).date()
                > datetime.strptime(now_formatted, "%Y-%m-%d").date()
            ]
        )

        max_storage = mode([item["nome_da_empresa"] for item in list])

        report_formatted = (
          f"Data de fabricação mais antiga: {date_making}\n"
          f"Data de validade mais próxima: {date_expiration}\n"
          f"Empresa com maior quantidade de produtos estocados: {max_storage}\n"
        )

        return report_formatted
