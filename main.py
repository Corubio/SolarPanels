def check_space(area, panel_width, panel_height, i, j):
    """ Revisa si el espacio está disponible para colocar un panel en la posición dada. """
    for x in range(i, i + panel_width):
        for y in range(j, j + panel_height):
            if x >= len(area) or y >= len(area[0]) or area[x][y] != 0:
                return False
    return True


def place_panel(area, panel_width, panel_height, i, j):
    """ Coloca un panel en la posición dada. """
    for x in range(i, i + panel_width):
        for y in range(j, j + panel_height):
            area[x][y] = 1


def remove_panel(area, panel_width, panel_height, i, j):
    """ Remueve un panel en la posición dada. """
    for x in range(i, i + panel_width):
        for y in range(j, j + panel_height):
            area[x][y] = 0


def fill_area(area, panel_width, panel_height, i, j):
    """ Rellena el área con paneles y devuelve la cantidad máxima de paneles que se pueden colocar. """
    if i >= len(area):
        return 0

    # Se definen las coordenadas de la siguiente celda
    next_i, next_j = (i, j + 1) if j + 1 < len(area[0]) else (i + 1, 0)

    # Opcion 1: No colocar un panel
    max_panels = fill_area(area, panel_width, panel_height, next_i, next_j)

    # Opcion 2: Colocar un panel si es posible
    if check_space(area, panel_width, panel_height, i, j):
        place_panel(area, panel_width, panel_height, i, j)
        max_panels = max(
            max_panels,
            1 + fill_area(area, panel_width, panel_height, next_i, next_j)
        )
        remove_panel(area, panel_width, panel_height, i, j)

    # opción 3: Colocar un panel rotado si es posible
    if panel_width != panel_height and check_space(area, panel_height, panel_width, i, j):
        place_panel(area, panel_height, panel_width, i, j)
        max_panels = max(
            max_panels,
            1 + fill_area(area, panel_width, panel_height, next_i, next_j)
        )
        remove_panel(area, panel_height, panel_width, i, j)

    return max_panels


def generar_area(area_width, area_height, figure):
    """ Genera un área que representa la figura dada. """
    if figure == "R":
        return [[0 for _ in range(area_height)] for _ in range(area_width)]
    return [[0]]


def main():
    """ Función principal. Lee la entrada desde in.txt genera el área y entrega el resultado en out.txt. """
    with open("in.txt", "r") as infile:
        figure = infile.readline().strip()
        panel_width, panel_height = map(int, infile.readline().split())
        area_width, area_height = map(int, infile.readline().split())

    area = generar_area(area_width, area_height, figure)
    result = fill_area(area, panel_width, panel_height, 0, 0)

    with open("out.txt", "w") as outfile:
        outfile.write(str(result) + "\n")


if __name__ == "__main__":
    main()
