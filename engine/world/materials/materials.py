"""
Docstring for engine.world.materials.materials

Módulo para definir os materiais e suas propriedades para a geração de mundo

"""

class Material:
    """
    Classe que representa um material com nome, densidade e resistência.

    Atua como contrato para os demais materiais no mundo.

    """
    # Inicializa o material com nome, densidade e resistência.
    def __init__(self, id, name, density, strength, inflamability):
        self.id = id
        self.name = name
        self.density = density
        self.strength = strength
        self.inflamability = inflamability # Define se o material é inflamável ou não.


