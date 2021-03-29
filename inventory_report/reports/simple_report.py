from datetime import datetime
from statistics import mode


class SimpleReport:
    def __init__(self):
        pass

    @classmethod
    def generate(cls, list):
        hoje = datetime.today()
        hojeF = f"{hoje.year}-0{hoje.month}-{hoje.day}"

        data_de_fabricacao = min(
            [
                datetime.strptime(
                    data["data_de_fabricacao"], "%Y-%m-%d"
                ).date()
                for data in list
            ]
        )

        data_de_vencimento = min(
            [
              datetime.strptime(data["data_de_validade"], "%Y-%m-%d").date()
              for data in list
              if datetime.strptime(data["data_de_validade"], "%Y-%m-%d")
              .date()
              > datetime.strptime(hojeF, "%Y-%m-%d").date()
            ]
        )

        stock = mode([data["nome_da_empresa"] for data in list])

        relatorio = (
            f"Data de fabricação mais antiga: {data_de_fabricacao}\n"
            f"Data de validade mais próxima: {data_de_vencimento}\n"
            f"Empresa com maior quantidade de produtos estocados: {stock}\n"
        )

        return relatorio
