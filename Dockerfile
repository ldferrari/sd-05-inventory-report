FROM python:3
RUN mkdir inventory-report
WORKDIR /inventory-report
COPY . .
# Instalando as dependências
RUN apt-get update && apt-get install -y \
    python3-venv
RUN python3 -m venv .venv && \
    python3 -m pip install -r dev-requirements.txt

# Para rodar o container:
# docker build . -t trybe/inventory-report
# docker run -it --name=project -v $PWD/inventory_report:/inventory-report/inventory_report trybe/inventory-report bash