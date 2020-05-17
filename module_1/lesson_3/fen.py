def convert_fen_to_bbd(str_array):
    """ Convert FEN representation of chess field to bit board definition format. """
    fen_str = str_array[0]

    chess_desc_rows = [row for row in fen_str.split('/')]  # Split figures positions to chess rows
    chess_desc_rows.reverse()  # Reverse rows position. Now they are directed from the bottom to up

    figures_positions = ''.join(chess_desc_rows)

    result_figure_indexes = 'PNBRQKpnbrqk'  # figure's indexes in result
    result_positions_list = [0 for _ in range(12)]  # figure's positions in bbd format

    index = 0
    for item in figures_positions:  # check all fen positions
        if item.isdigit():  # skip numbers
            index += int(item)
        else:
            item_index = result_figure_indexes.index(item)
            result_positions_list[item_index] += 1 << index
            index += 1

    return '\n'.join([str(pos) for pos in result_positions_list])  # convert to list of string and return one with NL
