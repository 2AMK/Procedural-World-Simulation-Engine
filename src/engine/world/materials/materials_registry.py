"""
Docstring for src.engine.world.materials.materials_registry

Módulo para registrar e gerenciar materiais no mundo procedural.

Pega da pasta materials e extrai os conteúdos no formato yaml
para facilitar o acesso e a manipulação dos materiais.
"""

from typing import Dict


class MaterialsRegistry:
    """
    Classe para registrar e gerenciar materiais no mundo procedural.
    """

    def __init__(self):
        self.materials: Dict[str, dict] = {}

    def register_material(self, material_id: str, material_data: dict) -> None:
        """
        Registra um novo material no registro.

        :param material_id: ID único do material.
        :param material_data: Dados do material em formato de dicionário.
        """
        self.materials[material_id] = material_data

    def get_material(self, material_id: str) -> dict:
        """
        Recupera os dados de um material pelo seu ID.

        :param material_id: ID do material a ser recuperado.
        :return: Dados do material em formato de dicionário.
        """
        return self.materials.get(material_id, None)
