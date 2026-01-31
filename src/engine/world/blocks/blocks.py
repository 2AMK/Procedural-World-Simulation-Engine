"""
Módulo que define os blocos do mundo
Atualmente em progresso
"""

from typing import Any


class Block:
    """
    Classe que representa um bloco no mundo 
    """

    def __init__(self, loc_x, loc_y, loc_z, material_id, state):
        loc_x: int
        loc_y: int
        loc_z: int
        material_id: str
        state: dict[str, Any]  # Estado do bloco (atualmente opcional)


        self.material_id = material_id
        self.state = state  # Estado do bloco (atualmente opcional)
        
        # Posicao no espaco tridimensional do mundo
        # loc_x, loc_y, loc_z sao as coordenadas x
        self.loc_x = loc_x
        self.loc_y = loc_y 
        self.loc_z = loc_z
        # Adicionar mais atributos conforme necessário

