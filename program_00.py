WIDTH = 1280 # szerokość okna
HEIGHT = 720 # wysokość okna

# definicje klas

class Game:
    def __init__(self, background_active):
        self.background_active = background_active
        self.background_psition =(0,0)

    def update():
        screen.blit(background_active,background_position) # metoda blit pozwala wyświetlić obrazy na ekranie
        #print(dir())  metoda ta pozwala na sprawdzenie czego jeszcze potrzebujemy aby gra działąłą poprawnie

class Key:
    def __init__(self, key_name, in_pocet, room_number, place_on_floor):
    # self oznacza * siebie przypisywane są z parametrów
        self.key_name = key_name
        self.in_pocet = in_pocet
        self.room_number = room_number
        self.place_on_floor = place_on_floor
    # na razie nie robimy nice
    pass


# podstawowe zmienne
background_active = "corridor-01.jpg"
background_position = (0,0) # sprawdz cos ię stanie dla wartości (10,30) lub (20, -40)
# tworzymy klucze, a jako self bedą przypisywane nazwy zmiennych key_

key_00 = Key("key-00.png", False, 1, 1025)
key_01 = Key("key-01.png", False, 16, 80)
key_02 = Key("key-02.png", False, 18, 850)
key_03 = Key("key-03.png", False, 11, 950)

# tworzymy zmienną gry
game = Game(background_active)




