from modelos.restaurante import Restaurante
from colorama import Fore, Style
from modelos.cardapio.bebidas import Bebidas
from modelos.cardapio.prato import Prato
from modelos.cardapio.item_cardapio import Item_cardapio
beida_suco = Bebidas('suco de laranja', 5.0, 'grande')
comida_pazinho = Prato('pazinho', 1.5, 'pazinho' )
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 2.5)
restaurante_praca.receber_avaliacao('Emy', 2)
restaurante_praca.adicionar_bebida_no_cardapio(beida_suco)
restaurante_praca.adicionar_prato_no_cardapio(comida_pazinho)

def main():
    pass

if __name__ == '__main__':
    main()