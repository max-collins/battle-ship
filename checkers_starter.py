class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.data = [['O' for i in range(self.width)] for j in range(self.height)]
    
    def __repr__(self):
        s = ''                          
        for row in range(0, self.height):
            for col in range(0, self.width):
                s += self.data[row][col] 
            s += '\n'
        return s

    def can_place(self,r_0,c_0,r_1,c_1, s):
        """in: r_0 is start row, c_0 start column, r_1 end row, c_1 end column, s is ship length
           out: True is a boat can be placed there(no overlap and on board not diag), False else.
        """
        if r_0 < 0 or r_0 > 8: #initial board chekcs
            return False

        if c_0 < 0 or c_1 > 8:
            return False

        if r_1 < 0 or r_1 > 8:
            return False

        if c_1 < 0 or c_1 > 8:
            return False

        if r_0 == r_1:#not diag cause rows

            if abs(c_0 - c_1) != s: #fits ship length
                return False

            c_lower = min(c_0,c_1)
            c_upper = max(c_0,c_1) #range doesnt work if the lower bound is higher
            for i in range(c_lower, c_upper): #no overlap
                if self.data[r_0][i] != 'O':
                    return False
            return True

        if c_0 == c_1: #not diag cause cols
            if abs(r_0 - r_1) != s:#fits ship length
                return False
            r_lower = min(r_0,r_1)
            r_upper = max(r_0,r_1) #range doesnt work if the lower bound is higher
            for i in range(r_lower, r_upper): #no overlap
                if self.data[i][c_0] != 'O':
                    return False
            return True
        return False
        


            

    def place_ship(self, r, c):
        self.data[r][c] = "S"


    def init_game(self):
        while True:
            #destroyer
            r_0 = int(input('start row for 5: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
            while not self.can_place(r_0,c_0,r_1,c_1,5):
                r_0 = int(input('start row for 5: '))
                c_0 = int(input('start col: '))
                r_1 = int(input('end row: '))
                c_1 = int(input('end col: '))
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                for i in range(c_min, c_max):
                    self.place_ship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max):
                    self.place_ship(i,c_0)
            print(self)






            #whatever is under destroyer
            r_0 = int(input('start row for 4: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
            while not self.can_place(r_0,c_0,r_1,c_1,4):
                r_0 = int(input('start row for 4: '))
                c_0 = int(input('start col: '))
                r_1 = int(input('end row: '))
                c_1 = int(input('end col: '))
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                for i in range(c_min, c_max):
                    self.place_ship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max):
                    self.place_ship(i,c_0)
            print(self)
            


            #under that idfk
            r_0 = int(input('start row for 3: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
            while not self.can_place(r_0,c_0,r_1,c_1,3):
                r_0 = int(input('start row for 3: '))
                c_0 = int(input('start col: '))
                r_1 = int(input('end row: '))
                c_1 = int(input('end col: '))
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                for i in range(c_min, c_max):
                    self.place_ship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max):
                    self.place_ship(i,c_0)
            print(self)



            #happens twice
            r_0 = int(input('start row for 3: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
            while not self.can_place(r_0,c_0,r_1,c_1,3):
                r_0 = int(input('start row for 3: '))
                c_0 = int(input('start col: '))
                r_1 = int(input('end row: '))
                c_1 = int(input('end col: '))
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                for i in range(c_min, c_max):
                    self.place_ship(r_0,i)
            

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max):
                    self.place_ship(i,c_0)
            print(self)
            


            #baby one
            r_0 = int(input('start row for 2: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
            while not self.can_place(r_0,c_0,r_1,c_1,2):
                r_0 = int(input('start row for 2: '))
                c_0 = int(input('start col: '))
                r_1 = int(input('end row: '))
                c_1 = int(input('end col: '))
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                for i in range(c_min, c_max):
                    self.place_ship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max):
                    self.place_ship(i,c_0)
            print(self)
            
