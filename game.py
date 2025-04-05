import pygame

pygame.init()

chodi_doprava = [
    pygame.image.load('R1.png'),
    pygame.image.load('R2.png'),
    pygame.image.load('R3.png'),
    pygame.image.load('R4.png'),
    pygame.image.load('R5.png'),
    pygame.image.load('R6.png'),
    pygame.image.load('R7.png'),
    pygame.image.load('R8.png'),
    pygame.image.load('R9.png')
]
chodi_dolava = [
    pygame.image.load('L1.png'),
    pygame.image.load('L2.png'),
    pygame.image.load('L3.png'),
    pygame.image.load('L4.png'),
    pygame.image.load('L5.png'),
    pygame.image.load('L6.png'),
    pygame.image.load('L7.png'),
    pygame.image.load('L8.png'),
    pygame.image.load('L9.png')
]

vybuch = pygame.image.load('explosion.png')

#strela = pygame.mixer.Sound('cannon.wav')
#trefa = pygame.mixer.Sound('tresky.wav')


class charakter(object):

    def __init__(self, x, y, sirka_postavy, vyska_postavy):
        self.x = x
        self.y = y
        self.sirka_postavy = vyska_postavy
        self.vyska_postavy = sirka_postavy
        self.krok = 5
        self.vpravo = False
        self.vlavo = False
        self.pocet_krokov = 0
        self.skace = False
        self.pocet_skokov = 20
        self.stoji = True
        self.zivy = True

    def prekresli(self, okno):
        if self.pocet_krokov + 1 >= 27:
            self.pocet_krokov = 0

        if self.zivy:
            if not self.stoji:
                if self.vpravo:
                    okno.blit(chodi_doprava[hrac.pocet_krokov // 3], (self.x, self.y))
                    self.pocet_krokov += 1

                elif self.vlavo:
                    okno.blit(chodi_dolava[self.pocet_krokov // 3], (self.x, self.y))
                    self.pocet_krokov += 1

            else:
                if self.vpravo:
                    okno.blit(chodi_doprava[0], (self.x, self.y))
                else:
                    okno.blit(chodi_dolava[0], (self.x, self.y))
        else:
            okno.blit(vybuch, (self.x - 20, self.y - 20))
            okno.blit(lezi, (self.x, self.y))
            text_1 = font_1.render('LOSS! press r to restart', 1, (255, 0, 0))
            okno.blit(text_1, (80, vyska_pozadie // 2))


class vystrel(object):

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def prekresli(self, okno):
        okno.blit(bomba_obraz, (self.x, self.y))
        okno.blit(kanon, (0, 320))
        okno.blit(tabula, (15, 15))
        text = font.render('Score: ' + str(skore), 1, (0, 0, 0))
        okno.blit(text, (20, 30))


def prekresli_pozadie_hrac():
    okno.blit(pozadie, (0, 0))
    hrac.prekresli(okno)
    bomba.prekresli(okno)
    pygame.display.update()


sirka_pozadie = 600
vyska_pozadie = 377

okno = pygame.display.set_mode((sirka_pozadie, vyska_pozadie))
pygame.display.set_caption('Prva hra')

cas = pygame.time.Clock()

pozadie = pygame.image.load('bg.png')
lezi = pygame.image.load('dead.png')

tabula = pygame.image.load('image.png')
kanon = pygame.image.load('canon.png')
bomba_obraz = pygame.image.load('Bomba.png')

hrac = charakter(300, 290, 64, 64)
bomba = vystrel(90, 310, 2)
bezi = True
bomba_bezi = True

skore = 0
font = pygame.font.SysFont('comicsans', 17, True)
font_1 = pygame.font.SysFont('comicsans', 50, True)

tlacidla = pygame.key.get_pressed()

while bezi:
    cas.tick(54)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bezi = False

    tlacidla = pygame.key.get_pressed()

    if bomba.x < 605:
        bomba.x += bomba.krok

    elif bomba.krok < 20:
        bomba.x = 90
        bomba.krok += 0.25
        skore += 1

    else:
        bomba.x = 90

    #if bomba.x == 92 or bomba.x == 90:
        #strela.play()

    if tlacidla[pygame.K_LEFT] and hrac.x > hrac.krok + 90:
        hrac.x -= hrac.krok
        hrac.vlavo = True
        hrac.vpravo = False
        hrac.stoji = False

    elif tlacidla[pygame.K_RIGHT] and hrac.x < sirka_pozadie - hrac.krok - hrac.sirka_postavy:
        hrac.x += hrac.krok
        hrac.vlavo = False
        hrac.vpravo = True
        hrac.stoji = False

    else:
        hrac.stoji = True
        hrac.pocet_krokov = 0

    if tlacidla[pygame.K_SPACE]:
        hrac.skace = True

    if tlacidla[pygame.K_r] and hrac.zivy == False:
        hrac.krok = 5
        bomba.krok = 3
        hrac.zivy = True
        hrac.x = 300
        hrac.y = 290
        bomba.x = 90
        bomba.y = 310
        skore = 0

    if hrac.skace:
        if hrac.pocet_skokov >= -20:
            neg = 1
            if hrac.pocet_skokov < 0:
                neg = -1

            hrac.y -= (hrac.pocet_skokov ** 2) * 0.05 * neg
            hrac.pocet_skokov -= 1

        else:
            hrac.skace = False
            hrac.pocet_skokov = 20

    vzdialenost = ((hrac.x + 20 - bomba.x) ** 2 + (hrac.y + 20 - bomba.y) ** 2) ** 0.5

    if vzdialenost < 20:
        hrac.krok = 0
        bomba.krok = 0
        hrac.zivy = False
        hrac.y += 25
        bomba.x = -50
        #trefa.play()

    if hrac.y > 340:
        hrac.y = 310

    prekresli_pozadie_hrac()

pygame.quit()
