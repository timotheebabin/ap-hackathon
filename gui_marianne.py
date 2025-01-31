import flet as ft


def square(i):
    if i > 0 :
        return(ft.Container(
                content=ft.Text(value=str(i)),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                bgcolor=ft.Colors.GREEN,
                border_radius=ft.border_radius.all(5))
                )
    else : 
        return(ft.Container(
                content=ft.Text(value=str(i)),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                bgcolor=ft.Colors.RED,
                border_radius=ft.border_radius.all(5))
                )

squares = [ [square(i) for i in range(1,4)],[square(i) for i in range(4,7)], [square(i) for i in range(7,9)]+[square(0)]]

def main(page: ft.Page):
    page.title = "GridView Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.update()


    page.add(

        ft.Column([
                
                ft.Column([

                    ft.Row(spacing=10, controls=squares[0]),
                    ft.Row(spacing=10, controls=squares[1]),
                    ft.Row(spacing=10, controls=squares[2]),
                ]),

                ft.Row([
                    ft.IconButton(
                        icon=ft.Icons.REMOVE,
                        icon_color="blue400",
                        icon_size=50,
                        tooltip="Pause record"),
                    
                    ft.IconButton(
                        icon=ft.Icons.LIGHTBULB,
                        icon_color="yellow",
                        icon_size=50,
                        tooltip="Pause record")
                        
                    ])
            ])

    )


ft.app(main)

