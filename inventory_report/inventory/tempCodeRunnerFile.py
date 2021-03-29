       if report_type == "simples":
            report = SimpleReport.generate(stock)
        else:
            report = CompleteReport.generate(stock)

        return report