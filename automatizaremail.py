#Automatizar envio de email para lembrete de retorno de pacientes
from dotenv import load_dotenv

import yagmail
from datetime import datetime
import pandas
import os

load_dotenv()

tabela = pandas.read_csv("retornos.csv").to_dict('records')

dataHoje = datetime.today().date()

emailServer = yagmail.SMTP(
    os.getenv("USUARIO_SMTP"),
    os.getenv("SENHA_SMTP")
)

for linha in tabela:
    dataRetorno = datetime.strptime(linha["RETORNO"], "%d/%m/%Y").date()

    PACIENTE = linha["PACIENTE"]
    HORARIO = linha["HORARIO"]
    OBS = linha["OBS"]
    if dataRetorno == dataHoje:
        emailServer.send(
            os.getenv("EMAIL_RETORNO"),
            subject= "CAPTAR PACIENTE DE RETORNO", 
            contents= f"{PACIENTE}  {HORARIO} {OBS} {linha["RETORNO"]}"
        )

