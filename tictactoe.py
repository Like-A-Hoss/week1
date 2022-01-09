from types import FrameType


class board():
    def __init__(self) -> None:
        self.sq1 = "1"
        self.sq2 = "2"
        self.sq3 = "3"
        self.sq4 = "4"
        self.sq5 = "5"
        self.sq6 = "6"
        self.sq7 = "7"
        self.sq8 = "8"
        self.sq9 = "9"
        self.p1_active = True
        self.used_boxes = 0
        self.boxes_used = []
    def row_check(self):
        mark =""
        if self.p1_active == True:
            mark = "X"
        if self.p1_active == False:
            mark = "O"
        #Row 1 check
        if self.sq1 and self.sq2 and self.sq3 == mark:
            return True
        elif self.sq4 and self.sq5 and self.sq6 == mark:
            return True
        elif self.sq7 and self.sq8 and self.sq9 == mark:
            return True
        else:
            return False

    def col_check(self):
        mark =""
        if self.p1_active == True:
            mark = "X"
        if self.p1_active == False:
            mark = "O"
        #column checks
        if self.sq1 and self.sq4 and self.sq7 == mark:
            return True
        elif self.sq2 and self.sq5 and self.sq8 == mark:
            return True
        elif self.sq3 and self.sq6 and self.sq9 == mark:
            return True
        else:
            return False
    
    def diag_check(self):
        mark =""
        if self.p1_active == True:
            mark = "X"
        if self.p1_active == False:
            mark = "O"
        #Check direction 1
        if self.sq1 and self.sq5 and self.sq9 == mark:
            return True
        elif self.sq3 and self.sq5 and self.sq7 == mark:
            return True
        else:
            return False
    
    def draw_board(self):
        print("-------------")
        print(f"| {self.sq1} | {self.sq2} | {self.sq3} |")
        print("-------------")
        print(f"| {self.sq4} | {self.sq5} | {self.sq6} |")
        print("-------------")
        print(f"| {self.sq7} | {self.sq8} | {self.sq9} |")
        print("-------------")

    def cat_game_check(self):
        if self.used_boxes == 9:
            return True
        else:
            return False

    def mark_square(self, num):
        if self.p1_active == True:
            mark = "X"
        else:
            mark = "0"
        if num == 1:
            self.sq1 = mark
        if num == 2:
            self.sq2 = mark
        if num == 3:
            self.sq3 = mark    
        if num == 4:
            self.sq4 = mark
        if num == 5:
            self.sq5 = mark
        if num == 6:
            self.sq6 = mark
        if num == 7:
            self.sq7 = mark
        if num == 8:
            self.sq8 = mark
        if num == 9:
            self.sq9 = mark

    def change_player(self):
        if self.p1_active == True:
            self.p1_active == False
        else:
            self.p1_active =True

    def check_if_used(self, num):
        if num in self.boxes_used:
            return False
        else:
            return True
    def make_move(self):
        valid = False
        responses = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while valid == False:
            move = input("Please input the number of an open square: ")
            if move in responses:
                move = int(move)
                valid = self.check_if_used(move)
                if valid == True:
                    self.mark_square(move)
                    self.used_boxes += 1
                    self.boxes_used.append(move)
                






def main():
    game_on = True
    game = board()
    game.draw_board()
    while game_on == True:
        game.draw_board()
        game.make_move()
        row_check = game.row_check()
        col_check = game.col_check()
        diag_check = game.diag_check()
        cat_game = game.cat_game_check()
        if row_check == True or col_check == True or diag_check == True:
            if game.p1_active == True:
                print("Honor and Glory to Player 1  You Win!")
                game_on = False
            else:
                print("Honor and Glory to Player 2  You Win!")
                game_on = False
        elif cat_game == True:
            print("The Game is a Draw  The Cat has Scratched it!")
            game_on = False
        else:
            if game.p1_active == True:
                print("Player 2 is up next")
                game.change_player()


if __name__ == "__main__":
    main()
