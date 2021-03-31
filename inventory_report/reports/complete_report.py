from inventory_report.reports.simple_report import SimpleReport


def string_template(simple_report, quantidade_produtos):
    template = f"""{simple_report}\nProdutos estocados por empresa: \n"""
    for produto in quantidade_produtos:
        template = template + produto
    return template


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, data_list):
        simple_report = super().generate(data_list)
        products_from_empresas = {}
        quantidade_produtos = []
        empresas = []

        # Gera o complemento do report
        for report in data_list:
            empresa = report["nome_da_empresa"]
            if empresa not in empresas:
                empresas.append(empresa)
            if empresa not in products_from_empresas:
                products_from_empresas[empresa] = 0
            products_from_empresas[empresa] += 1

        for empresa in empresas:
            qtd_product = products_from_empresas[empresa]
            quantidade_produtos.append(f"""- {empresa}: {qtd_product}\n""")

        return string_template(simple_report, quantidade_produtos)
