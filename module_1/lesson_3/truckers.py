from module_1.lesson_3.fen import convert_fen_to_bbd


# TODO do not ready
def get_figures_moves(str_array):
    """ Get possible moves of white figures. """
    bbd_figures_positions = convert_fen_to_bbd(str_array)
    print(bbd_figures_positions)  # TODO delete later

    fen_str = str_array[0]
    print(fen_str)  # TODO delete later

    chess_desc_rows = [row for row in fen_str.split('/')]  # Split figures positions to chess rows
    chess_desc_rows.reverse()  # Reverse rows position. Now they are directed from the bottom to up
    print(chess_desc_rows)  # TODO delete later

    white_bishop_index = 0

    for row in chess_desc_rows:
        print(row)

    return None


print(get_figures_moves(['5k2/1Pr5/4Q1n1/8/5B2/1R3p2/7q/1bK5']))
