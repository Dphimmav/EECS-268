class BoardGame:
    def __init__(self, name, gibbonsrating, baverage, avgweight, yearpublished, bggbestplayers):
        self.name = name
        self.gibbonsrating = gibbonsrating
        self.baverage = baverage
        self.avgweight = avgweight
        self.yearpublished = yearpublished
        self.bggbestplayers = bggbestplayers

    #def __str__(self):
     #   return f'============\n{self.name}\n{self.gibbonsrating}\n{self.baverage}\n{self.avgweight}\n{self.yearpublished}\n{self.bggbestplayers}\n============'
    #def __repr__(self):
     #  return f"============\n(name='{self.name}', gibbons_rating={self.gibbonsrating}, average_rating={self.baverage}, average_weight={self.avgweight}, year_published={self.yearpublished}, best_players={self.bggbestplayers})"
