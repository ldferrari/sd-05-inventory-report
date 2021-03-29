from datetime import datetime


DATE_FORMAT = "%Y-%m-%d"


class SimpleReport:
    @classmethod
    def generate(cls, lista):
        return (
            f"Data de fabricação mais antiga: {cls.get_oldest_date(lista)}\n"
            f"Data de validade mais próxima: {cls.get_next_date(lista)}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{cls.get_company(lista)}\n"
        )

    @staticmethod
    def get_oldest_date(lista):
        lista.sort(
            key=lambda item: datetime.strptime(
                item["data_de_fabricacao"], DATE_FORMAT
            )
        )
        return lista[0]["data_de_fabricacao"]

    @staticmethod
    def get_next_date(lista):
        today = datetime.today()

        filtered_list = list(
            (
                filter(
                    lambda item: datetime.strptime(
                        item["data_de_validade"], DATE_FORMAT
                    )
                    > today,
                    lista,
                )
            )
        )

        sorted_list = sorted(
            filtered_list,
            key=lambda item: datetime.strptime(
                item["data_de_validade"], DATE_FORMAT
            ),
        )

        return sorted_list[0]["data_de_validade"]

    @staticmethod
    def get_company(lista):

        counter = {}

        for dic in lista:
            key = dic["nome_da_empresa"]
            counter[key] = counter.get(key, 0) + 1

        return sorted(counter.items(), key=lambda kv: kv[1])[-1][0]
