"""
Docstring for engine.world.chunks.chunks

Esse módulo configura o chunk do mundo procedural.
Chunks são partes discretas do mundo que podem ser geradas e carregadas de forma independente.

Visa melhorar o performance da simulação ao dividir o mundo em várias partes pequenas. 

Armazena uma lista de blocos e seus respectivos coordenadas no espaço tridimensional do mundo.
"""

class Chunk:
    """
    Classe que representa um chunk no mundo
    
    Um chunk é uma parte discretizada do mundo, contendo blocos e informações relevantes.
    """
    # Atualmente em progresso. Haverá mais adições em breve.
    def __init__(self, x,z):
        self.x = x
        self.z = z