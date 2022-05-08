from Pygame.bezier_curve.obj_class import *
import time
import os


def init(n, points):
    rang = [[] for i in range(n - 1)]
    flat = []

    for i in range(n - 1):
        pi = points[i]
        pii = points[i + 1]
        rang[0].append(Ligne(pi, pii))

    for k in range(n - 2):
        for i in range(n - 2 - k):
            pi = rang[k][i].pt
            pii = rang[k][i + 1].pt
            rang[k + 1].append(Ligne(pi, pii))

    [[flat.append(ligne) for ligne in lignes] for lignes in rang]
    return rang, flat


def save(surface, doc_name):

    path = 'C:/Users/simon/Documents/IPSA/A2/python/Pygame/bezier_curve/'

    if doc_name not in os.listdir(path):
        os.mkdir(doc_name)
    else:
        os.chdir(path + doc_name)
        pygame.image.save(surface, str(round(time.time(), 1)) + ".jpeg")


# ----------------------------------------------------------------------------------------------------------------------
# initialisation constante
H = 600
L = 400

blanc = (255, 255, 255)
gris = (150, 150, 150)
noir = (0, 0, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)
vert = (0, 255, 0)

# initialisation fenetre
pygame.init()
pygame.display.set_caption("Bezier curve")
surface = pygame.display.set_mode((H, L))

# initialisation environnement
n = 2
points = [Point(200, 200, surface),
          Point(400, 200, surface)]

rang, flat = init(n, points)

# boucle infinie
launched = 1
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = 0

    surface.fill(noir)

    if pygame.mouse.get_pressed()[2]:
        x, y = pygame.mouse.get_pos()

        points.append(Point(x, y, surface))
        n += 1

        rang, flat = init(n, points)
        time.sleep(0.1)

    for point in points:
        point.update()

    for ligne in flat:
        ligne.update()
        ligne.show()

    rang[-1][0].pt.show(color=rouge)

    save(surface, "1")

    pygame.display.flip()
