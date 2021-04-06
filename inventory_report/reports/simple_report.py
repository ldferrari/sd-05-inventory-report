from datetime import datetime
from statistics import mode


class SimpleReport:
    def __init__(self):
        pass

    @classmethod
    def generate(cls, lista):
        agora = datetime.today()

        agora_formatado = f"{agora.year}-{agora.month}-{agora.day}"

        data_fabricacao = min(
            [
                datetime.strptime(
                    item["data_de_fabricacao"], "%Y-%m-%d"
                ).date()
                for item in lista
            ]
        )

        data_validade = min(
            [
                datetime.strptime(item["data_de_validade"], "%Y-%m-%d").date()
                for item in lista
                if datetime.strptime(
                    item["data_de_validade"], "%Y-%m-%d"
                ).date()
                > datetime.strptime(agora_formatado, "%Y-%m-%d").date()
            ]
        )

        maior_stoc = mode([item["nome_da_empresa"] for item in lista])

        relatorio_formatado = (
          f"Data de fabricação mais antiga: {data_fabricacao}\n"
          f"Data de validade mais próxima: {data_validade}\n"
          f"Empresa com maior quantidade de produtos estocados: {maior_stoc}\n"
        )

        return relatorio_formatado
