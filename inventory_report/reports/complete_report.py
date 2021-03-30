from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def format_output(self, simple_report, complete_report):
        text = "Produtos estocados por empresa: \n"
        output = ""
        for product in complete_report:
            output += f"- {product[0]}: {product[1]}\n"
        return simple_report + "\n" + text + output

    @classmethod
    def generate(self, products):
        simple_report = super().generate(products)
        products_per_company = Counter(
            product["nome_da_empresa"] for product in products
        ).items()
        return self.format_output(self, simple_report, products_per_company)
