"""
Docstring for src.engine.world.materials.materials_registry

Módulo para registrar e gerenciar materiais no mundo procedural.

Pega da pasta materials e extrai os conteúdos no formato yaml
para facilitar o acesso e a manipulação dos materiais.
"""

from typing import Dict
from src.engine.world.materials import materials
from src.utils.yaml_loader import load_yaml_file


class MaterialsRegistry:
    """
    Classe para registrar e gerenciar materiais no mundo procedural.
    """

    def __init__(self):
        """
        Inicializa o registro de materiais.
        """
        self.materials: Dict[str, dict] = {}

    def load_materials_from_yaml(self, file_path: str) -> None:
        """
        Carrega materiais de um arquivo YAML e os registra no registro.

        :param file_path: Caminho para o arquivo YAML contendo os materiais.
        """
        self.materials.data = load_yaml_file(file_path)
        for materials_id, material_data in self.materials.data.items():
            self.register_material(materials_id, material_data)
            
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
