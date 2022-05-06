#!/usr/bin/env python3

game = [3, 7, 4, 2, 4, 1, 5, 6, 2]


def turn_right(game_board, current_pos):
    """Move right."""
    current_pos = current_pos + game_board[current_pos]
    return current_pos


def turn_left(game_board, current_pos):
    """Move left."""
    current_pos = current_pos - game_board[current_pos]
    return current_pos


def game_solution(game_board):
    """Solves the game."""
    solution = []
    current_pos = 0
    if current_pos == len(game_board) - 1:
        return solution
    else:
        if game_board[current_pos] == game_board[0]:
            current_pos = turn_right(game_board, current_pos)
            solution.append(current_pos)
            if current_pos > len(game_board):
                current_pos = turn_left(game_board, current_pos)
                solution.pop()
                solution.append(current_pos)
            if current_pos < 0:
                current_pos = turn_right(game_board, current_pos)
                solution.pop()
                solution.append(current_pos)
            else:
                current_pos = turn_right(game_board, current_pos)
                solution.append(current_pos)

    return solution


print(game_solution(game))
