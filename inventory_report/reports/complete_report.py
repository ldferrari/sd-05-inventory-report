from inventory_report.reports.simple_report import SimpleReport


def remove_repetidos(arr):
    i = []
    for item in arr:
        if item not in i:
            i.append(item)
    return i
# a função acima remove itens duplicados de uma lista
# fonte: https://pt.stackoverflow.com/questions
# /192567/removendo-elementos-duplicados-em-uma-lista-com-python


def quantidade_por_empresa(lista):
    empresas_quantidades = []
    empresas = []
    for item in lista:
        empresas.append(item['nome_da_empresa'])
    for item in lista:
        empresas_quantidades.append({
            'empresa': item['nome_da_empresa'],
            'quantidade': empresas.count(item['nome_da_empresa'])
        })
    return remove_repetidos(empresas_quantidades)


def format_qtd(lista):
    quantidades = 'Produtos estocados por empresa: \n'
    for item in lista:
        quantidade = item['quantidade']
        empresa = item['empresa']
        quantidades += f'- {empresa}: {quantidade}\n'
    return quantidades


class CompleteReport(SimpleReport):
    def __init__(self):
        SimpleReport.__init__(self)

    def generate(lista):
        simple = SimpleReport.generate(lista)
        complete = format_qtd(quantidade_por_empresa(lista))
        return f'{simple}\n{complete}'
