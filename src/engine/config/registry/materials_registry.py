"""
Docstring for src.engine.world.materials.materials_registry

Módulo para registrar e gerenciar materiais no mundo procedural.

Pega da pasta materials e extrai os conteúdos no formato yaml
para facilitar o acesso e a manipulação dos materiais.
"""

from typing import Dict
from src.engine.config.loaders.loader import DirectoryLoader, FileLoader
from src.engine.config.registry.base_registry import BaseRegistry


class MaterialsRegistry(BaseRegistry):
    """
    Classe para registrar e gerenciar materiais no mundo procedural.
    """

    def __init__(self):
        """
        Inicializa o registro de materiais e o loader de arquivos.
        """
        self.materials: Dict[str, dict] = {}
        self.file_loader: FileLoader = FileLoader()
        self.directory_loader: DirectoryLoader = DirectoryLoader()
    
    def load_material_from_loader(self, file_path: str) -> None:
        """
        Carrega único arquivo de material de um loader e os registra no registro.

        Args:
            file_path (str): Caminho para o arquivo de material.

        Returns:
            None

        Usage:
            registry = MaterialsRegistry()
            registry.load_material_from_loader("path/to/material.yaml")
        """
        material_data = self.file_loader.load(file_path)
        self.register_material(material_data["id"], material_data)


    def load_materials_from_directory(self, dir_path: str) -> None:
        """
        Carrega múltiplos arquivos de materiais de um diretório e os registra no registro.

        :param dir_path: Caminho para o diretório contendo arquivos de materiais.
        """
        materials_data = self.directory_loader.load(dir_path)
        
        for material_id, material_data in materials_data.items():
            self.register_material(material_id, material_data)

    def register(self, material_id: str, material_data: dict,*, overwrite: bool = False) -> None:
        """
        Registra um novo material no registro.

        :param material_id: ID único do material.
        :param material_data: Dados do material em formato de dicionário.
        """
        # Verificar se não estou sobrescrevendo um material existente
        if material_id in self.materials and not overwrite:
            raise ValueError(f"Material com ID '{material_id}' já está registrado.")
        self.materials[material_id] = material_data
            
    def get_material(self, material_id: str) -> dict:
        """
        Recupera os dados de um material pelo seu ID.

        :param material_id: ID do material a ser recuperado.
        :return: Dados do material em formato de dicionário.
        """
        return self.materials.get(material_id, None)

    def get_materials_list(self,list_material_ids: list) -> dict:
        """
        Recupera uma lista de materiais pelo seus IDs.

        :param list_material_ids: Lista de IDs dos materiais a serem recuperados.
        :return: Dicionário com os dados dos materiais.
        """
        materials_dict = {}
        for material_id in list_material_ids:
            material_data = self.get_material(material_id)
            if material_data:
                materials_dict[material_id] = material_data
        return materials_dict