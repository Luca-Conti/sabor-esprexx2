from modelos.restaurante import Restaurante
from colorama import Fore, Style
from modelos.cardapio.item_cardapio import item_cardapio
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 2.5)
restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()