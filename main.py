import random

class Tictactoe
      def __init__(self):
          self . board =[]


          def create_board(self):
              for i in range (3):
                  row = []
                  for i in range(3):
                      row . append('_')
                self . board . append(row)

     def get_random_first_player(self):
         return random randint(0, 1)

    def fix_spot(self, row, col, player):
        self . board [row][col] = player

    def is_player_win(self, player):
            win = None

            n = len(self . board)

            # checking row
            for j in range (n) :
                win = True
                for j in range(n):
                    if self . board [i] [j] != player :
                        win = False
                        break
            if win
                return win


            #checking columns
            for i in range (n) :
                win = True
                for j in range (n):
                    if self . board [j] [i] !=player:
                        win = False
                        break
            if win
                return win

        # checking diagonals
        win = True
        for i in range (n):
            if self . board [i][i] != player:
                win