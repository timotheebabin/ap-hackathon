import flet as ft
import random as rd
import numpy as np


# Cette fonction renvoie un bool indiquant si le board est atteignable.
def is_reachable(given_board):
    assert type(given_board) == np.ndarray or type(given_board) == list, "Il faut un tableau numpy ou une liste"
    board = np.array([0 for i in range(8)])
    k = 0
    given_board2 = given_board.copy()  # pour éviter les effets colatéraux
    if type(given_board2) == np.ndarray and given_board2.shape == (3, 3):
        given_board2.reshape(9)
    elif type(given_board2) == list:
        given_board2 = np.array(given_board2)
    for i in range(9):
        a = given_board2[i]
        if a != 0:
            board[k] = a
            k += 1

    # Calcul de la signature
    epsilon = 1
    for i in range(1, 8):
        for j in range(i + 1, 9):
            sigmai = board[i - 1]
            sigmaj = board[j - 1]
            if ((i < j and sigmai > sigmaj) or (i > j and sigmai < sigmaj)):
                epsilon *= (-1)
    return epsilon == 1


class Board:
    def __init__(self, page):
        self.page = page
        self.board = self.generate_board()

    def generate_board(self):
        board = list(range(1, 9)) + [0]
        rd.shuffle(board)
        while not is_reachable(np.array(board)):
            rd.shuffle(board)
        return [board[i:i + 3] for i in range(0, 9, 3)]

    def is_solved(self):
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def move_piece(self, empty_pos, new_pos):
        self.board[empty_pos[0]][empty_pos[1]], self.board[new_pos[0]][new_pos[1]] = \
            self.board[new_pos[0]][new_pos[1]], self.board[empty_pos[0]][empty_pos[1]]

    def get_empty_pos(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return (0, 0)

    def update_board(self):
        buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                value = self.board[i][j]
                if value == 0:
                    button = ft.ElevatedButton(text=" ", width=100, height=100)
                else:
                    button = ft.ElevatedButton(
                        text=str(value),
                        width=100,
                        height=100,
                        bgcolor=ft.colors.BLUE_100,
                        on_click=self.create_move_handler(i, j)
                    )
                row.append(button)
            buttons.append(row)
        grid = ft.Column(controls=[ft.Row(controls=row) for row in buttons], spacing=5)
        centered_grid = ft.Row(
            controls=[grid],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.page.controls.clear()
        self.page.add(centered_grid)
        icon_row = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.REFRESH,
                    icon_color="red",
                    icon_size=50,
                    tooltip="Recommencer",
                    on_click=self.reset_board
                ),
                ft.IconButton(
                    icon=ft.Icons.LIGHTBULB,
                    icon_color="yellow",
                    icon_size=50,
                    tooltip="Aide"
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20 
        )
        self.page.add(icon_row)
        self.page.update()

    def create_move_handler(self, i, j):
        def move_piece(e):
            empty_pos = self.get_empty_pos()
            ex, ey = empty_pos
            if (abs(i - ex) == 1 and j == ey) or (abs(j - ey) == 1 and i == ex):
                self.move_piece(empty_pos, (i, j))
                self.update_board()
        return move_piece

    def reset_board(self, e):
        self.board = self.generate_board()
        self.update_board()


def main(page: ft.Page):
    board = Board(page)
    board.update_board()
    while not board.is_solved():
        pass
    board.page.add(ft.Text("Vous avez gagné !", size=30))
    board.page.update() 

ft.app(target=main)
