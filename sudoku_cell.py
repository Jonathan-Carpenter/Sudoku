from warnings import warn

class Cell:
    def __init__(self, val=None, entry=None, revealed=True):
        self.val = val
        self.revealed = revealed
        self.entry = entry

        if self.revealed: self.reveal()

    def __str__(self):
        if self.entry == None:
            return ' '
        else:
            return str(self.entry)

    def __eq__(self, other):
        if self.entry==None or other.entry==None:
            warn("__eq__ tests equality on cell entries, not cell values. One or more cell entries are None.")
        return self.entry == other.entry

    def enter(self, entry):
        if not self.revealed: self.entry = entry

    def reveal(self):
        self.entry = self.val
        self.revealed = True

    def unreveal(self):
        self.entry = None
        self.revealed = False
