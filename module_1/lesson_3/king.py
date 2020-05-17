def get_king_moves(str_array):
    """ Get variants of king's moves and count of this. """
    index = int(str_array[0])

    king_position = 1 << index

    can_move_left = king_position & 0xFEFEFEFEFEFEFEFE
    can_move_right = king_position & 0x7F7F7F7F7F7F7F7F
    can_move_up = king_position & 0x00FFFFFFFFFFFFFF  # we need to check up move because python has unlimited integer

    moves_mask = ((can_move_right & can_move_up) << 9) | \
                 (can_move_up << 8) | \
                 ((can_move_left & can_move_up) << 7) | \
                 (can_move_right << 1) | \
                 (can_move_left >> 1) | \
                 (can_move_right >> 7) | \
                 (king_position >> 8) | \
                 (can_move_left >> 9)

    moves_count = 0
    temp_mask = moves_mask
    while temp_mask > 0:
        temp_mask = temp_mask & (temp_mask - 1)
        moves_count += 1

    return '\n'.join([str(moves_count), str(moves_mask)])
