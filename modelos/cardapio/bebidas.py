from modelos.cardapio.item_cardapio import Item_cardapio
class Bebidas(Item_cardapio):
    def __init__(self, nome, preco, marca, tamanho):
        super.__init__(nome,preco)
        self.marca = marca
        self.tamanho =  tamanho