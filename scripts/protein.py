class Protein:
    def __init__(self, id, sequence):
        self.id = id
        self.sequence = sequence

    def length(self):
        return len(self.sequence)

    def gc_content(self):
        g = self.sequence.count("G")
        c = self.sequence.count("C")
        return (g + c) / len(self.sequence)

    def __str__(self):
        return f"{self.id} | length={self.length()}"

