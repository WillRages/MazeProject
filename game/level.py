class Level:

    def __init__(self, horizontal_walls: list[str], vertical_walls: list[str],
                 collectibles: dict[tuple[int, int], str], spawnpoint: tuple[int, int],
                 enemies: list[tuple[int, int]], lava: list[tuple[int, int]],
                 exit: tuple[int, int], instructions: str):
        self.horizontal_walls = horizontal_walls
        self.vertical_walls = vertical_walls
        self.collectibles = collectibles
        self.spawnpoint = spawnpoint
        self.enemies = enemies
        self.lava = lava
        self.exit = exit
        self.instructions = instructions

    def __str__(self):
        return f'Level with\
        spawnpoint: {self.spawnpoint},\
        exit: {self.exit},\
        instructions: {self.instructions}'

    def __repr__(self):
        return f'Level(\
        {self.vertical_walls},\
        {self.horizontal_walls},\
        {self.collectibles},\
        {self.spawnpoint},\
        {self.enemies},\
        {self.lava},\
        {self.exit},\
        {self.instructions})'
