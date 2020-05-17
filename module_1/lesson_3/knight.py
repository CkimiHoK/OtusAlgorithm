def get_knight_moves(str_array):
    """ Get variants of knight's moves and count of this. """
    index = int(str_array[0])

    knight_position = 1 << index

    can_move_left_1_cell = knight_position & 0xFEFEFEFEFEFEFEFE
    can_move_left_2_cell = knight_position & 0xFCFCFCFCFCFCFCFC
    can_move_right_1_cell = knight_position & 0x7F7F7F7F7F7F7F7F
    can_move_right_2_cell = knight_position & 0x3F3F3F3F3F3F3F3F
    can_move_up_1_cell = knight_position & 0x00FFFFFFFFFFFFFF  # we need to check up move because python has unlimited integer
    can_move_up_2_cell = knight_position & 0x0000FFFFFFFFFFFF  # we need to check up move because python has unlimited integer

    moves_mask = ((can_move_up_2_cell & can_move_right_1_cell) << 17) | \
                 ((can_move_up_2_cell & can_move_left_1_cell) << 15) | \
                 ((can_move_up_1_cell & can_move_right_2_cell) << 10) | \
                 ((can_move_up_1_cell & can_move_left_2_cell) << 6) | \
                 (can_move_right_2_cell >> 6) | \
                 (can_move_left_2_cell >> 10) | \
                 (can_move_right_1_cell >> 15) | \
                 (can_move_left_1_cell >> 17)

    moves_count = 0
    temp_mask = moves_mask
    while temp_mask > 0:
        temp_mask = temp_mask & (temp_mask - 1)
        moves_count += 1

    return '\n'.join([str(moves_count), str(moves_mask)])
