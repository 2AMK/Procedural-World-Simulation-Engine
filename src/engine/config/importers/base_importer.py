"""
Módulo que define a classe base para importadores de configuração.
Essa classe serve como uma interface para todos os importadores de configuração,
"""

from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseImporter(ABC):
    """
    Classe base abstrata para os importadores que recebem 
    os dados dos loaders e passam para os registries.
    """

    @abstractmethod
    def __init__(self):
        """
        Deve inicializar o File/DirectoryLoader aqui.
        """
        pass

    @abstractmethod
    def import_one(self, items: Dict[str,Any]) -> None:
        """
        Método abstrato para importar um único item.

        Args:
            items (Dict[str, Any]): Dicionário contendo os dados do item a ser importado.
        """
        pass

    @abstractmethod
    def import_many(self, items: Dict[str,Any]) -> None:
        """
        Método abstrato para importar múltiplos itens.

        Args:
            items (Dict[str, Any]): Dicionário contendo os dados dos itens a serem importados.
        """
        for item in items.values():
            self.import_one(item)