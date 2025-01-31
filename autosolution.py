import flet as ft
import random
import pygame as pg

def solution(sol):
    clock = pg.time.Clock()

    for k in range(len(sol)):
        mat,n = sol[0][k],sol[1][k]
        i,j = (n-1)//3,(n-1)%3
        
        clock.tick(6)


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

