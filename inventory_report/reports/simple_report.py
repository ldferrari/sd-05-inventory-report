from datetime import datetime, timedelta
from collections import Counter


def retorna_fabricacao_mais_antiga(lista):
    present = datetime.now()
    data_timedelta = timedelta(days=1)
    for item in lista:
        try:
            data_descartavel = datetime.strptime(
                item["data_de_fabricacao"], '%Y-%m-%d')
        except ValueError:
            raise ValueError("Data inválida")
        else:
            tempo_relativo = present - data_descartavel
            if (tempo_relativo > data_timedelta):
                data_timedelta = tempo_relativo
                saida = data_descartavel
    return saida


def retorna_validade_mais_proxima(lista):
    present = datetime.now()
    data_timedelta = timedelta(days=15000)
    for item in lista:
        try:
            data_descartavel = datetime.strptime(
                item["data_de_validade"], '%Y-%m-%d')
        except ValueError:
            raise ValueError("Data inválida")
        else:
            tempo_relativo = data_descartavel - present
            if (tempo_relativo < data_timedelta
               and data_descartavel > present):
                data_timedelta = tempo_relativo
                saida = data_descartavel
    return saida


def retorna_empresa_maior_estoque(lista):
    empresas = []
    for item in lista:
        empresas.append(item["nome_da_empresa"])
    contador_ocorrencia = Counter(empresas)
    return contador_ocorrencia.most_common(1)[0][0]


class SimpleReport:

    @classmethod
    def generate(cls, lista):
        fabricacao_mais_antiga = datetime.strftime(
            retorna_fabricacao_mais_antiga(lista),
            "%Y-%m-%d"
        )

        data_validade_mais_proxima = datetime.strftime(
            retorna_validade_mais_proxima(lista),
            "%Y-%m-%d"
        )
        empresa = retorna_empresa_maior_estoque(lista)

        m1 = f"Data de fabricação mais antiga: {fabricacao_mais_antiga}"
        m2 = f"Data de validade mais próxima: {data_validade_mais_proxima}"
        m3 = f"Empresa com maior quantidade de produtos estocados: {empresa}"

        return f"{m1}\n{m2}\n{m3}\n"


#   https://www.educative.io/edpresso/how-to-convert-a-string-to-a-date-in-python
#   https://docs.python.org/3/library/datetime.html
#   https://stackoverflow.com/questions/8142364/how-to-compare-two-dates
#   https://realpython.com/python-f-strings/
#   https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
#   https://stackoverflow.com/questions/4613000/difference-between-cls-and-self-in-python-classes
