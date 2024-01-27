import pygame
import os
import random
import pygame.image

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (2, 136, 194)
GREY = (128, 128, 128)
BGCOLOR = (165, 85, 145)
FPS = 60
buttonrollx = 1000
buttonrolly = 50

buttonkupx = 1025
buttonkupy = 900
buttonnendturnx = 1200
buttonnendturny = 900

buttonhousex = 1025
buttonhousey = 700

buttonstatsx = 1700
buttonstatsy = 50

buttonbackx = 1700
buttonbacky = 900

textrollx = 1150
textrolly = 60
textroll1x = 1175
textroll1y = 60

BUTTONroll = pygame.Rect(buttonrollx, buttonrolly, 140, 60)
BUTTONkup = pygame.Rect(buttonkupx, buttonkupy, 140, 60)
BUTTONendturn = pygame.Rect(buttonnendturnx, buttonnendturny, 140, 60)
BUTTONhouse = pygame.Rect(buttonhousex, buttonhousey, 140, 60)
BUTTONstats = pygame.Rect(buttonstatsx, buttonstatsy, 140, 60)
BUTTONback = pygame.Rect(buttonbackx, buttonbacky, 140, 60)
WIDTH, HEIGHT = 1900, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Monopoly')

class Board:
    def __init__(self):
        self.board = []

class Player:
    def __init__(self, money, pos, x, y, id, wiezienie=0, ilemaszpol=0, ilestacji=0, wyjsciezwiezienia=0):
        self.money = money
        self.pos = pos
        self.x = x
        self.y = y
        self.id = id
        self.wiezienie= wiezienie
        self.ilemaszpol = ilemaszpol
        self.ilestacji = ilestacji
        self.wyjsciezwiezienia = wyjsciezwiezienia


class Pole:
    def __init__(self, price, x, y, szer, wys,  kolor, wlasnosc, nazwa='nazwapola',iloscdomow=0):
        self.price = price
        self.x = x
        self.y = y
        self.szer = szer
        self.wys = wys
        self.kolor = kolor
        self.wlasnosc = wlasnosc
        self.nazwa = nazwa
        self.iloscdomow = iloscdomow

class Game:
    def __init__(self, win):
        self.win = win
        self.board = Board()
        self.wynikrolki = 0
        self.buyshow = 10
        self.gracze = []
        self.gracze.append(Player(2000, 0, pole0.x + 10, pole0.y + 35, 1))
        self.gracze.append(Player(2000, 0, pole0.x + 50, pole0.y + 35, 2))
        self.tura = 1
        self.zmiana = 0
        self.zmienna1 = 0
        self.zmienna2 = 0
        self.x = 50
        self.y = 150
        self.x2 = 1400
        self.y2 = 150
        self.konieclicznik = 0
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.textp1money = self.font.render('2000', False, BLACK)
        self.textp2money = self.font.render('2000', False, BLACK)
        self.rollimg = pygame.image.load(os.path.join('Assets', 'roll.png'))
        self.rollimg = pygame.transform.scale(self.rollimg, (140, 60))
        self.kup = pygame.image.load(os.path.join('Assets', 'kupbutton.png'))
        self.kup = pygame.transform.scale(self.kup, (140, 60))
        self.niekup = pygame.image.load(os.path.join('Assets', 'endturn.png'))
        self.niekup = pygame.transform.scale(self.niekup, (140, 60))
        self.buyhouse = pygame.image.load(os.path.join('Assets', 'buyhouse.png'))
        self.buyhouse = pygame.transform.scale(self.buyhouse, (140, 60))
        self.domek = pygame.image.load(os.path.join('Assets', 'dom.png'))
        self.domek = pygame.transform.scale(self.domek, (30, 20))
        self.stats = pygame.image.load(os.path.join('Assets', 'stats.png'))
        self.stats = pygame.transform.scale(self.stats, (140, 60))
        self.back = pygame.image.load(os.path.join('Assets', 'back.png'))
        self.back = pygame.transform.scale(self.back, (140, 60))
        self.tlo = pygame.image.load(os.path.join('Assets', 'tlo.png'))
        self.tlo = pygame.transform.scale(self.tlo, (WIDTH, HEIGHT))
        self.like = pygame.image.load(os.path.join('Assets', 'like.png'))

        self.textroll = self.font.render(' = ', False, BLACK)
        self.textroll1 = self.font.render(' 1 ', False, BLACK)
        self.textroll2 = self.font.render(' 2 ', False, BLACK)
        self.textroll3 = self.font.render(' 3 ', False, BLACK)
        self.textroll4 = self.font.render(' 4 ', False, BLACK)
        self.textroll5 = self.font.render(' 5 ', False, BLACK)
        self.textroll6 = self.font.render(' 6 ', False, BLACK)
        self.textp1 = self.font.render('P1 money:', False, BLACK)
        self.textp2 = self.font.render('P2 money:', False, BLACK)
        self.textkup = self.font.render('Czy chcesz kupic za: ', False, BLACK)
        self.textgracz1 = self.font.render('Tura gracza: ', False, BLACK)
        self.wynikrolki = 0
        self.licznikroll = 0
        self.licznikendturn = 0
        self.ilerazy = self.font.render("x", False, BLACK)
        self.liczbadomownature = 0
        self.bluepola = 2
        self.licznikbluepola = 0
        self.greenpola = 3
        self.licznikgreenpola = 0
        self.pinkpola = 3
        self.licznikpinkpola = 0
        self.orangepola = 3
        self.licznikorangepola = 0
        self.redpola = 3
        self.licznikredpola = 0
        self.yellowpola = 3
        self.licznikyellowpola = 0
        self.brownpola = 3
        self.licznikbrownpola = 0
        self.blackpola = 2
        self.licznikblackpola = 0
        self.ilerazydodalodolisty = 0
        self.kupil = 0
        self.kupildom = 0
        self.niedom = 0
        self.event1 = 0
        self.event2 = 0
        self.chest1 = 0
        self.chest2 = 0
        self.tax1 = 0
        self.tax2 = 0
        self.przegrany = 0
        self.juztomasz = 0
        self.cena = 0
        self.ktostojuzma = 0
        self.zaplacone = 0
        self.start = 0
        self.posiada = self.font.render('posiada', False, BLACK)
        self.starttext = self.font.render('dostał 200 bo przeszedł przez start', False, BLACK)
        self.taxtext = self.font.render('zapłacił podatek w wysokości:', False, BLACK)
        self.gracz = self.font.render('gracz', False, BLACK)
        self.kupiltext = self.font.render('kupił pole nr', False, BLACK)
        self.dom = self.font.render('kupił dom na polu nr', False, BLACK)
        self.chesttext = self.font.render('Wydarzył się chest', False, BLACK)
        self.chest1text = self.font.render('Dostaje karte wyjścia z więzienia', False, BLACK)
        self.chest2text = self.font.render('Idzie na pole startowe', False, BLACK)
        self.eventtext = self.font.render('Wydarzył się event', False, BLACK)
        self.event1text = self.font.render('Dostaje 100 z banku', False, BLACK)
        self.event2text = self.font.render('Idzie na pole parking', False, BLACK)
        self.ktosjuztomatext = self.font.render('Ktoś juz posiada to pole', False, BLACK)
        self.moznakupic = self.font.render('Można kupić to pole', False, BLACK)
        self.juztomasztext = self.font.render('Już posiadasz to pole', False, BLACK)
        self.niemozeszdomutext = self.font.render('Nie możesz kupic domu', False, BLACK)
        self.wiezienietext = self.font.render('Jesteś w więzieniu', False, BLACK)
        self.zaplaciltext = self.font.render('Zapłacił', False, BLACK)
        self.koniec = self.font.render('Wygrał gracz ', False, BLACK)
        self.koniectext = self.font.render('Nie możesz kupić bo nie masz tyle pieniędzy ', False, BLACK)
        self.dlatext = self.font.render('dla', False, BLACK)
        self.red = self.font.render('Czerwony', False, BLACK)
        self.blue = self.font.render('Niebieski', False, BLACK)
        self.tax1text = self.font.render('200', False, BLACK)
        self.tax2text = self.font.render('300', False, BLACK)
        self.cyfra1 = self.font.render('1', False, BLACK)
        self.cyfra2 = self.font.render('2', False, BLACK)
        self.cyfra3 = self.font.render('3', False, BLACK)
        self.cyfra4 = self.font.render('4', False, BLACK)
        self.cyfra5 = self.font.render('5', False, BLACK)
        self.cyfra6 = self.font.render('6', False, BLACK)
        self.cyfra7 = self.font.render('7', False, BLACK)
        self.cyfra8 = self.font.render('8', False, BLACK)
        self.cyfra9 = self.font.render('9', False, BLACK)
        self.cyfra10 = self.font.render('10', False, BLACK)
        self.cyfra11 = self.font.render('11', False, BLACK)
        self.cyfra12 = self.font.render('12', False, BLACK)
        self.cyfra13 = self.font.render('13', False, BLACK)
        self.cyfra14 = self.font.render('14', False, BLACK)
        self.cyfra15 = self.font.render('15', False, BLACK)
        self.cyfra16 = self.font.render('16', False, BLACK)
        self.cyfra17 = self.font.render('17', False, BLACK)
        self.cyfra18 = self.font.render('18', False, BLACK)
        self.cyfra19 = self.font.render('19', False, BLACK)
        self.cyfra20 = self.font.render('20', False, BLACK)
        self.cyfra21 = self.font.render('21', False, BLACK)
        self.cyfra22 = self.font.render('22', False, BLACK)
        self.cyfra23 = self.font.render('23', False, BLACK)
        self.cyfra24 = self.font.render('24', False, BLACK)
        self.cyfra25 = self.font.render('25', False, BLACK)
        self.cyfra26 = self.font.render('26', False, BLACK)
        self.cyfra27 = self.font.render('27', False, BLACK)
        self.cyfra28 = self.font.render('28', False, BLACK)
        self.cyfra29 = self.font.render('29', False, BLACK)
        self.cyfra30 = self.font.render('30', False, BLACK)
        self.cyfra31 = self.font.render('31', False, BLACK)
        self.cyfra32 = self.font.render('32', False, BLACK)
        self.cyfra33 = self.font.render('33', False, BLACK)
        self.cyfra34 = self.font.render('34', False, BLACK)
        self.cyfra35 = self.font.render('35', False, BLACK)
        self.cyfra36 = self.font.render('36', False, BLACK)
        self.cyfra37 = self.font.render('37', False, BLACK)
        self.cyfra38 = self.font.render('38', False, BLACK)
        self.cyfra39 = self.font.render('39', False, BLACK)

    def drawboard(self, win):
        win.fill(BGCOLOR)
        WIN.blit(karta, (pole0.x, pole0.y))
        WIN.blit(karta1, (pole1.x, pole1.y))
        WIN.blit(karta2, (pole2.x, pole2.y))
        WIN.blit(karta3, (pole3.x, pole3.y))
        WIN.blit(karta4, (pole4.x, pole4.y))
        WIN.blit(karta5, (pole5.x, pole5.y))
        WIN.blit(karta6, (pole6.x, pole6.y))
        WIN.blit(karta7, (pole7.x, pole7.y))
        WIN.blit(karta8, (pole8.x, pole8.y))
        WIN.blit(karta9, (pole9.x, pole9.y))
        WIN.blit(karta10, (pole10.x, pole10.y))
        WIN.blit(karta11, (pole11.x, pole11.y))
        WIN.blit(karta12, (pole12.x, pole12.y))
        WIN.blit(karta13, (pole13.x, pole13.y))
        WIN.blit(karta14, (pole14.x, pole14.y))
        WIN.blit(karta15, (pole15.x, pole15.y))
        WIN.blit(karta16, (pole16.x, pole16.y))
        WIN.blit(karta17, (pole17.x, pole17.y))
        WIN.blit(karta18, (pole18.x, pole18.y))
        WIN.blit(karta19, (pole19.x, pole19.y))
        WIN.blit(karta20, (pole20.x, pole20.y))
        WIN.blit(karta21, (pole21.x, pole21.y))
        WIN.blit(karta22, (pole22.x, pole22.y))
        WIN.blit(karta23, (pole23.x, pole23.y))
        WIN.blit(karta24, (pole24.x, pole24.y))
        WIN.blit(karta25, (pole25.x, pole25.y))
        WIN.blit(karta26, (pole26.x, pole26.y))
        WIN.blit(karta27, (pole27.x, pole27.y))
        WIN.blit(karta28, (pole28.x, pole28.y))
        WIN.blit(karta29, (pole29.x, pole29.y))
        WIN.blit(karta30, (pole30.x, pole30.y))
        WIN.blit(karta31, (pole31.x, pole31.y))
        WIN.blit(karta32, (pole32.x, pole32.y))
        WIN.blit(karta33, (pole33.x, pole33.y))
        WIN.blit(karta34, (pole34.x, pole34.y))
        WIN.blit(karta35, (pole35.x, pole35.y))
        WIN.blit(karta36, (pole36.x, pole36.y))
        WIN.blit(karta37, (pole37.x, pole37.y))
        WIN.blit(karta38, (pole38.x, pole38.y))
        WIN.blit(karta39, (pole39.x, pole39.y))

        WIN.blit(self.kup, (buttonkupx, buttonkupy))
        WIN.blit(self.niekup, (buttonnendturnx, buttonnendturny))
        WIN.blit(self.buyhouse, (buttonhousex, buttonhousey))
        WIN.blit(self.stats, (buttonstatsx, buttonstatsy))
        if self.zmiana == 0:
            if self.wynikrolki == 1:
                WIN.blit(self.textroll1, (textroll1x, textroll1y))
            elif self.wynikrolki == 2:
                WIN.blit(self.textroll2, (textroll1x, textroll1y))
            elif self.wynikrolki == 3:
                WIN.blit(self.textroll3, (textroll1x, textroll1y))
            elif self.wynikrolki == 4:
                WIN.blit(self.textroll4, (textroll1x, textroll1y))
            elif self.wynikrolki == 5:
                WIN.blit(self.textroll5, (textroll1x, textroll1y))
            elif self.wynikrolki == 6:
                WIN.blit(self.textroll6, (textroll1x, textroll1y))

        WIN.blit(self.rollimg, (buttonrollx, buttonrolly))
        WIN.blit(self.textroll, (textrollx, textrolly))
        WIN.blit(self.textp1, (1000, 150))
        WIN.blit(self.textp2, (1300, 150))
        WIN.blit(self.textp1money, (1140, 150))
        WIN.blit(self.textp2money, (1440, 150))
        WIN.blit(self.textgracz1, (1260, 60))
        for gracz in self.gracze:
            if gracz.id == 1:
                WIN.blit(player1image, (gracz.x, gracz.y))
                self.textgracz2 = self.font.render('Czerwony', False, BLACK)
                self.textp1money = self.font.render(str(gracz.money), False, BLACK)

            elif gracz.id == 2:
                WIN.blit(player2image, (gracz.x, gracz.y))
                self.textgracz3 = self.font.render('Niebieski', False, BLACK)
                self.textp2money = self.font.render(str(gracz.money), False, BLACK)
        if self.tura == 1:
            WIN.blit(self.textgracz2, (1440, 60))
        elif self.tura == 2:
            WIN.blit(self.textgracz3, (1440, 60))

        for qwe in range(0, 40):
            if Lista[qwe].iloscdomow > 0:
                if Game.iledomownapolu(self, qwe) > 0:
                    if qwe > 10 and qwe < 20 or qwe > 30 and qwe < 40:
                        WIN.blit(self.domek, (Lista[qwe].x + 130, Lista[qwe].y))
                        WIN.blit(self.ilerazy, (Lista[qwe].x + 165, Lista[qwe].y - 10))
                    else:
                        WIN.blit(self.domek, (Lista[qwe].x, Lista[qwe].y - 20))
                        WIN.blit(self.ilerazy, (Lista[qwe].x + 35, Lista[qwe].y - 35))
                    if qwe > 10 and qwe < 20 or qwe > 30 and qwe < 40:
                        if Game.iledomownapolu(self, qwe) == 1:
                            WIN.blit(self.textroll1, (Lista[qwe].x + 180, Lista[qwe].y - 10))
                        elif Game.iledomownapolu(self, qwe) == 2:
                            WIN.blit(self.textroll2, (Lista[qwe].x + 180, Lista[qwe].y - 10))
                        elif Game.iledomownapolu(self, qwe) == 3:
                            WIN.blit(self.textroll3, (Lista[qwe].x + 180, Lista[qwe].y - 10))
                        elif Game.iledomownapolu(self, qwe) == 4:
                            WIN.blit(self.textroll4, (Lista[qwe].x + 180, Lista[qwe].y - 10))
                        elif Game.iledomownapolu(self, qwe) == 5:
                            WIN.blit(self.textroll4, (Lista[qwe].x + 180, Lista[qwe].y - 10))
                    else:
                        if Game.iledomownapolu(self, qwe) == 1:
                            WIN.blit(self.textroll1, (Lista[qwe].x + 50, Lista[qwe].y - 35))
                        elif Game.iledomownapolu(self, qwe) == 2:
                            WIN.blit(self.textroll2, (Lista[qwe].x + 50, Lista[qwe].y - 35))
                        elif Game.iledomownapolu(self, qwe) == 3:
                            WIN.blit(self.textroll3, (Lista[qwe].x + 50, Lista[qwe].y - 35))
                        elif Game.iledomownapolu(self, qwe) == 4:
                            WIN.blit(self.textroll4, (Lista[qwe].x + 50, Lista[qwe].y - 35))
                        elif Game.iledomownapolu(self, qwe) == 5:
                            WIN.blit(self.textroll5, (Lista[qwe].x + 50, Lista[qwe].y - 35))

            Game.obecnepole(self)
            Game.nazwapola(self)
            Game.wlascicielpola(self)
            Game.cenaza(self)
            WIN.blit(self.gracz, (400, 250))
            if self.tura == 1:
                WIN.blit(self.red, (500, 250))
            elif self.tura == 2:
                WIN.blit(self.blue, (500, 250))

            if self.kupil == 1:
                WIN.blit(self.kupiltext, (300, 350))
                WIN.blit(self.obecnepole, (475, 350))
                WIN.blit(self.nazwapola, (525, 350))

            if self.kupildom == 1:
                WIN.blit(self.dom, (300, 400))
                WIN.blit(self.obecnepole, (575, 400))
                WIN.blit(self.nazwapola, (625, 400))

            if self.chest1 == 1 or self.chest2 == 1:
                WIN.blit(self.chesttext, (300, 350))
                if self.chest1 == 1:
                    WIN.blit(self.chest1text, (300, 400))
                elif self.chest2 == 1:
                    WIN.blit(self.chest2text, (300, 400))
            elif self.event1 == 1 or self.event2 == 1:
                WIN.blit(self.eventtext, (300, 350))
                if self.event1 == 1:
                    WIN.blit(self.event1text, (300, 400))
                elif self.event2 == 1:
                    WIN.blit(self.event2text, (300, 400))

            if self.juztomasz >= 1:
                WIN.blit(self.juztomasztext, (300, 700))

            if self.ktostojuzma >= 1:
                if Lista[self.gracze[self.tura-1].pos].wlasnosc != 6:
                    pass
                elif Lista[self.gracze[self.tura - 1].pos].wlasnosc != 7:
                    pass
                else:
                    WIN.blit(self.ktosjuztomatext, (300, 700))

            if self.niedom >= 1:
                WIN.blit(self.niemozeszdomutext, (300, 750))

            if self.zaplacone >= 1:
                WIN.blit(self.zaplaciltext, (300, 550))
                WIN.blit(self.cena, (425, 550))
                WIN.blit(self.dlatext, (525, 550))
                WIN.blit(self.wlascicielpola, (575, 550))

            if self.tax1 >= 1 or self.tax2 >= 1:
                WIN.blit(self.taxtext, (300, 400))
                if self.tax1 >= 1:
                    WIN.blit(self.tax1text, (715, 400))
                if self.tax2 >= 1:
                    WIN.blit(self.tax2text, (715, 400))

            if self.start >= 1:
                WIN.blit(self.starttext, (300, 450))

            if self.gracze[self.tura-1].wiezienie > 0:
                WIN.blit(self.wiezienietext, (300, 450))

        if self.konieclicznik > 0:
            WIN.blit(self.koniectext,  (200, 450))

        if Game.koniecgry(self) != 0:
            if Game.koniecgry(self) == 1:
                Game.koniecplansza(self)
                WIN.blit(self.blue, (900, 100))
            if Game.koniecgry(self) == 2:
                Game.koniecplansza(self)
                WIN.blit(self.red, (900, 100))

    def bot(self):
        pass
        # miał być, może będzie ale na razie nie ma :(
        # na razie też tylko 2 graczy, może jeszcze zrobię żeby bylo max 4 i wybór ilu ma być

    def koniecplansza(self):
        WIN.fill(BGCOLOR)
        WIN.blit(self.like, (500, 150))
        WIN.blit(self.koniec, (700, 100))
        pygame.display.update()

    def koniecgry(self):
        if self.gracze[self.tura-1].money < 0:
            return self.tura

    def statyshow(self):
        for q in range(0, 40):
            if Lista[q].wlasnosc == 1:
                Game.cenaza(self)
                self.poleteraz = self.font.render(str(Lista[q].nazwa +' - '), False, BLACK)
                WIN.blit(self.poleteraz, (self.x, self.y))
                WIN.blit(self.cena, (self.x+200, self.y))
                self.y += 50
            elif Lista[q].wlasnosc == 2:
                Game.cenaza(self)
                self.poleteraz2 = self.font.render(str(Lista[q].nazwa + ' - '), False, BLACK)
                WIN.blit(self.poleteraz2, (self.x2, self.y2))
                WIN.blit(self.cena, (self.x2+200, self.y))
                self.y2 += 50

    def stats(self):
        self.y = 150
        self.y2 = 150
        WIN.fill(BGCOLOR)
        WIN.blit(self.back, (buttonbackx, buttonbacky))
        WIN.blit(self.red, (50, 50))
        WIN.blit(self.blue, (1500, 50))
        WIN.blit(self.posiada, (200, 50))
        WIN.blit(self.posiada, (1650, 50))
        Game.statyshow(self)
        pygame.display.update()


    def obecnepole(self):
        self.obecnepole = self.font.render(str(self.gracze[self.tura-1].pos), False, BLACK)
        return self.obecnepole

    def nazwapola(self):
        self.nazwapola = self.font.render(Lista[self.gracze[self.tura-1].pos].nazwa, False, BLACK)
        return self.nazwapola

    def wlascicielpola(self):
        if Lista[self.gracze[self.tura-1].pos].wlasnosc == 1:
            self.wlascicielpola = self.red
        elif Lista[self.gracze[self.tura-1].pos].wlasnosc == 2:
            self.wlascicielpola = self.blue
        return self.wlascicielpola

    def cenaza(self):
        self.cena = self.font.render(str(Game.cenazawejscie(self, self.tura)), False, BLACK)
        return self.cena

    def checkpola(self, id):
        id -= 1
        if Lista[self.gracze[id].pos].wlasnosc == 1 or 2:
            if self.gracze[id].id == 1 and Lista[self.gracze[id].pos].wlasnosc == 2:
                return 1
            elif self.gracze[id].id == 2 and Lista[self.gracze[id].pos].wlasnosc == 1:
                return 2
            elif self.gracze[id].id == 1 and Lista[self.gracze[id].pos].wlasnosc == 1:
                Game.house(self)
            elif self.gracze[id].id == 2 and Lista[self.gracze[id].pos].wlasnosc == 2:
                Game.house(self)

    def cenazawejscie(self, id):
        id -= 1
        cena = 0
        if Lista[self.gracze[id].pos].wlasnosc == 1:
            idwlasciciela = 1
        else:
            idwlasciciela = 2

        if self.gracze[id].pos == 5 or self.gracze[id].pos == 15 or self.gracze[id].pos == 25 or self.gracze[id].pos == 35:
            cena = 100 * self.gracze[idwlasciciela-1].ilestacji
        else:
            cena = Lista[self.gracze[id].pos].price / 2
            for dom in range(Lista[self.gracze[id].pos].iloscdomow):
                cena *= 1.3
        return cena

    def iledomownapolu(self, numer):
        id = self.tura - 1
        if Lista[numer].iloscdomow == 1:
            return 1
        elif Lista[numer].iloscdomow == 2:
            return 2
        elif Lista[numer].iloscdomow == 3:
            return 3
        elif Lista[numer].iloscdomow == 4:
            return 4
        elif Lista[numer].iloscdomow == 5:
            return 5
        if Lista[numer].iloscdomow == 0:
            return 0

    def zerowanie(self):
        self.kupil = 0
        self.kupildom = 0
        self.event1 = 0
        self.event2 = 0
        self.chest1 = 0
        self.chest2 = 0
        self.ktostojuzma = 0
        self.juztomasz = 0
        self.niedom = 0
        self.zaplacone = 0
        self.tax1 = 0
        self.tax2 = 0
        self.start = 0
        self.konieclicznik = 0


    def house(self):
        id = self.tura - 1
        cenazadomek = Lista[self.gracze[id].pos].price / 3

        for domek in range(Lista[self.gracze[id].pos].iloscdomow):
            cenazadomek *= 1.2

        Game.podliczpola(self)

        if Lista[self.gracze[id].pos].wlasnosc == self.tura and Lista[self.gracze[id].pos].iloscdomow < 5:
            if self.liczbadomownature < 1:
                if Game.czymaszwszystkiekolory(self):
                    Lista[self.gracze[id].pos].iloscdomow += 1
                    self.gracze[id].money -= int(cenazadomek)
                    self.liczbadomownature += 1
                    self.kupildom += 1
                else:
                    self.niedom += 1

        Game.zerowanielicznikowdomkow(self)

    def placenie(self, id):
        id -= 1
        idwlasciciela = 0
        cena = Game.cenazawejscie(self, self.tura)
        self.gracze[id].money -= cena
        if Lista[self.gracze[id].pos].wlasnosc == 1:
            idwlasciciela = 1
        elif Lista[self.gracze[id].pos].wlasnosc == 2:
            idwlasciciela = 2
        self.gracze[idwlasciciela-1].money += cena
        self.zaplacone += 1

    def chest(self):
        id = self.tura - 1
        rollchest = random.randint(1, 2)
        if rollchest == 1:
            self.gracze[id].wyjsciezwiezienia = 1
            self.chest1 += 1
        elif rollchest == 2:
            x = 40 - self.gracze[id].pos
            Game.playermove(self, x, self.tura)
            self.chest2 += 1

    def event(self):
        id = self.tura - 1
        rollevent = random.randint(1, 2)
        if rollevent == 1:
            self.gracze[id].money += 100
            self.event1 += 1
        elif rollevent == 2:
            self.event2 += 1
            if self.gracze[id].pos > 20:
                self.gracze[id].pos = 20
                x = 20 + self.gracze[id].pos
            else:
                self.gracze[id].pos = 20
                x = 20 - self.gracze[id].pos
            Game.playermove(self, x, self.tura)

    def wiezienie(self):
        id = self.tura - 1
        if self.gracze[id].wyjsciezwiezienia == 1:
            self.gracze[id].wyjsciezwiezienia = 0
        else:
            self.gracze[id].wiezienie += 1
            if self.gracze[id].wiezienie < 4:
                if self.wynikrolki == 6:
                    Game.playermove(self, 6, id)
                    self.gracze[id].wiezienie = 0
            else:
                self.gracze[id].wiezienie = 0

    def kupowanie(self):
        id = self.tura-1
        cena = Lista[self.gracze[id].pos].price
        if (self.gracze[id].money - cena) > 0:
            if self.tura == Lista[self.gracze[id].pos].wlasnosc:
                self.juztomasz += 1
            elif Lista[self.gracze[id].pos].wlasnosc == 0:
                self.gracze[id].money -= cena
                self.kupil += 1
                Lista[self.gracze[id].pos].wlasnosc = self.tura
                self.gracze[id].ilemaszpol += 1
                if self.gracze[id].pos == 5 or self.gracze[id].pos == 15 or self.gracze[id].pos == 25 or self.gracze[
                    id].pos == 35:
                    self.gracze[id].ilestacji += 1
            elif Lista[self.gracze[id].pos].wlasnosc != 5:
                self.ktostojuzma += 1
        else:
            self.konieclicznik = 1

    def zerowanielicznikowdomkow(self):
        self.licznikbluepola = 0
        self.licznikgreenpola = 0
        self.licznikpinkpola = 0
        self.licznikorangepola = 0
        self.licznikredpola = 0
        self.licznikyellowpola = 0
        self.licznikbrownpola = 0
        self.licznikblackpola = 0

    def podliczpola(self):
        for kolor in range(0, 40):
            if Lista[kolor].kolor == 11 and Lista[kolor].wlasnosc == self.tura:
                self.licznikbluepola += 1
            elif Lista[kolor].kolor == 12 and Lista[kolor].wlasnosc == self.tura:
                self.licznikgreenpola += 1
            elif Lista[kolor].kolor == 13 and Lista[kolor].wlasnosc == self.tura:
                self.licznikpinkpola += 1
            elif Lista[kolor].kolor == 14 and Lista[kolor].wlasnosc == self.tura:
                self.licznikorangepola += 1
            elif Lista[kolor].kolor == 15 and Lista[kolor].wlasnosc == self.tura:
                self.licznikredpola += 1
            elif Lista[kolor].kolor == 16 and Lista[kolor].wlasnosc == self.tura:
                self.licznikyellowpola += 1
            elif Lista[kolor].kolor == 17 and Lista[kolor].wlasnosc == self.tura:
                self.licznikbrownpola += 1
            elif Lista[kolor].kolor == 18 and Lista[kolor].wlasnosc == self.tura:
                self.licznikblackpola += 1

    def czymaszwszystkiekolory(self):
        id = self.tura - 1
        if Lista[self.gracze[id].pos].kolor == 11 and self.licznikbluepola == self.bluepola:
            return True
        elif Lista[self.gracze[id].pos].kolor == 12 and self.licznikgreenpola == self.greenpola:
            return True
        elif Lista[self.gracze[id].pos].kolor == 13 and self.licznikpinkpola == self.pinkpola:
            return True
        elif Lista[self.gracze[id].pos].kolor == 14 and self.licznikorangepola == self.orangepola:
            return True
        elif Lista[self.gracze[id].pos].kolor == 15 and self.licznikredpola == self.redpola:
            return True
        elif Lista[self.gracze[id].pos].kolor == 16 and self.licznikyellowpola == self.yellowpola:
            return True
        elif Lista[self.gracze[id].pos].kolor == 17 and self.licznikbrownpola == self.brownpola:
            return True
        elif Lista[self.gracze[id].pos].kolor == 18 and self.licznikblackpola == self.blackpola:
            return True

    def akcja(self):
        if Game.checkpola(self, self.tura) == 1:
            Game.placenie(self, 1)
        elif Game.checkpola(self, self.tura) == 2:
            Game.placenie(self, 2)
        if Lista[self.gracze[self.tura-1].pos].wlasnosc == 6:
            Game.chest(self)
        elif Lista[self.gracze[self.tura-1].pos].wlasnosc == 7:
            Game.event(self)

    def playermove(self, dice, id):
        id -= 1
        self.gracze[id].pos += dice

        if self.gracze[id].pos == 4:
            self.gracze[id].money -= 200
            self.tax1 += 1
        if self.gracze[id].pos == 38:
            self.gracze[id].money -= 300
            self.tax2 += 1
        if self.gracze[id].pos > 39:
            self.gracze[id].pos = 0 + self.gracze[id].pos % 40
            self.gracze[id].money += 200
            self.start += 1

        if self.gracze[id].pos == 30:
            self.gracze[id].pos = 10
            Game.wiezienie(self)

        if self.gracze[id].pos == 0 or self.gracze[id].pos == 20:
            self.gracze[id].x = Lista[self.gracze[id].pos].x + 5
            self.gracze[id].y = Lista[self.gracze[id].pos].y + 35
        elif self.gracze[id].pos == 10:
            self.gracze[id].x = Lista[self.gracze[id].pos].x + 5
            self.gracze[id].y = Lista[self.gracze[id].pos].y + 70
            if self.gracze[id].wiezienie == 1:
                self.gracze[id].y -= 50
        elif 0 < self.gracze[id].pos < 10:
            self.gracze[id].x = Lista[self.gracze[id].pos].x+5
            self.gracze[id].y = Lista[self.gracze[id].pos].y+70

        elif 10 < self.gracze[id].pos < 20:
            self.gracze[id].x = Lista[self.gracze[id].pos].x + 20
            self.gracze[id].y = Lista[self.gracze[id].pos].y + 5
        elif 20 < self.gracze[id].pos < 30:
            self.gracze[id].x = Lista[self.gracze[id].pos].x + 5
            self.gracze[id].y = Lista[self.gracze[id].pos].y + 40
        elif 30 < self.gracze[id].pos < 40:
            self.gracze[id].x = Lista[self.gracze[id].pos].x + 70
            self.gracze[id].y = Lista[self.gracze[id].pos].y + 5
        if self.gracze[id].id == 2:
            if 0 <= self.gracze[id].pos < 11 or 19 < self.gracze[id].pos < 31:
                self.gracze[id].x += 35
            else:
                self.gracze[id].y += 35

        Game.akcja(self)

    def swap(self):
        Game.zerowanie(self)
        self.zmiana = 1
        if self.licznikendturn == self.licznikroll - 1:
            self.licznikendturn += 1
            if self.tura == 1:
                self.tura = 2
                return self.tura
            elif self.tura == 2:
                self.tura = 1
                return self.tura
        self.liczbadomownature = 0


    def diceroll(self):
        self.zmiana = 0
        if self.licznikroll == self.licznikendturn:
            self.licznikroll += 1
            rollwynik = random.randint(1, 6)
            #rollwynik = 1
            if rollwynik == 1:
                self.wynikrolki = 1
            elif rollwynik == 2:
                self.wynikrolki = 2
            elif rollwynik == 3:
                self.wynikrolki = 3
            elif rollwynik == 4:
                self.wynikrolki = 4
            elif rollwynik == 5:
                self.wynikrolki = 5
            elif rollwynik == 6:
                self.wynikrolki = 6
            if self.gracze[self.tura-1].wiezienie == 0:
                Game.playermove(self, self.wynikrolki, self.tura)
                return self.wynikrolki
            else:
                Game.wiezienie(self)
            return self.wynikrolki

    def update(self):
        self.drawboard(self.win)
        pygame.display.update()


karta = pygame.image.load(os.path.join('Assets', 'start.png'))
karta = pygame.transform.scale(karta, (125, 125))
karta1 = pygame.image.load(os.path.join('Assets', 'Ukraina.png'))
karta1 = pygame.transform.scale(karta1, (75, 125))
karta2 = pygame.image.load(os.path.join('Assets', 'chest.png'))
karta2 = pygame.transform.scale(karta2, (75, 125))
karta3 = pygame.image.load(os.path.join('Assets', 'Bialorus.png'))
karta3 = pygame.transform.scale(karta3, (75, 125))
karta4 = pygame.image.load(os.path.join('Assets', 'Tax200.png'))
karta4 = pygame.transform.scale(karta4, (75, 125))
karta5 = pygame.image.load(os.path.join('Assets', 'Stacja.png'))
karta5 = pygame.transform.scale(karta5, (75, 125))
karta6 = pygame.image.load(os.path.join('Assets', 'Slowacja.png'))
karta6 = pygame.transform.scale(karta6, (75, 125))
karta7 = pygame.image.load(os.path.join('Assets', 'question.png'))
karta7 = pygame.transform.scale(karta7, (75, 125))
karta8 = pygame.image.load(os.path.join('Assets', 'Grecja.png'))
karta8 = pygame.transform.scale(karta8, (75, 125))
karta9 = pygame.image.load(os.path.join('Assets', 'Portugalia.png'))
karta9 = pygame.transform.scale(karta9, (75, 125))
karta10 = pygame.image.load(os.path.join('Assets', 'jail.png'))
karta10 = pygame.transform.scale(karta10, (125, 125))
karta11 = pygame.image.load(os.path.join('Assets', 'Hiszpania.png'))
karta11 = pygame.transform.scale(karta11, (75, 125))
karta11 = pygame.transform.rotate(karta11, 270)
karta12 = pygame.image.load(os.path.join('Assets', 'Elektrownia.png'))
karta12 = pygame.transform.scale(karta12, (75, 125))
karta12 = pygame.transform.rotate(karta12, 270)
karta13 = pygame.image.load(os.path.join('Assets', 'Polska.png'))
karta13 = pygame.transform.scale(karta13, (75, 125))
karta13 = pygame.transform.rotate(karta13, 270)
karta14 = pygame.image.load(os.path.join('Assets', 'Irlandia.png'))
karta14 = pygame.transform.scale(karta14, (75, 125))
karta14 = pygame.transform.rotate(karta14, 270)
karta15 = pygame.image.load(os.path.join('Assets', 'Stacja.png'))
karta15 = pygame.transform.scale(karta15, (75, 125))
karta15 = pygame.transform.rotate(karta15, 270)
karta16 = pygame.image.load(os.path.join('Assets', 'Czechy.png'))
karta16 = pygame.transform.scale(karta16, (75, 125))
karta16 = pygame.transform.rotate(karta16, 270)
karta17 = pygame.image.load(os.path.join('Assets', 'chest.png'))
karta17 = pygame.transform.scale(karta17, (75, 125))
karta17 = pygame.transform.rotate(karta17, 270)
karta18 = pygame.image.load(os.path.join('Assets', 'Austria.png'))
karta18 = pygame.transform.scale(karta18, (75, 125))
karta18 = pygame.transform.rotate(karta18, 270)
karta19 = pygame.image.load(os.path.join('Assets', 'Rosja.png'))
karta19 = pygame.transform.scale(karta19, (75, 125))
karta19 = pygame.transform.rotate(karta19, 270)
karta20 = pygame.image.load(os.path.join('Assets', 'parking.png'))
karta20 = pygame.transform.scale(karta20, (125, 125))
karta21 = pygame.image.load(os.path.join('Assets', 'Szwecja.png'))
karta21 = pygame.transform.scale(karta21, (75, 125))
karta22 = pygame.image.load(os.path.join('Assets', 'question.png'))
karta22 = pygame.transform.scale(karta22, (75, 125))
karta23 = pygame.image.load(os.path.join('Assets', 'Niemcy.png'))
karta23 = pygame.transform.scale(karta23, (75, 125))
karta24 = pygame.image.load(os.path.join('Assets', 'Wlochy.png'))
karta24 = pygame.transform.scale(karta24, (75, 125))
karta25 = pygame.image.load(os.path.join('Assets', 'stacja.png'))
karta25 = pygame.transform.scale(karta25, (75, 125))
karta26 = pygame.image.load(os.path.join('Assets', 'Belgia.png'))
karta26 = pygame.transform.scale(karta26, (75, 125))
karta27 = pygame.image.load(os.path.join('Assets', 'Francja.png'))
karta27 = pygame.transform.scale(karta27, (75, 125))
karta28 = pygame.image.load(os.path.join('Assets', 'Wodociagi.png'))
karta28 = pygame.transform.scale(karta28, (75, 125))
karta29 = pygame.image.load(os.path.join('Assets', 'Cypr.png'))
karta29 = pygame.transform.scale(karta29, (75, 125))
karta30 = pygame.image.load(os.path.join('Assets', 'gotojail.png'))
karta30 = pygame.transform.scale(karta30, (125, 125))
karta31 = pygame.image.load(os.path.join('Assets', 'Finlandia.png'))
karta31 = pygame.transform.scale(karta31, (75, 125))
karta31 = pygame.transform.rotate(karta31, 90)
karta32 = pygame.image.load(os.path.join('Assets', 'Dania.png'))
karta32 = pygame.transform.scale(karta32, (75, 125))
karta32 = pygame.transform.rotate(karta32, 90)
karta33 = pygame.image.load(os.path.join('Assets', 'chest.png'))
karta33 = pygame.transform.scale(karta33, (75, 125))
karta33 = pygame.transform.rotate(karta33, 90)
karta34 = pygame.image.load(os.path.join('Assets', 'Anglia.png'))
karta34 = pygame.transform.scale(karta34, (75, 125))
karta34 = pygame.transform.rotate(karta34, 90)
karta35 = pygame.image.load(os.path.join('Assets', 'Stacja.png'))
karta35 = pygame.transform.scale(karta35, (75, 125))
karta35 = pygame.transform.rotate(karta35, 90)
karta36 = pygame.image.load(os.path.join('Assets', 'question.png'))
karta36 = pygame.transform.scale(karta36, (75, 125))
karta36 = pygame.transform.rotate(karta36, 90)
karta37 = pygame.image.load(os.path.join('Assets', 'Luksemburg.png'))
karta37 = pygame.transform.scale(karta37, (75, 125))
karta37 = pygame.transform.rotate(karta37, 90)
karta38 = pygame.image.load(os.path.join('Assets', 'Tax300.png'))
karta38 = pygame.transform.scale(karta38, (75, 125))
karta38 = pygame.transform.rotate(karta38, 90)
karta39 = pygame.image.load(os.path.join('Assets', 'Szwajcaria.png'))
karta39 = pygame.transform.scale(karta39, (75, 125))
karta39 = pygame.transform.rotate(karta39, 90)

player1image = pygame.image.load(os.path.join('Assets', 'player1.png'))
player1image = pygame.transform.scale(player1image, (30, 30))
player2image = pygame.image.load(os.path.join('Assets', 'player2.png'))
player2image = pygame.transform.scale(player2image, (30, 30))

pole0 = Pole(0, 845, 848, 125, 125, 10, 5)
pole1 = Pole(100, 772, 848, 75, 125, 11, 0, 'Ukraina')
pole2 = Pole(0, 697, 848, 75, 125, 10, 6)
pole3 = Pole(150, 622, 848, 75, 125, 11, 0, 'Białoruś')
pole4 = Pole(0, 547, 848, 75, 125, 10, 5)
pole5 = Pole(400, 472, 848, 75, 125, 19, 0, 'Stacja1')
pole6 = Pole(200, 397, 848, 75, 125, 12,  0, 'Słowacja')
pole7 = Pole(0, 322, 848, 75, 125, 10, 7)
pole8 = Pole(150, 247, 848, 75, 125, 12, 0, 'Grecja')
pole9 = Pole(300, 172, 848, 75, 125, 12,  0, 'Portugalia')
pole10 = Pole(0, 48, 850, 125, 125, 10, 5)
pole11 = Pole(250, 48, 775, 75, 125, 13, 0, 'Hiszpania')
pole12 = Pole(200, 48, 700, 75, 125, 20, 0, 'Elektrownia')
pole13 = Pole(350, 48, 625, 75, 125, 13, 0, 'Polska')
pole14 = Pole(200, 48, 550, 75, 125, 13, 0, 'Irlandia')
pole15 = Pole(400, 48, 475, 75, 125, 19,  0, 'Stacja2')
pole16 = Pole(250, 48, 400, 75, 125, 14, 0, 'Czechy')
pole17 = Pole(0, 48, 325, 75, 125, 10, 6)
pole18 = Pole(300, 48, 250, 75, 125, 14, 0, 'Austria')
pole19 = Pole(400, 48, 175, 75, 125, 14, 0, 'Rosja')
pole20 = Pole(0, 48, 50, 125, 125, 10, 5)
pole21 = Pole(300, 172, 50, 75, 125, 15, 0, 'Szwecja')
pole22 = Pole(0, 247, 50, 75, 125, 10, 5)
pole23 = Pole(400, 322, 50, 75, 125, 15, 0, 'Niemcy')
pole24 = Pole(350, 397, 50, 75, 125, 15, 0, 'Włochy')
pole25 = Pole(400, 472, 50, 75, 125, 19,  0, 'Stacja3')
pole26 = Pole(350, 547, 50, 75, 125, 16, 0, 'Belgia')
pole27 = Pole(450, 622, 50, 75, 125, 16, 0, 'Francja')
pole28 = Pole(250, 697, 50, 75, 125, 20, 0, 'Wodociągi')
pole29 = Pole(300, 772, 50, 75, 125, 16, 0, 'Cypr')
pole30 = Pole(0, 847, 50, 125, 125, 10, 5)
pole31 = Pole(400, 847, 175, 75, 125, 17, 0, 'Finlandia')
pole32 = Pole(450, 847, 250, 75, 125, 17, 0, 'Dania')
pole33 = Pole(0, 847, 325, 75, 125, 10, 6)
pole34 = Pole(400, 847, 400, 75, 125, 17, 0, 'Anglia')
pole35 = Pole(400, 847, 475, 75, 125, 19, 0, 'Stacja4')
pole36 = Pole(0, 847, 550, 75, 125, 10, 7)
pole37 = Pole(450, 847, 625, 75, 125, 18, 0, 'Luksemburg')
pole38 = Pole(0, 847, 700, 75, 125, 10, 5)
pole39 = Pole(500, 847, 775, 75, 125, 18, 0, 'Szwajcaria')

Lista = []
Lista.append(pole0)
Lista.append(pole1)
Lista.append(pole2)
Lista.append(pole3)
Lista.append(pole4)
Lista.append(pole5)
Lista.append(pole6)
Lista.append(pole7)
Lista.append(pole8)
Lista.append(pole9)
Lista.append(pole10)
Lista.append(pole11)
Lista.append(pole12)
Lista.append(pole13)
Lista.append(pole14)
Lista.append(pole15)
Lista.append(pole16)
Lista.append(pole17)
Lista.append(pole18)
Lista.append(pole19)
Lista.append(pole20)
Lista.append(pole21)
Lista.append(pole22)
Lista.append(pole23)
Lista.append(pole24)
Lista.append(pole25)
Lista.append(pole26)
Lista.append(pole27)
Lista.append(pole28)
Lista.append(pole29)
Lista.append(pole30)
Lista.append(pole31)
Lista.append(pole32)
Lista.append(pole33)
Lista.append(pole34)
Lista.append(pole35)
Lista.append(pole36)
Lista.append(pole37)
Lista.append(pole38)
Lista.append(pole39)

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    licznik = 0
    while run:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUTTONroll.collidepoint(mouse_pos):
                    Game.diceroll(game)
                if BUTTONkup.collidepoint(mouse_pos):
                    Game.kupowanie(game)
                if BUTTONendturn.collidepoint(mouse_pos):
                    Game.swap(game)
                if BUTTONhouse.collidepoint(mouse_pos):
                    Game.house(game)
                if BUTTONstats.collidepoint(mouse_pos):
                    licznik += 1
                    Game.stats(game)
                if BUTTONback.collidepoint(mouse_pos):
                    licznik = 0

        if licznik == 0:
            game.update()
    pygame.quit()
main()
