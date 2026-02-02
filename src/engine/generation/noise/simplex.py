"""
Módulo de simplex noise para geração procedural do mundo.
"""

import opensimplex

class SimplexNoise:
    """
    Classe para gerar ruído simplex em 2D e 3D.
    """

    def __init__(self, seed: int):
        self.noise = opensimplex.OpenSimplex(seed)

    def noise2d(self, x: float, y: float) -> float:
        """
        Gera ruído simplex 2D para as coordenadas fornecidas.

        :param x: Coordenada X.
        :param y: Coordenada Y.
        :return: Valor do ruído entre -1 e 1.

        Examples:
            >>> noise = SimplexNoise(seed=42)
            >>> value = noise.noise2d(x=10.5, y=20.3)
            >>> print(value)
            0.123456789

        """
        return self.noise.noise2d(x, y)

    def noise3d(self, x: float, y: float, z: float) -> float:
        """
        Gera ruído simplex 3D para as coordenadas fornecidas.

        :param x: Coordenada X.
        :param y: Coordenada Y.
        :param z: Coordenada Z.
        :return: Valor do ruído entre -1 e 1.

        Examples:
            >>> noise = SimplexNoise(seed=42)
            >>> value = noise.noise3d(x=10.5, y=20.3, z=5.7)
            >>> print(value)
            0.123456789s
        """
        return self.noise.noise3d(x, y, z)