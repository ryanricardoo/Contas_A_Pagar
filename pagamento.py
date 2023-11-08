from datetime import date


class Pagamento:
    def __init__(self,numero:str,metodo:str,data:date,comentario:str):
        self.numero = numero
        self.metodo = metodo
        self.data = data
        self.comentario = comentario