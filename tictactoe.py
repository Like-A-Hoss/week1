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
        print("----------")
        print(f"| {self.sq1} | {self.sq2} | {self.sq3} |")
        print("----------")
        print(f"| {self.sq4} | {self.sq5} | {self.sq6} |")
        print("----------")
        print(f"| {self.sq7} | {self.sq8} | {self.sq9} |")
        print("----------")

    def cat_game_check(self):
        if self.used_boxes == 9:
            return True
        else:
            return False

class player():
    def __init__(self) -> None:
        name = ""
        score = 0


def main():
    game = board()
    board.draw_board()

if __name__ == "__main__":
    main()
