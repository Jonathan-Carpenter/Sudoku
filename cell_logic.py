from time import sleep

class Cell:
    def __init__(self, pos, master, entry=None):
        self.entry = entry
        self.pos = pos
        self.master = master

    def __str__(self):
        if self.entry == None:
            return ""
        else:
            return str(self.entry)

    def __eq__(self, other):
        if other == None or self.entry == None or other.entry == None: return False
        return self.entry == other.entry

    def isValid(self):
        r, c = self.pos[0], self.pos[1]

        exclusives = (self.master.get_row(r)
                    + self.master.get_col(r, c)
                    + self.master.get_square(r, c))

        for cell in exclusives:
            if self == cell and cell.pos != self.pos:
                return False
        return True

    def get_valids(self):
        r, c = self.pos[0], self.pos[1]

        # print("Getting valid entries for {}".format((r,c)))

        exclusives = (self.master.get_row(r)
                    + self.master.get_col(r, c)
                    + self.master.get_square(r, c))

        valids = set([1,2,3,4,5,6,7,8,9])
        for cell in exclusives:
            if cell.entry in valids: valids.remove(cell.entry)
        return list(valids)

class GUICell(Cell):
    def __init__(self, pos, master, widget=None, default_colour=None):
        super().__init__(pos, master)
        self.widget = widget

        if default_colour == None: self.default_colour = self.master.known_colour
        else: self.default_colour = default_colour

        self.set_colour(default_colour)

    def set_colour(self, colour):
        if self.widget != None:
            self.widget["bg"] = colour
            self.widget.update()

    def set_entry(self, num):
        self.master.active_cell = None

        if num == "0":
            self.clear()
            return

        self.widget["text"] = num
        self.entry = int(float(num))

        if self.isValid():
            self.set_colour(self.default_colour)
        else:
            self.set_colour(self.master.invalid_colour)
            sleep(1)
            self.clear()

    def clear(self):
        self.entry = None
        self.widget["bg"] = self.default_colour
        self.widget["text"] = ""
