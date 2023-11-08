from tinydb import TinyDB
from tinydb import Query
import os
class Fornecedor:
    db = "fornecedores.json"
    def __init__(self,nome:str,endereco:str,telefone:str,contato:str):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.contato = contato
    def menu():
            os.system('cls')
            print("1 Registrar Título")
            print("2 Exibir fornecedores")
            print("3 Remover fornecedor")
            print("4 Alterar fornecedor")
            print("5 Pesquisar fornecedor")
            print("6 Retornar")
            opcao = int(input("Informe a opcao desejada: "))
            match opcao:
                case 1:
                    Fornecedor.Add()
                case 2:
                    Fornecedor.Show()
                case 3:
                    Fornecedor.Remove()
                case 4:
                    Fornecedor.Update()
                case 5:
                    Fornecedor.Search()
                case 6:
                    pass
    def Add():
        nome = input("Informe o nome do fornecedor: ")
        endereco = input("Informe o endereço do fornecedor: ")
        telefone = input("Informe o telefone do fornecedor: ")
        contato = input("Informe o contato do fornecedor: ")
        db = TinyDB(Fornecedor.db)
        db.insert({'nome':nome,'endereco':endereco,'telefone':telefone,'contato':contato})
        print("Fornecedor registrado")
        input("Pressione qualquer tecla para continuar")

    def Show():
        db = TinyDB(Fornecedor.db)
        resultado = db.all()
        for fornecedor in resultado:
            print(f"Id: {fornecedor.doc_id}")
            print(f"Nome: {fornecedor['nome']}")
            print(f"Endereço: {fornecedor['endereco']}")
            print(f"Telefone: {fornecedor['telefone']}")
            print(f"Contato: {fornecedor['contato']}")
            print('-------------------------------------------------')
        input("Pressione qualquer tecla para continuar")

    def Remove():
        id = int(input("Informe o id do fornecedor: "))
        db = TinyDB(Fornecedor.db)
        nome = db.get(doc_id=id)['nome']
        result = db.remove(doc_ids=[id])
        if(result.__len__() > 0):
            print(f"Fornecedor {nome} removido")
        else:
            print(f"Fornecedor não encontrado")
        input("Pressione qualquer tecla para continuar")
        
    def Update():
        id = int(input("Informe o id do fornecedor: "))
        db = TinyDB(Fornecedor.db)
        fornecedor = db.get(doc_id=id)
        if(fornecedor is not None):
            nome = input("Informe o nome do fornecedor: ")
            endereco = input("Informe o endereço do fornecedor: ")
            telefone = input("Informe o telefone do fornecedor: ")
            contato = input("Informe o contato do fornecedor: ")
            db.update({'nome':nome,'endereco':endereco,'telefone':telefone,'contato':contato},doc_ids=[id])
            print("Dados do fornecedor atualizados")
        else:
            print("Fornecedor não encontrado")
        input("Pressione qualquer tecla para continuar")
        
    def Search():
        nome = input("Informe o nome do fornecedor: ")
        db = TinyDB(Fornecedor.db)
        fornecedores = Query()
        result = db.search(fornecedores.nome == nome)
        if(result.__len__()>0):
           for fornecedor in result:
            print(f"Id: {fornecedor.doc_id}")
            print(f"Nome: {fornecedor['nome']}")
            print(f"Endereço: {fornecedor['endereco']}")
            print(f"Telefone: {fornecedor['telefone']}")
            print(f"Contato: {fornecedor['contato']}")
            print('-------------------------------------------------')
        else:
            print("Fornecedor não encontrado")
        input("Pressione qualquer tecla para continuar")
