WIDTH = 1280
HEIGHT = 640

# definicje klas
class Game:
    def __init__(self, background_active):
        # ustawiamy najważniejsze elementy, niektóre na stałe
        self.background_active = background_active
        self.background_position = (0, 0)

    def update_game(self):
        """ ta metoda będzie wywoływana z funkcji update() programu głównego """
        screen.blit(self.background_active, self.background_position)

class Key:
    def __init__(self, key_name, in_pocket, room_number, place_on_floor):
        """ self oznacza *siebie samego* - czyli konkretny klucz """
        # te właściwości obiektu *self* przepisywane są z parametrów
        self.key_name = key_name
        self.in_pocket = in_pocket
        self.room_number = room_number
        self.place_on_floor = place_on_floor

    # na razie nie robimy nic
    pass

# podstawowe zmienne
background_active = "corridor-01.jpg"

# tworzymy klucze, a jako *self* będą przypisane nazwy zmiennych key_
key_00 = Key("key-00.png", False, 11, 1025)
key_01 = Key("key-01.png", False, 17, 80)
key_02 = Key("key-02.png", False, 16, 850)
key_03 = Key("key-03.png", False, 4, 950)
key_04 = Key("key-04.png", False, 0, 370)

# tworzymy zmienną gry
game = Game(background_active)

def update():
    game.update_game()