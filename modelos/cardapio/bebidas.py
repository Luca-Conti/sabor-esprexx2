from modelos.cardapio.item_cardapio import Item_cardapio

class Bebidas(Item_cardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome