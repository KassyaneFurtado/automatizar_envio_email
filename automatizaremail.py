#Automatizar envio de email para lembrete de retorno de pacientes
import yagmail
from datetime import datetime
import pandas
tabela = pandas.read_csv("retornomasto.csv")
print(tabela)
#contato que irá receber o email
contato = input("Insira seu email")
#Descobrir data atual
datahoje = datetime.now().strftime("%d/%m/%y")
#comparar data atual com data de retorno e enviar o email
emailServer = yagmail.SMTP("remetente","senha")
for linha in tabela:
    RETORNO = datetime.strptime(str(linha["RETORNO"]).strip(), "%d/%m/%y").strftime("%d/%m/%y")
    PACIENTE = tabela.loc[linha,"PACIENTE"]
    HORARIO = tabela.loc[linha,"HORARIO"]
    if RETORNO -datahoje:
        emailServer.send(contato,subject= "CAPTAR PACIENTE DE RETORNO MASTOLOGIA", contents= PACIENTE + HORARIO + RETORNO)

