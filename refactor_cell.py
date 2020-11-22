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
        return self.entry == other.entry

    def isValid(self):
        r, c = self.pos[0], self.pos[1]

        exclusives = (self.master.getRow(r)
                    + self.master.getCol(c)
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
    def __init__(self, widget=None, default_colour=None):
        super().__init__()
        self.widget = widget

        if default_colour == None: default_colour = self.master.default_colour
        else: self.default_colour = default_colour

        self.current_colour = default_colour
