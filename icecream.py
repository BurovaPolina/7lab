class Ice_cream:
    def __init__(self, name, quality, energy):
        self.name = name
        self.quality = quality
        self.energy = energy
    name = ''
    quality = ''
    energy = 0
    def __str__(self):
        return 'name:' + self.name + ' quality:' + self.quality + ' energy:' + str(self.energy)

