from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


def retorna_dic_estoque(lista):
    empresas = []
    for item in lista:
        empresas.append(item["nome_da_empresa"])
    contador_ocorrencia = Counter(empresas)
    return dict(contador_ocorrencia)


def retorna_relatorio_completo(lista):
    relatorio_simples = SimpleReport.generate(lista) + "\n"
    estoque = retorna_dic_estoque(lista)

    detalhe_estoque = "Produtos estocados por empresa: \n"
    for key in estoque:
        detalhe_estoque += ("- %s: %s\n" % (key, estoque[key]))
    relatorio_completo = relatorio_simples + detalhe_estoque
    return relatorio_completo


class CompleteReport:
    @classmethod
    def generate(cls, lista):
        return retorna_relatorio_completo(lista)

#   https://stackoverflow.com/questions/11068986/how-to-convert-counter-object-to-dict
#   https://stackoverflow.com/questions/3545331/how-can-i-get-dictionary-key-as-variable-directly-in-python-not-by-searching-fr
