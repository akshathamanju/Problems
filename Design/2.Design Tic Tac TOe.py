import os
'''
Board class: to create hte board and display the board
'''
#1. board class
#2.
#3.Determine the winner
#4. draw/Tie game
# not implemented 5.AI moves/ Computer play
class Board:

    def __init__(self):
        #creating 10 cells to strt the cells from index-1
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    #to display the board
    def display(self):
        print("%s | %s  |%s "%(self.cells[1], self.cells[2], self.cells[3]))
        print("___________")
        print("%s | %s  |%s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("___________")
        print("%s | %s  |%s " % (self.cells[7], self.cells[8], self.cells[9]))
    # To update the cells in the board
    def update_cell(self, cell_number, player ):
        # if cell is empty, update the cell
        if self.cells[cell_number] == " ":
            self.cells[cell_number] = player

    def decide_winner(self, player):
        for each_combinaton in [[1,2,3],[3,4,5],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
            result = True
            for cell_no in each_combinaton:
                if self.cells[cell_no] != player:
                    result = False
                if result == True:
                    return True
        return False
        # if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
        #     return True
        # if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
        #     return True
        # if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
        #     return True
        # if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
        #     return True
        # if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
        #     return True
        # if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
        #     return True
        # if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
        #     return True
        # if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
        #     return True
        # return False


    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False
    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def ai_move(self, player):

        if player == "X":
            enemy = "O"
        if player == "O":
            enemy = "X"
        #If center cell is open choose that
        if self.cells[5] == " ":
            self.update_cell(5, player)
        #AI  can win

        #AI blocks

        #Choose random
        for i in range(1, 10):
            if self.cells[i] == "":
                self.update_cell(i, player)
                break

board = Board()
board.display()

def print_header():
    print("Welcome to tic tac toe")

def refresh_screen():
    #clear the screen
    os. system('cls')
    #print the header
    print_header()
    #show the updated board
    board.display()


while True:
    refresh_screen()

    #Get X input
    x_choice = int(input("\nX) Please choose 1 - 9 : "))

    #Update board
    board.update_cell(x_choice, "X")
    refresh_screen()
    # check for X win
    if board.decide_winner("X"):
        print("\n X won !")
        play_again = input("Would ypu like to play again ? (Y/N) : ").upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break
    #check for tie
    if board.is_tie():
        print("\n Game Tie/Draw !")
        play_again = input("Would ypu like to play again ? (Y/N) : ").upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break
    board.ai_move("O")
    # # Get O input
    # o_choice = int(input("\nO) Please choose 1 - 9 : "))
    #
    # # Update board
    # board.update_cell(o_choice, "O")
    #

    # check for O win
    if board.decide_winner("O"):
        print("\n O won !")
        play_again = input("Would ypu like to play again ? (Y/N) : ").upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break

    #check for tie
    if board.is_tie():
        print("\n Game Tie/Draw !")
        play_again = input("Would ypu like to play again ? (Y/N) : ").upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break
    #refresh screen will update the board in the memory
    refresh_screen()


