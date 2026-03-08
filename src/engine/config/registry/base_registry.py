"""
Esse módulo atua como um template method para registries 
para padronizar a criação de registries no motor.
Ele define a estrutura básica e os métodos que todos 
os registries devem implementar.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseRegistry(ABC):
    """
    Classe base abstrata para todos os registries no motor.
    Define a estrutura básica e os métodos que todos os registries devem implementar.
    """

    def __init__(self):
        # Dicionário para armazenar os itens registrados
        self._registry: Dict[str, Any] = {}

    @abstractmethod
    def register(self, item_id: str, item_data: Any) -> None:
        """
        Registra um novo item no registry.

        Args:
            item_id (str): ID único do item.
            item_data (Any): Dados do item a ser registrado.
        """
        pass

    @abstractmethod
    def get(self, item_id: str) -> Any:
        """
        Recupera os dados de um item pelo seu ID.

        Args:
            item_id (str): ID único do item.

        Returns:
            Any: Dados do item registrado.
        """
        pass

    @abstractmethod
    def validate_schemas(self) -> bool:
        """
        Valida os dados registrados contra seus schemas definidos.

        Returns:
            bool: True se todos os dados forem válidos, False caso contrário.
        """
        pass