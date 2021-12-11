import random
import time
class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.data = [['O' for i in range(self.width)] for j in range(self.height)]
        self.opp_data  = [['O' for i in range(self.width)] for j in range(self.height)]
        self.has_hot = False #mode for searching for a shot
        self.hot_zone = (0,0) #area to search around
        self.v5, self.v4, self.v3, self.v33, self.v2 = True, True, True, True, True #vals are True if that ship is not sunk
        self.available_guesses = []
        for row in range(0, 8):
            for col in range(0, 8):
                self.available_guesses += [(row, col)]
        self.successfulHits = []
        self.available_adv_moves = []
        self.player_wins = 0
        self.ai_wins = 0
    
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

    def show_opp_data(self):
        """prints the opponent's board with the places that you have hit/missed"""
        s = ''                          
        for row in range(0, self.height): # The main board
            
            for col in range(0, self.width):
                s += self.opp_data[row][col] 
            s = s + '|' + str(row) #add row numbers
            s += '\n'
        s += (self.width + 1) * '-'   # Bottom of the board
        
        s = s + '\n'
        for col in range(self.width):
            s = s + str(col) #put the column numbers underneath
        print(s)

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

    def can_place_for_opp(self,r_0,c_0,r_1,c_1, s):
        """can_place() but for ai_just_lookin
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
                if self.opp_data[r_0][i] != 'O':
                    return False
            return True

        if c_0 == c_1: #not diag cause cols
            if abs(r_0 - r_1) != (s-1):#fits ship length
                return False
            r_lower = min(r_0,r_1)
            r_upper = max(r_0,r_1) #range doesnt work if the lower bound is higher
            for i in range(r_lower, r_upper): #no overlap
                if self.opp_data[i][c_0] != 'O':
                    return False
            return True
        return False

    def place_aircraft_carrier(self, r, c):
        """I was just too lazy to do this command a bunch
        it places the ship for the AC"""
        self.data[r][c] = "A"
    def place_battleship(self, r, c):
        """I was just too lazy to do this command a bunch
        places the battleship"""
        self.data[r][c] = "B"
    def place_sub(self, r, c):
        """I was just too lazy to do this command a bunch
        places the sub"""
        self.data[r][c] = "S"
    def place_cruiser(self, r, c):
        """I was just too lazy to do this command a bunch
        places cruiser"""
        self.data[r][c] = "C"
    def place_destroyer(self, r, c):
        """I was just too lazy to do this command a bunch
        places destroyer"""
        self.data[r][c] = "D"

    def init_game(self):
        """initializes a board for the player to fill out"""
        print(self)
        #destroyer
        try:
            r_0 = int(input('start row for 5: '))
        except:
            r_0 = 20
        try:
            c_0 = int(input('start col: '))
        except:
            c_0 = 20
        try:
            r_1 = int(input('end row: '))
        except:
            r_1 = 20
        try:
            c_1 = int(input('end col: '))
        except:
            c_1 = 20
        while not self.can_place(r_0,c_0,r_1,c_1,5):
            r_0 = int(input('start row for 5: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
        if r_0 == r_1:
            c_min = min(c_0,c_1)
            c_max = max(c_0,c_1)
            for i in range(c_min, c_max+1):
                self.place_aircraft_carrier(r_0,i)

        if c_0 == c_1:
            r_min = min(r_0,r_1)
            r_max = max(r_0,r_1)
            for i in range(r_min, r_max+1):
                self.place_aircraft_carrier(i,c_0)
        print(self)

        #whatever is under destroyer
        try:
            r_0 = int(input('start row for 4: '))
        except:
            r_0 = 20
        try:
            c_0 = int(input('start col: '))
        except:
            c_0 = 20
        try:
            r_1 = int(input('end row: '))
        except:
            r_1 = 20
        try:
            c_1 = int(input('end col: '))
        except:
            c_1 = 20
        while not self.can_place(r_0,c_0,r_1,c_1,4):
            r_0 = int(input('start row for 4: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
        if r_0 == r_1:
            c_min = min(c_0,c_1)
            c_max = max(c_0,c_1)
            for i in range(c_min, c_max+1):
                self.place_battleship(r_0,i)

        if c_0 == c_1:
            r_min = min(r_0,r_1)
            r_max = max(r_0,r_1)
            for i in range(r_min, r_max+1):
                self.place_battleship(i,c_0)
        print(self)

        #under that idk
        try:
            r_0 = int(input('start row for 3: '))
        except:
            r_0 = 20
        try:
            c_0 = int(input('start col: '))
        except:
            c_0 = 20
        try:
            r_1 = int(input('end row: '))
        except:
            r_1 = 20
        try:
            c_1 = int(input('end col: '))
        except:
            c_1 = 20
        while not self.can_place(r_0,c_0,r_1,c_1,3):
            r_0 = int(input('start row for 3: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
        if r_0 == r_1:
            c_min = min(c_0,c_1)
            c_max = max(c_0,c_1)
            for i in range(c_min, c_max+1):
                self.place_cruiser(r_0,i)

        if c_0 == c_1:
            r_min = min(r_0,r_1)
            r_max = max(r_0,r_1)
            for i in range(r_min, r_max+1):
                self.place_cruiser(i,c_0)
        print(self)

        #happens twice
        try:
            r_0 = int(input('start row for 3: '))
        except:
            r_0 = 20
        try:
            c_0 = int(input('start col: '))
        except:
            c_0 = 20
        try:
            r_1 = int(input('end row: '))
        except:
            r_1 = 20
        try:
            c_1 = int(input('end col: '))
        except:
            c_1 = 20
        while not self.can_place(r_0,c_0,r_1,c_1,3):
            r_0 = int(input('start row for 3: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
        if r_0 == r_1:
            c_min = min(c_0,c_1)
            c_max = max(c_0,c_1)
            for i in range(c_min, c_max+1):
                self.place_sub(r_0,i)
        

        if c_0 == c_1:
            r_min = min(r_0,r_1)
            r_max = max(r_0,r_1)
            for i in range(r_min, r_max+1):
                self.place_sub(i,c_0)
        print(self)

        #baby one
        try:
            r_0 = int(input('start row for 2: '))
        except:
            r_0 = 20
        try:
            c_0 = int(input('start col: '))
        except:
            c_0 = 20
        try:
            r_1 = int(input('end row: '))
        except:
            r_1 = 20
        try:
            c_1 = int(input('end col: '))
        except:
            c_1 = 20
        while not self.can_place(r_0,c_0,r_1,c_1,2):
            r_0 = int(input('start row for 2: '))
            c_0 = int(input('start col: '))
            r_1 = int(input('end row: '))
            c_1 = int(input('end col: '))
        if r_0 == r_1:
            c_min = min(c_0,c_1)
            c_max = max(c_0,c_1)
            for i in range(c_min, c_max+1):
                self.place_destroyer(r_0,i)

        if c_0 == c_1:
            r_min = min(r_0,r_1)
            r_max = max(r_0,r_1)
            for i in range(r_min, r_max+1):
                self.place_destroyer(i,c_0)
        print(self)

            
             
    def ai_board(self):
        while True:
            #aircraft carrier
            r_0 = random.randrange(0,8)
            c_0 = random.randrange(0,8)
            r_1 = random.randrange(0,8)
            c_1 = random.randrange(0,8)
            while not self.can_place(r_0,c_0,r_1,c_1, 5):
                r_0 = random.randrange(0,8)
                c_0 = random.randrange(0,8)
                r_1 = random.randrange(0,8)
                c_1 = random.randrange(0,8)
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                if self.can_place(r_0,c_0,r_1,c_1, 5) == True:
                    for i in range(c_min, c_max+1):
                        self.place_aircraft_carrier(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                if self.can_place(r_0,c_0,r_1,c_1, 5) == True:
                    for i in range(r_min, r_max+1):
                        self.place_aircraft_carrier(i,c_0)


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
                if self.can_place(r_0,c_0,r_1,c_1, 4) == True:
                    for i in range(c_min, c_max+1):
                    
                        self.place_battleship(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                if self.can_place(r_0,c_0,r_1,c_1, 4) == True:
                    for i in range(r_min, r_max+1):
                    
                        self.place_battleship(i,c_0)

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
                if self.can_place(r_0,c_0,r_1,c_1, 3) == True:
                    for i in range(c_min, c_max+1):
                    
                        self.place_cruiser(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                if self.can_place(r_0,c_0,r_1,c_1, 3) == True:
                    for i in range(r_min, r_max+1):
                    
                        self.place_cruiser(i,c_0)

            #happens twice
            r_0 = random.randrange(0,8)
            c_0 = random.randrange(0,8)
            r_1 = random.randrange(0,8)
            c_1 = random.randrange(0,8)
            while not self.can_place(r_0,c_0,r_1,c_1, 3):
                r_0 = random.randrange(0,8)
                c_0 = random.randrange(0,8)
                r_1 = random.randrange(0,8)
                c_1 = random.randrange(0,8)
            if r_0 == r_1:
                c_min = min(c_0,c_1)
                c_max = max(c_0,c_1)
                if self.can_place(r_0,c_0,r_1,c_1, 3) == True:
                    for i in range(c_min, c_max+1):
                        self.place_sub(r_0,i)
            

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                if self.can_place(r_0,c_0,r_1,c_1, 3) == True:
                    for i in range(r_min, r_max+1):
                        self.place_sub(i,c_0)

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
                if self.can_place(r_0,c_0,r_1,c_1, 2) == True:
                    for i in range(c_min, c_max+1):
                        self.place_destroyer(r_0,i)

            if c_0 == c_1:
                r_min = min(r_0,r_1)
                r_max = max(r_0,r_1)
                if self.can_place(r_0,c_0,r_1,c_1, 2) == True:
                    for i in range(r_min, r_max+1):
                        self.place_destroyer(i,c_0)
            return

    def aiGuess(self):
        """Make a guess (random from list). Removes that guess from the list 
        so AI doesn't guess it again, and if there is a hit, then in the 
        next move it should check the four cardinal directions adjacent 
        to that point. (makes a list of those and choose randomly between them)
        Keeps guessing from those 4 directions until it gets another hit. Keep 
        guessing in those directions until it sinks the ship. Otherwise, if 
        there has been no hit, then it guesses based on probability function. """

        if self.successfulHits != []:
            chosenHitLocation = random.choice(range(len(self.successfulHits)))
            chosenHitCoordinate = self.successfulHits[chosenHitLocation]
            row = chosenHitCoordinate[0]
            col = chosenHitCoordinate[1]
            if (row, col) in self.available_guesses:
                self.available_guesses.remove((row, col))
            advantageous_moves = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            for x in range(len(advantageous_moves)):
                if advantageous_moves[x] in self.available_guesses:
                    if advantageous_moves[x] not in self.available_adv_moves:
                        self.available_adv_moves += [advantageous_moves[x]]
            if self.available_adv_moves == []:
                self.successfulHits.remove((row, col))
                #subtracted the guessed hit from successful hits
                guess = self.ai_just_lookin()
            else:
                guess_loc = random.choice(range(len(self.available_adv_moves)))
                guess = self.available_adv_moves[guess_loc]
                self.available_adv_moves.remove((guess))
                self.available_guesses.remove((guess))
                
                
        #Check if there's a hit, and look at the coordinates of that hit
        #If there is a hit, save the cardinal direction coordinates around that hit in a list: 
        #[(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        #Make a random guess from that list for the next move, and subtract that coordinate from available guesses
        #else statement: if no move is advantageous (e.g. no hit), resort to probability density function
        else:
            guess = self.ai_just_lookin()
        
        return guess

    def take_shot(self, r, c):
        """in: r is a row c is a col
           out: mutates the board to an * if there's a hit, X otherwise, returns True if the r and c is a hit
        """
        if self.data[r][c] == 'S' or self.data[r][c] =='A' or self.data[r][c] =='B' or self.data[r][c] =='D' or self.data[r][c] =='C':
            self.data[r][c] = '*'
            self.opp_data[r][c] = '*'
            self.successfulHits += [(r, c)]
            return True
        if self.data[r][c] == 'O':
            self.data[r][c] = 'X'
            self.opp_data[r][c] = 'X'
            return False
        return False
        
    def prob_density(self):
        """in: v5 true if destroyer isnt sunk, v4 if the four one isnt sunk, so on
           out: returns prob density of self.data by iterating ship placement across the board
        """
        denisty_graph = [[0 for i in range(self.width)] for j in range(self.height)]
        #destoryer
        if self.v5 == True:
            #with vert placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i+(5-1), j,5):
                        for k in range(5-1):
                            denisty_graph[i+k][j] += 1
            #with horiz placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i, j+(5-1),5):
                        for k in range(5-1):
                            denisty_graph[i][j+k] += 1
        

        #under that 
        if self.v4 == True:
            #with vert placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place(i,j,i+(4-1), j,4):
                        for k in range(4-1):
                            denisty_graph[i+k][j] += 1
            #with horiz placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i, j+(4-1),4):
                        for k in range(4-1):
                            denisty_graph[i][j+k] += 1


        #hell if i know
        if self.v3 == True:
            #with vert placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i+(3-1), j,3):
                        for k in range(3-1):
                            denisty_graph[i+k][j] += 1
            #with horiz placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i, j+(3-1),3):
                        for k in range(3-1):
                            denisty_graph[i][j+k] += 1

        #under that
        if self.v33 == True:
            #with vert placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i+(3-1), j,3):
                        for k in range(3-1):
                            denisty_graph[i+k][j] += 1
            #with horiz placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i, j+(3-1),3):
                        for k in range(3-1):
                            denisty_graph[i][j+k] += 1


        #lil baby
        if self.v2 == True:
            #with vert placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i+(2-1), j,2):
                        for k in range(2-1):
                            denisty_graph[i+k][j] += 1
            #with horiz placement
            for i in range(self.width): #rows
                for j in range(self.height): #cols
                    if self.can_place_for_opp(i,j,i, j+(2-1),2):
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
    
    def ai_move(self):
        if not self.has_hot:
            shot = (self.ai_just_lookin()[0],self.ai_just_lookin()[1])
            if self.take_shot(shot[0],shot[1]):
                self.has_hot = True
                self.hot_zone = shot
                print('hit')
    
    def sunk_ship(self):  
        """checks if each ship is sunk or not and tells the player"""    
        if "A" not in repr(self.data):
            self.v5 = False
            print("Aircraft carrier sunk.")
            
        if "B" not in repr(self.data):
            self.v4 = False
            print("Battleship sunk.")
        
        if "C" not in repr(self.data):
            self.v3 = False
            print("Cruiser sunk.")
        
        if "S" not in repr(self.data):
            self.v33 = False
            print("Submarine sunk.")
            
        if "D" not in repr(self.data):
            self.v2 = False
            print("Destroyer sunk.")

    def host_game(self):
        """runs the game"""
        print("Welcome to Battleship! Please place your ships.")
        playerBoard = Board()
        aiBoard = Board()
        playerhits = Board()
        aiBoard.ai_board()
        playerBoard.init_game()
        print('Your Targets')
        aiBoard.show_opp_data()
            
        while True: 
            #user takes a shot at the AI 
            while True:
                try:
                    user_shot_row = int(input("Which row would you like to target? "))
                except:
                    user_shot_row = 20
                try:
                    user_shot_col = int(input("Which column would you like to target? "))
                except:
                    user_shot_col = 20

                if (0 <= user_shot_row <=7) and (0 <= user_shot_col <=7):
                    break
                else:
                    print("those aren't valid inputs")

            shot = aiBoard.take_shot(user_shot_row, user_shot_col)
            print(' ')
            aiGuess = playerBoard.aiGuess()
            #Ai takes a shot at the player
            ai_shot_row = aiGuess[0]
            ai_shot_col = aiGuess[1]
            ai_shot = playerBoard.take_shot(ai_shot_row, ai_shot_col)
            playerhits.take_shot(ai_shot_row, ai_shot_col)
            print(' ')
            print("Your Ships")
            print(playerBoard)
            if ai_shot == True:
                print("You were hit at", ai_shot_row, ai_shot_col)
            else:
                print("Your opponent missed!")
            playerBoard.sunk_ship()

            print(' ')
            print('Your Targets')
            aiBoard.show_opp_data()

            if shot == True:
                print('You got a hit!')
                print(' ')
            else:
                print('You missed. Better luck next time!')
            aiBoard.sunk_ship()

            if playerBoard.v5 == False and playerBoard.v4 ==  False and playerBoard.v3 == False and playerBoard.v33 == False and playerBoard.v2 == False:
                print("They have sunk all of your ships. You have lost. Play again?")
                self.ai_wins += 1
                return
            
            if aiBoard.v5 == False and aiBoard.v4 ==  False and aiBoard.v3 == False and aiBoard.v33 == False and aiBoard.v2 == False:
                print("You have sunk all of their ships. Congratulations! Play again?")
                self.player_wins += 1
                return  
    def ai_vs_ai(self):
        """plays a game between two ais rewarding wins to the player if ai1 wins."""
        ai1Board = Board()
        ai2Board = Board()
        ai1Board.ai_board()
        ai2Board.ai_board()
        while True:
            ai1Guess = ai2Board.aiGuess() 
            ai1_shot_row = ai1Guess[0]
            ai1_shot_col = ai1Guess[1]
            ai1_shot = ai2Board.take_shot(ai1_shot_row, ai1_shot_col)
            print('ai1 guesses:', ai1Guess)
            time.sleep(.5)

            ai2Guess = ai1Board.aiGuess() 
            ai2_shot_row = ai2Guess[0]
            ai2_shot_col = ai2Guess[1]
            ai2_shot = ai1Board.take_shot(ai2_shot_row, ai2_shot_col)
            print('ai2 guesses:', ai2Guess)
            time.sleep(.5)

            print('this leaves ai1 board as:')
            print(ai1Board)
            print(' ')
            print('and ai2:')
            print(ai2Board)
            
            ai1Board.sunk_ship()
            ai2Board.sunk_ship()

            if ai1Board.v5 == False and ai1Board.v4 ==  False and ai1Board.v3 == False and ai1Board.v33 == False and ai1Board.v2 == False:
                print("You have sunk all of their ships. Congratulations! Play again?")
                self.ai_wins += 1
                return
            
            if ai2Board.v5 == False and ai2Board.v4 ==  False and ai2Board.v3 == False and ai2Board.v33 == False and ai2Board.v2 == False:
                print("You have sunk all of their ships. Congratulations! Play again?")
                self.player_wins += 1
                return  

    def save_files(self,filename):
        f = open(filename, 'w')
        print(self.player_wins, file = f)
        print(self.ai_wins, file = f)
        f.close()
        print(filename, 'saved.')

    def load_game(self, filename):
        f = open(filename, 'r')
        self.player_wins = int(f.readline())
        self.ai_wins = int(f.readline())
        f.close()
        print(filename,'loaded.')






def menu():
    """starts the menu"""
    b = Board()
    while True:
        print('Hello. Welcome to Battleship, please select:')
        print('(1) Play a new game')
        print('(2) See current score')
        print('(3) Load a past session')
        print('(4) Save current session')
        print("(5) Have two ai's battle it out, you'll receive a win if ai one wins")
        while True:
            try:
                choice = int(input('selection: '))
                break
            except:   
                print('not a valid selection')
        if choice == 1:
            b.host_game()

        elif choice == 2:
            print('The current score is, you:',b.player_wins,'computer:',b.ai_wins)
        elif choice == 3:
            file = input('What was the filename? ')
            b.load_game(file)
        elif choice == 4:
            file = input('What will you name the file? ')
            b.save_files(file)
        elif choice == 5:
            b.ai_vs_ai()
        print()
menu()
