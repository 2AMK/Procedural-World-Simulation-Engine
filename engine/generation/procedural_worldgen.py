"""
Docstring for engine.generation.procedural_worldgen.py


Módulo de geração procedural do mundo que define as regras:
- Altura de terreno máximo e mínimo (configurável), baseada no noise procedural
- Geração de rios, montanhas, florestas, etc. com base em perlin noise ou outras técnicas.
- Camadas de terra, pedra, areia, etc


- Também deve ser possível ajustar parâmetros como semente, altura máxima, etc.
- Deve ser possível escolher tipo de geração (perlin, simplex, etc.)

Atualmente em progresso
"""
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple

from engine.world.blocks.blocks import Block
from engine.world.chunks.chunks import Chunk



@dataclass(frozen=True) # dataclass é usado como boilerplate/atalho para agilizar o classe de configuração
class WorldGenConfig:
    """ Definido por próprio usuário para gerar o mundo"""
    seed: int = 42 # semente determínistica
    chunk_size: int = 16 # número de bloco por lado em um chunk
    height_scale: int = 20 # altura máximo do terreno em bloco
    noise_scale: float = 1.0 # escala do noise procedural
    noise_type: str = 'perlin' # tipo de noise procedural (perlin, simplex, etc)
    max_height: int = 256 # altura absoluta do mundo em bloco



# ────────────────────────────────────────────────────────────────────────
#  WorldGen
# ────────────────────────────────────────────────────────────────────────

class WorldGen:
    """
    Docstring for WorldGen

    Gerador procedural de mundo. Utiliza configurações fornecidas para gerar um mundo tridimensional.

    Parametros:
    - config: Configuração do mundo a ser gerado.
    
    """

    # Inicializa o mundo com as configurações fornecidas
    def __init__(self, config: WorldGenConfig = WorldGenConfig()) -> None: # Esse método não deve ter retorno, assim como é denotado pelo None
        """
        Inicializa o mundo com as configurações fornecidas
        """
        self.config = config

        # Verifica se a configuração é válida, caso contrário retorne erro.
        # Adicionar mais verificações conforme necessário.
        if not isinstance(self.config, WorldGenConfig):
            raise ValueError("Invalid configuration type. Expected WorldGenConfig.")
    
        self.seed = config.seed
        self.noise_type = config.noise_type

    












