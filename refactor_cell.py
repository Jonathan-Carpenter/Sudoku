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

        exclusives = (self.master.getRow(r)
                    + self.master.getCol(r, c)
                    + self.master.getSquare(r, c))

        for cell in exclusives:
            if self == cell: return False
        return True

    def getValids(self):
        r, c = self.pos[0], self.pos[1]

        # print("Getting valid entries for {}".format((r,c)))

        exclusives = (self.master.getRow(r)
                    + self.master.getCol(r, c)
                    + self.master.getSquare(r, c))

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
        if self.widget != None: self.widget["bg"] = colour

    def set_entry(self, num):
        self.widget["text"] = num
        self.entry = int(float(num))

        if self.isValid():
            self.widget["bg"] = self.default_colour
        else:
            self.widget["bg"] = self.master.invalid_colour
            sleep(0.1)
            self.widget["bg"] = self.default_colour
            self.widget["text"] = ""
            self.entry = None
