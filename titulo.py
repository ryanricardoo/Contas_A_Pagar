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
        print("3 Realizar pagamento")
        print("4 Cancelar titulo")
        print("9 Retornar")
        opcao = int(input("Informe a opcao desejada: "))
        match opcao:
            case 1:
                Titulo.Add()
            case 2:
                Titulo.Show()
            case 3:
                pass
            case 4:
                Titulo.Cancel()
            case 9:
                pass
    def Add():
        valor = float(input("Informe o valor do título: R$"))
        fornecedor = input("Informe o nome completo do fornecedor: ")
        desc = input("Informe a descrição do título: ")
        vencimento = datetime.strptime(input("Informe a data de vencimento do título no formato dia/mês/ano: "),'%d/%m/%Y')
        status = Verify_Status(vencimento)
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
                print(f"Status: {titulo['status']}")
                print('-------------------------------------------------')
        else:
            print("Nenhum título encontrado")
        input("Pressione qualquer tecla para continuar")

    def Cancel():
        db = TinyDB(Titulo.db)
        id = int(input("Informe o número do titulo: "))
        titulo = db.get(doc_id=id)
        if (titulo is not None):
            db.update({'status':StatusPgto.cancelado.value},doc_ids=[id])
            print("Título cancelado")
        else:
            print("Título não encontrado")
        input("Pressione qualquer tecla para continuar")



def Verify_Status(vencimento):
    hoje = datetime.now()
    if hoje <= vencimento:
        return StatusPgto.pendente.value
    else:
        return StatusPgto.atrasado.value


def registrar_pgto(self, dt_pagamento):
    self.pagamento = dt_pagamento
    self.status = StatusPgto.pago.value

def metodo_pgto(self,metodo:str):
    self.metodo = metodo

