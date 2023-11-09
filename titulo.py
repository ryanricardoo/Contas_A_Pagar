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
    def __init__(self,valor:float,fornecedor:Fornecedor,desc:str,status:str,vencimento:date):
        self.dt_emissao = date.now()
        self.vencimento = date
        self.pagamento = date
        self.valor = valor
        self.desc = desc
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
        status = StatusPgto.pendente.value
        vencimento = datetime.strptime(input("Informe a data de vencimento do título no formato dia/mês/ano: "),'%d/%m/%Y')
        db = TinyDB(Titulo.db)
        db.insert({'valor':valor,'fornecedor':fornecedor,'desc':desc,'status':status,'vencimento':f'{vencimento.day}/{vencimento.month}/{vencimento.year}'})
        print("Título registrado")
        input("Pressione qualquer tecla para continuar")
    def Show():
        db = TinyDB(Titulo.db)
        titulos = Query()
        os.system('cls')
        print("1 Mostrar todos")
        print("2 Pendentes")
        print("3 Pagos")
        print("4 Atrasados")
        print("5 Cancelados")
        print("9 Retornar")
        opcao = int(input("Informe a opcao desejada: "))
        match opcao:
            case 1:
                resultado = db.all()
            case 2:
                resultado = db.search(titulos.status == StatusPgto.pendente.value)
            case 3:
                resultado = db.search(titulos.status == StatusPgto.pago.value)
            case 4:
                resultado = db.search(titulos.status == StatusPgto.atrasado.value)
            case 5:
                resultado = db.search(titulos.status == StatusPgto.cancelado.value)
            case 9:
                pass
        if(resultado.__len__()>0):
            for titulo in resultado:
                print(f"Valor: R${titulo['valor']}")
                print(f"Fornecedor: {titulo['fornecedor']}")
                print(f"Descrição: {titulo['desc']}")
                print(f"Número: {titulo.doc_id}")
                print(f"Vencimento: {titulo['vencimento']}")
                print('-------------------------------------------------')
        else:
            print("Nenhum título encontrado")
        input("Pressione qualquer tecla para continuar")
def registrar_pgto(self, dt_pagamento):
    self.pagamento = dt_pagamento
    self.status = StatusPgto.pago.value

def metodo_pgto(self,metodo:str):
    self.metodo = metodo

