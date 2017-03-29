from test.test_ssl import handle_error

class Soduku_solver(object):
    class Square():
        def __init__(self, areas, index, set_queue, update_queue, print_matrix):
            self.areas = areas
            self.index = index
            self.set_queue = set_queue
            self.update_queue = update_queue
            self.print_matrix = print_matrix
            self.possibles = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            for area in self.areas:
                area.append(self)
        def no_possibles(self):
            return len(self.possibles)
        def possibles_set(self):
            return self.possibles
        def set(self, value):
            self.print_matrix[self.index[0]][ self.index[1]] = value
            for area in self.areas:
                area.remove(self)
                self.set_queue.append((value, area))
                
        def remove_possibles(self, possibles_set):
            prev_len = len(self.possibles)
            self.possibles = self.possibles - possibles_set
            if len(self.possibles) == 1:
                self.set(self.possibles.pop()) # We are all in from here...
            elif prev_len > len(self.possibles):
                self.dirty()
            
        def dirty(self):
            for area in self.areas:
                if not area in self.update_queue: 
                    self.update_queue.append(area)
                
    def __init__(self, board):
        self.update_queue = []
        self.set_queue = []
        self.board = board
        rows = [[],[],[],[],[],[],[],[],[]]
        cols = [[],[],[],[],[],[],[],[],[]]
        quadrants = [[],[],[],[],[],[],[],[],[]]
        
        
        for row_index in range(0,9):
            for col_index in range(0,9):
                current_areas = []
                current_areas.append(rows[row_index])
                current_areas.append(cols[col_index])
                current_areas.append(quadrants[calc_quadrant(row_index, col_index)])
                current_square = Soduku_solver.Square(current_areas, (row_index, col_index), self.set_queue, self.update_queue, self.board)
                if self.board[row_index][col_index] != 0:
                    current_square.set(self.board[row_index][col_index])
        self.areas = []
        for row in rows:
            self.areas.append(row)
        for col in cols:
            self.areas.append(col)
        for quadrant in quadrants:
            self.areas.append(quadrant)
        
    def pretty_print(self):
        print("------------------")
        for row in self.board:
            print(row)
                
    def solve_loop(self):
        if len(self.set_queue) > 0:
            self.handle_sets()
        for area in self.areas:
            self.handle_doubles(area)
            self.handle_onlyone(area)
        self.inner_solve_loop()
            
    def inner_solve_loop(self):
        if len(self.set_queue) > 0:
            self.handle_sets()
        for area in self.update_queue:
            self.update_queue.remove(area)
            self.handle_doubles(area)
            self.handle_onlyone(area)
        if len(self.set_queue) > 0 or len(self.update_queue) > 0:
            self.inner_solve_loop()       

    def handle_sets(self):
        for (value, area) in self.set_queue:
            self.set_queue.remove((value, area))
            value_set = set()
            value_set.add(value)
            for square in area:
                square.remove_possibles(value_set)
        if len(self.set_queue) > 0:
            self.handle_sets()     
        
    def handle_doubles(self, area):
        for a_square in area:
            if a_square.no_possibles() == 2:
                work_area = area[:]
                work_area.remove(a_square)
                for another_square in work_area:
                    if another_square.possibles_set() == a_square.possibles_set():
                        work_area.remove(another_square)
                        for square in work_area:
                            square.remove_possibles(a_square.possibles_set())
    def handle_onlyone(self, area):
        for a_square in area:
            possibles = a_square.possibles_set()
            for another_square in area:
                if another_square != a_square:
                    possibles = possibles - another_square.possibles_set()
            if len(possibles) == 1:
                a_square.remove_possibles(a_square.possibles_set() - possibles)
                
        
        
                        
        
def calc_quadrant(row, col):
    """ 
    012 R0(0-2)
    345 R1(3-5)
    678 R2(6-8) """
    row_part = int(row/3)*3
    col_part = int(col/3) 
    return row_part + col_part

if __name__ == "__main__":
    matrix = [
        [0,0,3,0,2,0,6,0,0],
        [9,0,0,3,0,5,0,0,1],
        [0,0,1,8,0,6,4,0,0],
        [0,0,8,1,0,2,9,0,0],
        [7,0,0,0,0,0,0,0,8],
        [0,0,6,7,0,8,2,0,0],
        [0,0,2,6,0,9,5,0,0],
        [8,0,0,2,0,3,0,0,9],
        [0,0,5,0,1,0,3,0,0]]
    s = Soduku_solver(matrix)
    s.pretty_print()
    s.solve_loop()
    s.pretty_print()
    








