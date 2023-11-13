from datetime import date, datetime
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
    pendente = "pendente"

class Titulo:
    db = "titulos.json"
    def __init__(self,valor:float,fornecedor:Fornecedor,desc:str,status:str, metodoPgto:str, vencimento:date):
        self.dt_emissao = date.now()
        self.vencimento = date
        self.pagamento = str
        self.valor = valor
        self.desc = desc
        self.status = status
        self.fornecedor = fornecedor
        self.metogoPgto = metodoPgto
    def menu():
        os.system('cls||clear')
        print()
        print("1 Registrar título")
        print("2 Exibir títulos")
        print("3 Realizar pagamento")
        print("4 Cancelar titulo")
        print("9 Retornar")
        print("-------------------------------------")
        opcao = int(input("Informe a opcao desejada: "))
        match opcao:
            case 1:
                Titulo.Add()
            case 2:
                Titulo.Show()
            case 3:
                  Titulo.registrar_pgto()
            case 4:
                Titulo.Cancel()
                
            case 9:
                pass


    def Add():
        valor = float(input("Informe o valor do título: R$ "))
        fornecedor = input("Informe o nome completo do fornecedor: ")
        desc = input("Informe a descrição do título: ")
        forma_pagamento = MetodoPgto.pendente.value
        vencimento = datetime.strptime(input("Informe a data de vencimento do título no formato dia/mês/ano: "),'%d/%m/%Y')
        status = Verify_Status(vencimento)
        db = TinyDB(Titulo.db)
        db.insert({'valor':valor,'fornecedor':fornecedor,'desc':desc,'status':status,'vencimento':f'{vencimento.day}/{vencimento.month}/{vencimento.year}', 'meioPgto':forma_pagamento})
        print("Título registrado")
        input("Pressione qualquer tecla para continuar")

    def registrar_pgto():
        db = TinyDB(Titulo.db)
        titulos = Query()
        mostrar = db.search((titulos.status == StatusPgto.pendente.value) | (titulos.status == StatusPgto.atrasado.value))
        print("Qual titulo deseja realizar o pagamento? ")
        for titulo in mostrar:
            print(f"Número: {titulo.doc_id}")
            print(f"Fornecedor: {titulo['fornecedor']}")
            print(f"Valor: R${titulo['valor']}")
            print(f"Descrição: {titulo['desc']}")
            print(f"Vencimento: {titulo['vencimento']}")
            print(f"Status: {titulo['status']}")
            print('-------------------------------------------------')

        while True:
            try:
                opcao = int(input("Escolha o titulo a ser pago pelo número: "))
            except Exception as erro:
                opcao = None
                print(erro)
                continue
            else:
                break
        if opcao > 0 and opcao <= mostrar.__len__():
            db.update({'status': StatusPgto.pago.value}, doc_ids=[opcao])
            print("Qual o método de pagamento? ")
            print("1 Cheque")
            print("2 Boleto")
            print("3 Cartão de crédito")
            print("4 Cartão de débito")
            print("5 Dinheiro")
            forma_pagamento = int(input("Escolha a forma de pagamento: "))
            match forma_pagamento:
                case 1:
                    meioPgto = MetodoPgto.cheque.value
                    db.update({'meioPgto': meioPgto}, doc_ids=[opcao])
                case 2:
                    meioPgto = MetodoPgto.boleto.value
                    db.update({'meioPgto': meioPgto}, doc_ids=[opcao])
                case 3:
                    meioPgto = MetodoPgto.cartao_credito.value
                    db.update({'meioPgto': meioPgto}, doc_ids=[opcao])
                case 4:
                    meioPgto = MetodoPgto.cartao_debito.value
                    db.update({'meioPgto': meioPgto}, doc_ids=[opcao])
                case 5:
                    meioPgto = MetodoPgto.dinheiro.value
                    db.update({'meioPgto': meioPgto}, doc_ids=[opcao])
            print("Pagamento registrado")
            print("-------------------------------------------------")
        else:
            print("Documento selecionado inválido!")


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
                print(f"Método de pagamento: {titulo['meioPgto']}")
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


