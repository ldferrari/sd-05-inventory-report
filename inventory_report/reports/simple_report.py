from datetime import datetime


class SimpleReport:
    def __init__(self):
        pass

    @classmethod
    def generate(cls, list):
        data_de_fabricacao = min(
            [
                datetime.strftime(
                    data["data_de_fabricacao"], "%Y-%m-%d"
                ).date()
                for data in list
            ]
        )

        relatorio = (
            f"Data de fabricação mais antiga: {data_de_fabricacao}\n"
        )

        return relatorio
