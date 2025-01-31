import flet as ft
import random as rd
import numpy as np

#Cette fonction renvoie un bool indiquant si le board est atteignable.
def is_reachable(given_board):
    assert type(given_board)==np.ndarray or type(given_board)==list, "il faut un tableau numpy ou une liste"
    #on commence par convertir tout cela en un tableau array linéaire de 8 cases
    board = np.array([0 for i in range(8)])
    k=0
    given_board2=given_board.copy() #pour éviter les effets colatéraux
    if type(given_board2)==np.ndarray and given_board2.shape==(3,3) :
        given_board2.reshape(9)
    elif type(given_board2)==list :
        given_board2=np.array(given_board2)
    for i in range(9):
        a=given_board2[i]
        if a!=0:
            board[k]=a
            k+=1
    
    #maintenant, on calcule la signature
    #Pour épargner au code des calculs sur des floats, on préfère faire des batteries de test.
    epsilon=1
    for i in range(1,8):
        for j in range(i+1,9):
            sigmai=board[i-1]
            sigmaj=board[j-1]
            if ((i<j and sigmai>sigmaj) or (i>j and sigmai<sigmaj)):
                epsilon*=(-1)
    #On conclut
    if epsilon==1:
        return True
    else :
        return False

class Board:
    def __init__(self, page):
        self.page = page
        self.board = self.generate_board()

    def generate_board(self):
        # Créer un tableau avec des numéros de 1 à 8 et une case vide représentée par 0
        board = list(range(1, 9)) + [0]
        rd.shuffle(board)
        while not is_reachable(np.array(board)):
            rd.shuffle(board)
        return [board[i:i + 3] for i in range(0, 9, 3)]  # Organiser en matrice 3x3

    def is_solved(self):
        # Vérifie si le plateau est résolu
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def move_piece(self, empty_pos, new_pos):
        # Effectuer l'échange entre la pièce et la case vide
        self.board[empty_pos[0]][empty_pos[1]], self.board[new_pos[0]][new_pos[1]] = \
            self.board[new_pos[0]][new_pos[1]], self.board[empty_pos[0]][empty_pos[1]]

    def get_empty_pos(self):
        # Trouve la position de la case vide (0)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return (0, 0)

    def update_board(self):
        # Crée les boutons pour chaque case
        buttons = []  # Liste pour stocker les boutons

        for i in range(3):
            row = []  # Liste pour une ligne de boutons
            for j in range(3):
                value = self.board[i][j]
                if value == 0:
                    # Si c'est la case vide, on met un bouton vide
                    button = ft.ElevatedButton(text=" ", width=100, height=100)
                else:
                    # Créer un bouton pour chaque case avec un gestionnaire d'événements
                    button = ft.ElevatedButton(
                        text=str(value),
                        width=100,
                        height=100,bgcolor=ft.colors.BLUE_100,
                        on_click=self.create_move_handler(i, j)  # Attacher le gestionnaire ici
                    )
                row.append(button)
            buttons.append(row)

        # Organiser les boutons en une grille de colonnes et lignes
        grid = ft.Column(controls=[ft.Row(controls=row) for row in buttons], spacing=5)
        self.page.controls.clear()  # Effacer l'ancienne grille
        self.page.add(grid)  # Ajouter la nouvelle grille
        self.page.update()  # Mettre à jour l'affichage

    def create_move_handler(self, i, j):
        # Cette méthode crée et retourne un gestionnaire d'événements pour le clic d'un bouton
        def move_piece(e):
            empty_pos = self.get_empty_pos()  # Trouver la position de la case vide
            ex, ey = empty_pos  # Position de la case vide

            # Logique de déplacement
            if (abs(i - ex) == 1 and j == ey) or (abs(j - ey) == 1 and i == ex):
                print(f"Déplacement de ({ex}, {ey}) vers ({i}, {j})")
                self.move_piece(empty_pos, (i, j))  # Effectuer l'échange des pièces
                self.update_board()  # Mettre à jour la grille après le mouvement

                # Vérifier si le jeu est résolu
                if self.is_solved():
                    self.page.add(ft.Text("Vous avez gagné !", size=30))  # Afficher un message de victoire
                    self.page.update()  # Mettre à jour l'affichage
        return move_piece  # Retourner la fonction de gestion de l'événement


def main(page: ft.Page):
    # Afficher un message de chargement au démarrage
    page.add(ft.Text("Chargement du jeu... Veuillez patienter.", size=20))
    page.update()

    # Créer une instance du jeu
    board = Board(page)
    
    # Afficher initialement la grille
    board.update_board()

    # Ajouter un message de victoire une fois que le jeu est résolu
    while not board.is_solved():  # Tant que le jeu n'est pas résolu, mettre à jour le plateau
        pass

    # Lorsque le jeu est résolu, afficher "Vous avez gagné !"
    board.page.add(ft.Text("Vous avez gagné !", size=30))
    board.page.update()  # Mettre à jour l'affichage


# Démarrer l'application Flet
ft.app(target=main)
