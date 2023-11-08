# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.


from logic import make_empty_board, get_winner, other_player

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = "X"
    while winner == None:
        print("Player's turn:", player)
        
        # Show the board to the user.
        for row in board:
            print(row)
        
        # Input a move from the player.
        x, y = map(int, input("Enter the position of (x,y), split with comma: ").split(","))
        
        # Update the board.
        board[x][y] = player
        winner = get_winner(board)
        
        # Update who's turn it is.
        if not winner:
            player = other_player(player)
        
        print(winner)