import os
from fornecedor import Fornecedor
from titulo import Titulo

def menu():
    while True:
        try:
            os.system('cls')
            print("1 Fornecedores")
            print("2 Títulos")
            print("9 Sair")
            opcao = int(input("Informe a opcao desejada: "))
            match opcao:
                case 1:
                    Fornecedor.menu()
                case 2:
                    Titulo.menu()
                    pass
                case 9:
                    sai_sys = input("Deseja sair (S)im/(N)ao: ").upper()
                    if sai_sys in ['SIM', 'S']:
                        break         
        except Exception as error:
         print("Opção Inválida")
         input("Pressione qualquer tecla para continuar")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()
        

