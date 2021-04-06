class PlaneSeating:
    plane_list = []
    rows = 0
    groups_list = []
    groups = 0

    def __init__(self, _filename=None):
        self.read_file(_filename)
        self.default_message = "Passengers can take seats: "
        self.reject_message = "Cannot fulfill passengers requirements"

    def read_file(self, _filename):
        plane_list = []
        groups_list = []
        with open(_filename, 'r') as f:
            n = int(f.readline())
            self.rows = int(n)
            while n != 0:
                plane_list.append(f.readline())
                n -= 1
            m = int(f.readline())
            self.groups = int(m)
            while m != 0:
                groups_list.append(f.readline())
                m -= 1
        self.plane_list = plane_list
        self.groups_list = groups_list

    def print_board(self):
        for row in self.plane_list:
            for column in row:
                print(column, end='')

    def define_free_seats(self, group: str):
        seats_in_row = {0: "A", 1: "B", 2: "C", 4: "D", 5: "E", 6: "F"}
        if "left" in group:
            if "aisle" in group:
                if "1" in group:
                    pos_to_search = [2]
                elif "2" in group:
                    pos_to_search = [1, 2]
                else:
                    pos_to_search = [0, 1, 2]
            else:   # window
                if "1" in group:
                    pos_to_search = [0]
                elif "2" in group:
                    pos_to_search = [0, 1]
                else:
                    pos_to_search = [0, 1, 2]
        else:  # right
            if "aisle" in group:
                if "1" in group:
                    pos_to_search = [4]
                elif "2" in group:
                    pos_to_search = [4, 5]
                else:
                    pos_to_search = [4, 5, 6]
            else:   # window
                if "1" in group:
                    pos_to_search = [6]
                elif "2" in group:
                    pos_to_search = [5, 6]
                else:
                    pos_to_search = [4, 5, 6]
        k = 0
        found = False
        while k != self.rows:
            row = self.plane_list[k]
            pos_of_free = [i for i, j in enumerate(row) if j == '.']
            if set(pos_to_search).issubset(set(pos_of_free)):
                min_val, max_val = min(pos_to_search), max(pos_to_search)
                self.plane_list[k] = self.plane_list[k][:min_val] + 'X'*len(pos_to_search) + self.plane_list[k][max_val+1:]
                found = True
                break
            k += 1
        if found:
            seats = str()
            for el in pos_to_search:
                seats += str(k+1) + seats_in_row[el] + ' '
            print(self.default_message + seats[:-1])
            self.print_board()
            self.put_another_sign(k, min_val, max_val, pos_to_search)
        else:
            print(self.reject_message)

    def put_another_sign(self, pos: int, min_val: int, max_val: int, pos_to_search: []):
        self.plane_list[pos] = self.plane_list[pos][:min_val] + '#' * len(pos_to_search) + self.plane_list[pos][max_val+1:]

    def run(self):
        i = 0
        while i != self.groups:
            self.define_free_seats(self.groups_list[i])
            i += 1


filename = "input.txt"
plane = PlaneSeating(filename)
plane.run()
