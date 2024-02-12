from perlin_noise import PerlinNoise

class Background:
    def __init__(self, x: int = 100, y: int = 100, octaves: int = 6, seed: int = None) -> None:
        self.x = x
        self.y = y
        self.octaves = octaves
        self.seed = seed

    def generate_map(self):
        noise = PerlinNoise(octaves=self.octaves, seed=self.seed)
        height_map = [[noise([i/self.x, j/self.y]) for j in range(self.x)] for i in range(self.y)]
        return height_map
