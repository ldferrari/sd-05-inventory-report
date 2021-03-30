from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, productsList):
        a = super().generate(productsList)
        b = Counter(c["nome_da_empresa"] for c in productsList)
        r = ""
        for c in b:
            r += f"- {c}: {b[c]}" + "\n"

        return (
          a + "\n" +
          "Produtos estocados por empresa: " + "\n" +
          r
        )
