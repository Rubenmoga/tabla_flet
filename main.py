import flet as ft


def main(page: ft.Page, data): # Data debe ser una matriz (lista de listas) con los datos de la tabla.

    page.title = "Tabla de peliculas"
    page.window.width = 900
    page.window.height = 900
    page.window.frameless = True
    #page.window.resizable=False
    page.padding=0

    window_width = page.window.width
    window_height = page.window.height
    
    columnas=[
        ft.DataColumn(
            ft.Text(data[0][i], size=15, weight=ft.FontWeight.W_600)
            )
            for i in range(len(data[0]))
    ]

    filas=[
        ft.DataRow(
            cells=[ft.DataCell(ft.Text(cell)) for cell in row],
        )
        for row in data[1:]
    ]

    tabla = ft.DataTable(
        width=window_width, border=ft.border.all(color=ft.colors.WHITE), expand=True,
        column_spacing=100,
        border_radius=10,
        columns=columnas, 
        rows=filas
        )

    lv = ft.ListView(
        expand=True
    )

    lv.controls.append(tabla)


    def on_resize(event): # event es un parametro que pasa el evento de redimensionamiento. Aunque no se utilice es una buena práctica incluirlo
        page.update()


    page.on_resized = on_resize

    page.add(lv)


def start_flet(data):
    ft.app(target=lambda page: main(page, data))

if __name__ == "__main__":
    data = sys.argv[1] 
    if not len(sys.argv) > 1: "No se proporcionaron datos"
    start_flet_app(data)