from datetime import datetime



WIDTH = 1280
HEIGHT = 640

# definicje klas
class Game:
    def __init__(self, background_active):
        # ustawiamy najważniejsze elementy, niektóre na stałe
        self.background_active = background_active
        self.background_position = (0, 0)
        self.game_start = False
        self.game_finish = False
        self.actual_room = 5
        self.start_time = None
        # grafiki na rozpoczęcie i zakończenie gry
        self.intro_canvas = Actor("intro-canvas.png")
        self.intro_canvas.pos = (640, -160)
        self.game_over_canvas = Actor("intro-gamover-canvas.png")
        self.intro_canvas.pos = (320, -160)

        # elementy związane z bohaterem
        self.floor_level = 460
        self.hero = Actor("character-right-01.png")
        self.hero.pos = (WIDTH / 2, self.floor_level)
        # wyznaczanie rozmiarow gracza
        self.hero.height = 256
        self.hero.width = 140
        self.hero.frame = 1
        self.animation_step = 15

        #słownik z opisami pomieszczeń
        self.rooms = rooms_in_game

        # klucze
        self.pocket = Actor("pocket.jpg")
        self.pocket.pos = (1000,100)
        self.keys_in_pocket = [key_00,key_01,key_02,key_03,key_04]

    def draw_intro(self):
        def draw_text(text, x_offset, y_offset, fontsize=20):
            dcreen.draw.text (
            text,
            (self.intro_canvas.x + x_offset, self.intro_canvas.y + y_offset),
            fontname = "ptsansnarrowbold",
            fontsize = fontsize,
            color = (187, 96, 191)
            )
        # wyswietlenie ekranu startowego
        self.intro_canvas.draw()
        animate(self.intro_canvas, pos=(640, 320), duration=0.3, tween = "linear")
        draw_text("Przygoda", -450, -200, fontsize=32)

        # wprowadzenie: przedstawienie histori gry, obsługa klawiszy
        story = (
            "Tu opisujemy swoja przygode "
            "ipsum dolor sit amet, consectetur adipiscing elit. Curabitur "
            "at arcu sollicitudin, elementum velit a, tempus erat. Quisque sed"
            "tortor id nibh ullamcorper dictum. Vivamus efficitur gravida mauris"
            "ut mattis. Fusce fringilla facilisis sagittis. In mi risus, pellentesque"
            "at sodales vitae, mattis vel nibh. Duis ac iaculis justo. Etiam a dolor eu"
            "\n\n"
            "klawisz 'Q' - koniec gry"
            "\n\n"
            "Spacja start gry"
        )
        screen.draw.text(
            story,
            (self.into_canvas.x - 450, self.intro_canwas.y - 160),
            width= 900,
            fontname = "ptsansnarrowregular",
            fontsize=20,
            color=(0,0,0)
        )
        # opis klawiszy kontrolnych
        draw_text("otwieranie drzwi", 200,-55)
        draw_text("chodzenie w lewo", 75,175)
        draw_text("podnoszenie", 220,175)
        draw_text("chodzenie w prawo", 330,175)

    def draw_pocket(self):
        self.pocket.draw()
        # ustalimy polozenie i odleglosci miedzy kluczami
        key_pos = [-200,-100,0,100,200]
        temp = 0
    # dla każedego klucza w liście kluczy
        for key in self.keys_in_pocket:
            pos = (self.pocket.x + key_pos[temp] - 45, self.pocket.y - 10)
            temp += 1
            if key.in_pocket:
                # jesli mamy klucz wyswietlamu goz pliku graficznego w konkretnej pozycji
                screen.blit (key.file_name, pos)
            else:
                screen.blit("question-mark.png", pos)

    def hero_move(self, direction):
        if direction == "right":
            # jeżeli jest to mozliwe przesuwamy postać
            if self.hero.x < WIDTH - self.hero.width:
               self.hero.x += self.animation_step
        if direction == "left":
            if self.hero.x > self.hero.width:
                self.hero.x -= self.animation_step

    # wstawiamy odpowiedni obraze animujacy ruch
    self.hero.image = f"character-{direction}-0{self.hero.frame}.png"
    #zwiekszamy numer obrazka co bedzie pozwornie wygladalo jak ruch
    self.hero.frame += 1
    if self.hero.frame > 8:
        # to wracamy do 1
        self.hero.frame = 1

    def upade_game(self):
        if not self.game_start and keyboard.space:
            self.game_start = True
            self.start_time = datatime.now()

        if keyboard.q:
            quit()

        if self.game_start:
            if keyboard.right:
                self.hero_move("right")
            if keyboard.left:
                self.hero_move("left")

    def update_game(self):
        """ ta metoda będzie wywoływana z funkcji update() programu głównego """
        screen.blit(self.background_active, self.background_position)

    def draw_scene(self):
        # rysujemy tło
        screen.blit(self.background_active, self.background_position)
        #rysujemy głównego bohatera
        if self.game_start:
            # narysuj torbe z kluczami
            self.draw_pocket()
            self.hero.draw()
        elif self.game_finish:
            pass
        else:
            self.draw_intro()


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

class Door:
    def __init__(self, room_number, door_position, next_room_number, open):
        self.room_number = room_number
        self.x_left_door = door_position
        self.x_right_door = door_position
        self.next_room_number = next_room_number
        self.open = open
    pass

class Room:
    def __init__(self, room_number, room_name, can_move_lr, file_name, doors=[]):
        self.room_number = room_number
        self.room_name = room_name
        self.can_move_lr = can_move_lr
        self.file_name = file_name
        self.doors = doors

    pass

# podstawowe zmienne
background_active = "corridor-01.jpg"

# tworzymy klucze, a jako *self* będą przypisane nazwy zmiennych key_
key_00 = Key("key-00.png", False, 11, 1025)
key_01 = Key("key-01.png", False, 17, 80)
key_02 = Key("key-02.png", False, 16, 850)
key_03 = Key("key-03.png", False, 4, 950)
key_04 = Key("key-04.png", False, 0, 370)


# tworzymy drzwi zgodnie z planem pomieszczeń
# domyślnie każde z drzwi będzie otwarte

door_00 = Door(0, 963, 5, True)
door_01 = Door(3, 962, 58, True)
door_02 = Door(5, 307, 15, True)
door_03 = Door(5, 967, 0, True)
door_04 = Door(6, 337, 11, True)
door_05 = Door(7, 932, 17, True)
door_06 = Door(8, 767, 3, True)
door_07 = Door(8, 327, 13, False)
door_08 = Door(11, 327, 6, True)
door_09 = Door(13, 327, 8, True)
door_10 = Door(15, 307, 5, True)
door_11 = Door(17, 932, 7, True)

# tworzymy opisy pomieszczen zgodnie z planem
room_00 = Room(0, "Biologia 01", 2, "biol-01.jpg", [door_00])
room_01 = Room(1, "Biologia02", 1, "biol-02.jpg")
room_03 = Room(3, "Sala Gimnastyczna 01", 2, "gym-01.jpg", [door_01])
room_04 = Room(4, "Sala Gimnastyczna 02", 1, "gym-02.jpg")
room_05 = Room(5, "Korytarz 01 lewy", 2, "corridor-01.jpg", [door_02, door_03])
room_06 = Room(6, "Korytarz 02", 3, "corridor-02.jpg", [door_04])
room_07 = Room(7, "Korytarz 03", 3, "corridor-03.jpg", [door_05])
room_08 = Room(8, "Korytarz 04 prawy", 1, "corridor-04.jpg", [door_06, door_07])
room_11 = Room(11, "WC", 0, "wc.jpg", [door_08])
room_13 = Room(13, "Aula", 0, "assembly-hall.jpg", [door_09])
room_15 = Room(15, "Matematyka 01", 2, "maths-01.jpg", [door_10])
room_16 = Room(16, "Matematyka 02", 1, "maths-02.jpg")
room_17 = Room(17, "Informatyka 01", 2, "computer-science-01.jpg", [door_11])
room_18 = Room(18, "Informatyka 02", 1, "computer-science-02.jpg")

# nastepnie tworzymy sł¸ownik odpowiadajacy układowi pomieszczen na mapie

room_in_game = {
    0: room_00,
    1: room_01,
    3: room_03,
    4: room_04,
    5: room_05,
    6: room_06,
    7: room_07,
    8: room_08,
    11: room_11,
    13: room_13,
    15: room_15,
    16: room_16,
    17: room_17,
    18: room_18,
}

# tworzymy zmienną gry
game = Game(background_active)

def update():
    game.update_game()

def draw():
    game.draw_scene()










