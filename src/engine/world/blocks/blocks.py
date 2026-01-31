"""
Módulo que define os blocos do mundo
Atualmente em progresso
"""

class Block:
    """
    Classe que representa um bloco no mundo 
    """

    def __init__(self, loc_x, loc_y, loc_z, material, state = None):
        self.material = material
        self.state = state  # Estado do bloco (atualmente opcional)
        
        # Posicao no espaco tridimensional do mundo
        # loc_x, loc_y, loc_z sao as coordenadas x
        self.loc_x = loc_x
        self.loc_y = loc_y 
        self.loc_z = loc_z
        # Adicionar mais atributos conforme necessário

