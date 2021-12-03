import random
class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.data = [['O' for i in range(self.width)] for j in range(self.height)]
        self.available_guesses = []
        for row in range(0, 8):
            for col in range(0, 8):
                self.available_guesses += [(row, col)]
    
    def __repr__(self):
        s = ''                          
        for row in range(0, self.height): # The main board
            
            for col in range(0, self.width):
                s += self.data[row][col] 
            s = s + '|' + str(row) #add row numbers
            s += '\n'
        s += (self.width + 1) * '-'   # Bottom of the board
        
        s = s + '\n'
        for col in range(self.width):
            s = s + str(col) #put the column numbers underneath
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

            if abs(c_0 - c_1) != (s-1): #fits ship length
                return False

            c_lower = min(c_0,c_1)
            c_upper = max(c_0,c_1) #range doesnt work if the lower bound is higher
            for i in range(c_lower, c_upper): #no overlap
                if self.data[r_0][i] != 'O':
                    return False
            return True

        if c_0 == c_1: #not diag cause cols
            if abs(r_0 - r_1) != (s-1):#fits ship length
                return False
            r_lower = min(r_0,r_1)
            r_upper = max(r_0,r_1) #range doesnt work if the lower bound is higher
            for i in range(r_lower, r_upper): #no overlap
                if self.data[i][c_0] != 'O':
                    return False
            return True
        return False
        


            

    def place_ship(self, r, c):
        """I was just too lazy to do this command a bunch"""
        self.data[r][c] = "S"


    def init_game(self):
        """initializes a board for the player to fill out"""
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
                for i in range(c_min, c_max+1):
                    self.place_ship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max+1):
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
                for i in range(c_min, c_max+1):
                    self.place_ship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max+1):
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
                for i in range(c_min, c_max+1):
                    self.place_ship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max+1):
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
                for i in range(c_min, c_max+1):
                    self.place_ship(r_0,i)
            

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max+1):
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
                for i in range(c_min, c_max+1):
                    self.place_ship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max+1):
                    self.place_ship(i,c_0)
            print(self)
            

    
    def ai_board(self):
        while True:
            #destroyer
            r_0 = random.randrange(0,8)
            c_0 = random.randrange(0,8)
            r_1 = random.randrange(0,8)
            c_1 = random.randrange(0,8)
            while not self.can_place(r_0,c_0,r_1,c_1,5):
                r_0 = random.randrange(0,8)
                c_0 = random.randrange(0,8)
                r_1 = random.randrange(0,8)
                c_1 = random.randrange(0,8)
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                for i in range(c_min, c_max+1):
                    self.place_ship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max+1):
                    self.place_ship(i,c_0)


            #whatever is under destroyer
            r_0 = random.randrange(0,8)
            c_0 = random.randrange(0,8)
            r_1 = random.randrange(0,8)
            c_1 = random.randrange(0,8)
            while not self.can_place(r_0,c_0,r_1,c_1,4):
                r_0 = random.randrange(0,8)
                c_0 = random.randrange(0,8)
                r_1 = random.randrange(0,8)
                c_1 = random.randrange(0,8)
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                for i in range(c_min, c_max+1):
                    self.place_ship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max+1):
                    self.place_ship(i,c_0)

            


            #under that idfk
            r_0 = random.randrange(0,8)
            c_0 = random.randrange(0,8)
            r_1 = random.randrange(0,8)
            c_1 = random.randrange(0,8)
            while not self.can_place(r_0,c_0,r_1,c_1,3):
                r_0 = random.randrange(0,8)
                c_0 = random.randrange(0,8)
                r_1 = random.randrange(0,8)
                c_1 = random.randrange(0,8)
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                for i in range(c_min, c_max+1):
                    self.place_ship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max+1):
                    self.place_ship(i,c_0)




            #happens twice
            r_0 = random.randrange(0,8)
            c_0 = random.randrange(0,8)
            r_1 = random.randrange(0,8)
            c_1 = random.randrange(0,8)
            while not self.can_place(r_0,c_0,r_1,c_1,3):
                r_0 = random.randrange(0,8)
                c_0 = random.randrange(0,8)
                r_1 = random.randrange(0,8)
                c_1 = random.randrange(0,8)
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                for i in range(c_min, c_max+1):
                    self.place_ship(r_0,i)
            

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max+1):
                    self.place_ship(i,c_0)
        
            


            #baby one
            r_0 = random.randrange(0,8)
            c_0 = random.randrange(0,8)
            r_1 = random.randrange(0,8)
            c_1 = random.randrange(0,8)
            while not self.can_place(r_0,c_0,r_1,c_1,2):
                r_0 = random.randrange(0,8)
                c_0 = random.randrange(0,8)
                r_1 = random.randrange(0,8)
                c_1 = random.randrange(0,8)
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                for i in range(c_min, c_max+1):
                    self.place_ship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                for i in range(r_min, r_max+1):
                    self.place_ship(i,c_0)
            return

    def aiGuess(self):
        """Make a guess (random from list). Removes that guess from the list 
        so AI doesn't guess it again, and if there is a hit, then in the 
        next move it should check the four cardinal directions adjacent 
        to that point. (makes a list of those and choose randomly between them)
        Keeps guessing from those 4 directions until it gets another hit,
        which means it's figured out the orientation of the ship. Then check that
        direction and the direction on the opposite side (eg if north is a hit
        then check south as well, if east is a hit then check west as well) in case
        it hit in the middle of the ship. Keep guessing in those directions until
        it sinks the ship. Otherwise, if there has been no hit, then it guesses randomly."""
        
        
        list_HitTrue = []
        #Need a call to the hit register function here
        #Check if there's a hit, and look at the coordinates of that hit
        #If there is a hit, save the cardinal direction coordinates around that hit in a list: 
        #[(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        #Make a random guess from that list for the next move, and subtract that coordinate from 
        # both the mini-hit list and the overall available guesses list

        #else statement: if no move is advantageous (e.g. no hit), resort to random choice
        guess_location = random.choice(range(len(self.available_guesses)))
        guess = self.available_guesses[guess_location]
        print("I'll guess", guess, "!")
        self.available_guesses.remove(guess)
        return guess

    def take_shot(self, r, c):
        """in: r is a row c is a col
           out: mutates the board to an * if there's a hit, X otherwise, returns True if the r and c is a hit
        """
        if self.data[r][c] == 'S':
            self.data[r][c] = '*'
            return True
        elif self.data == 'O':
            self.data[r][c] = 'X'
        return False
    
    def prob_density(self):
        """returns prob density of self.data by iterating ship placement across the board"""
        denisty_graph = [[0 for i in range(self.width)] for j in range(self.height)]
        #destoryer
        #with vert placement
        for i in range(self.width): #rows
            for j in range(self.height): #cols
                if self.can_place(i,j,i+(5-1), j,5):
                    for k in range(5-1):
                        denisty_graph[i+k][j] += 1
        #with horiz placement
        for i in range(self.width): #rows
            for j in range(self.height): #cols
                if self.can_place(i,j,i, j+(5-1),5):
                    for k in range(5-1):
                        denisty_graph[i][j+k] += 1
        

        #under that 
        #with vert placement
        for i in range(self.width): #rows
            for j in range(self.height): #cols
                if self.can_place(i,j,i+(4-1), j,4):
                    for k in range(4-1):
                        denisty_graph[i+k][j] += 1
        #with horiz placement
        for i in range(self.width): #rows
            for j in range(self.height): #cols
                if self.can_place(i,j,i, j+(4-1),4):
                    for k in range(4-1):
                        denisty_graph[i][j+k] += 1


        #hell if i know
        #with vert placement
        for i in range(self.width): #rows
            for j in range(self.height): #cols
                if self.can_place(i,j,i+(3-1), j,3):
                    for k in range(3-1):
                        denisty_graph[i+k][j] += 1
        #with horiz placement
        for i in range(self.width): #rows
            for j in range(self.height): #cols
                if self.can_place(i,j,i, j+(3-1),3):
                    for k in range(3-1):
                        denisty_graph[i][j+k] += 1

        #under that
        #with vert placement
        for i in range(self.width): #rows
            for j in range(self.height): #cols
                if self.can_place(i,j,i+(3-1), j,3):
                    for k in range(3-1):
                        denisty_graph[i+k][j] += 1
        #with horiz placement
        for i in range(self.width): #rows
            for j in range(self.height): #cols
                if self.can_place(i,j,i, j+(3-1),3):
                    for k in range(3-1):
                        denisty_graph[i][j+k] += 1


        #lil baby
        #with vert placement
        for i in range(self.width): #rows
            for j in range(self.height): #cols
                if self.can_place(i,j,i+(2-1), j,2):
                    for k in range(2-1):
                        denisty_graph[i+k][j] += 1
        #with horiz placement
        for i in range(self.width): #rows
            for j in range(self.height): #cols
                if self.can_place(i,j,i, j+(2-1),2):
                    for k in range(2-1):
                        denisty_graph[i][j+k] += 1
        return denisty_graph

    def ai_just_lookin(self):
        """shoots at the highest num of the prob density graph"""
        max_val = (0,0,0) #thriple containing (val of prob density at (x,y),x,y)
        for i in range(len(self.prob_density())):
            for j in range(len(self.prob_density()[i])):
                max_val = max(max_val, (self.prob_density()[i][j], i, j))
        return (max_val[1],max_val[2])




    

