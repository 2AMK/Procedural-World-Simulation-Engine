"""
Módulo de noise Perlin para geração procedural do mundo.
"""


from noise import pnoise2, pnoise3

class PerlinNoise:
    """
    Gera ruído Perlin em 2D e 3D.
    """
    def __init__(self, seed: int):
        self.seed = seed

    def noise2d(self, 
                x: float, 
                y: float, 
                scale: float = 1.0, 
                octaves: int = 1, 
                persistence: float = 0.5, 
                lacunarity: float = 2.0) -> float:
        """
        Gera ruído Perlin 2D para as coordenadas fornecidas.

        Args:
            x (float): Coordenada X.
            y (float): Coordenada Y.
            scale (float): Escala do ruído.
            octaves (int): Número de oitavas.
            persistence (float): Persistência do ruído.
            lacunarity (float): Lacunaridade do ruído.

        Returns:
            float: Valor do ruído entre -1 e 1.

        Usages:
            >>> noise = PerlinNoise(seed=42)
            >>> value = noise.noise2d(x=10.5, y=20.3, scale=0.1, octaves=4)
            >>> print(value)
            0.123456789

        """

        return pnoise2(x * scale,
                       y * scale,
                       octaves=octaves,
                       persistence=persistence,
                       lacunarity=lacunarity,
                       repeatx=1024,
                       repeaty=1024,
                       base=self.seed)
    
    def noise3d(self,
                x: float,
                y: float,
                z: float,
                scale: float = 1.0,
                octaves: int = 1,
                persistence: float = 0.5,
                lacunarity: float = 2.0) -> float:
        """
        Gera ruído Perlin 3D para as coordenadas fornecidas.

        Args:
            x (float): Coordenada X.
            y (float): Coordenada Y.
            z (float): Coordenada Z.
            scale (float): Escala do ruído.
            octaves (int): Número de oitavas.
            persistence (float): Persistência do ruído.
            lacunarity (float): Lacunaridade do ruído.
        Returns:
            float: Valor do ruído entre -1 e 1.
        Usages:
            >>> noise = PerlinNoise(seed=42)
            >>> value = noise.noise3d(x=10.5, y=20.3, z=15.7, scale=0.1, octaves=4)
            >>> print(value)
            0.123456789
        """

        return pnoise3(x * scale,
                       y * scale,
                       z * scale,
                       octaves=octaves,
                       persistence=persistence,
                       lacunarity=lacunarity,
                       repeatx=1024,
                       repeaty=1024,
                       repeatz=1024,
                       base=self.seed)