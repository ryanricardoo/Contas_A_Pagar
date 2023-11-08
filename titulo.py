from datetime import date,datetime
from enum import Enum
from fornecedor import Fornecedor
from tinydb import TinyDB
from tinydb import Query
import os

class StatusPgto(Enum):
    pendente = "pendente"
    pago = "pago"
    atrasado = "atrasado"
    cancelado = "cancelado"

class MetodoPgto(Enum):
    cheque = "cheque"
    boleto = "boleto"
    cartao_credito = "cartão de credito"
    cartao_debito = "cartão de debito"
    dinheiro = "dinheiro"

class Titulo:
    db = "titulos.json"
    def __init__(self,valor:float,fornecedor:Fornecedor,desc:str,numero:int,status:str,vencimento:date):
        self.dt_emissao = date.now()
        self.vencimento = date
        self.pagamento = date
        self.valor = valor
        self.desc = desc
        self.numero = numero
        self.status = status
        self.fornecedor = fornecedor
        self.metogoPgto = str
    def menu():
        os.system('cls')
        print("1 Registrar título")
        print("2 Exibir títulos")
        print("9 Retornar")
        opcao = int(input("Informe a opcao desejada: "))
        match opcao:
            case 1:
                Titulo.Add()
            case 2:
                Titulo.Show()
            case 9:
                pass
    def Add():
        valor = float(input("Informe o valor do título: R$"))
        fornecedor = input("Informe o nome completo do fornecedor: ")
        desc = input("Informe a descrição do título: ")
        numero = input("Informe o número do título: ")
        status = StatusPgto.pendente.value
        vencimento = datetime.strptime(input("Informe a data de vencimento do título: "),'%d/%m/%Y')
        db = TinyDB(Titulo.db)
        db.insert({'valor':valor,'fornecedor':fornecedor,'desc':desc,'numero':numero,'vencimento':str(vencimento.date())})
        print("Título registrado")
        input("Pressione qualquer tecla para continuar")
    def Show():
        titulos = Query()
        db = TinyDB(Titulo.db)
        resultado = db.all()
        for titulo in resultado:
            print(f"Id: {titulo.doc_id}")
            print(f"Valor: R${titulo['valor']}")
            print(f"Fornecedor: {titulo['fornecedor']}")
            print(f"Descrição: {titulo['desc']}")
            print(f"Número: {titulo['numero']}")
            print(f"Vencimento: {titulo['vencimento']}")
            print('-------------------------------------------------')
        input("Pressione qualquer tecla para continuar")
def registrar_pgto(self, dt_pagamento):
    self.pagamento = dt_pagamento
    self.status = StatusPgto.pago.value

def metodo_pgto(self,metodo:str):
    self.metodo = metodo

