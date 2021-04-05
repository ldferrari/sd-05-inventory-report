from datetime import datetime

f_a = 'Data de fabricação mais antiga: '
v_p = 'Data de validade mais próxima: '
qtd = 'Empresa com maior quantidade de produtos estocados: '


def data(data):
    data_formatada = datetime.strptime(data, '%Y-%m-%d').date()
    return data_formatada


def quant(lista):
    empresas = []
    quantidade = 0
    empresa = ''
    for item in lista:
        empresas.append(item['nome_da_empresa'])
    for item in lista:
        quant = empresas.count(item['nome_da_empresa'])
        if quant > quantidade:
            quantidade = quant
            empresa = item['nome_da_empresa']
    return empresa


def mais_antiga(lista):
    data_fabricacao_antiga = data('9999-12-30')
    for item in lista:
        fabricacao_antiga = data(item['data_de_fabricacao'])
        if fabricacao_antiga < data_fabricacao_antiga:
            data_fabricacao_antiga = fabricacao_antiga
    return data_fabricacao_antiga


def validade(lista):
    data_v_p = data('9999-12-30')
    hoje = data(datetime.today().strftime('%Y-%m-%d'))
    for item in lista:
        v_p = data(item['data_de_validade'])
        if v_p > hoje and v_p < data_v_p:
            data_v_p = v_p
    return data_v_p


class SimpleReport:
    def __init__(self):
        pass

    def generate(lista):
        f_m_a = mais_antiga(lista)
        v_m_p = validade(lista)
        quantidade = quant(lista)
        return f'{f_a}{f_m_a}\n{v_p}{v_m_p}\n{qtd}{quantidade}\n'
        