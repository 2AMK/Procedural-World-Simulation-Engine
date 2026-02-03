"""
Atua como interface base para carregadores de arquivos de configuração.
"""
import os
from typing import Union, Dict, Any
import abc

class BaseFileLoader(abc.ABC):
    """
    Classe abstrata base para carregadores de arquivos de configuração.
    Define a interface que todos os carregadores devem implementar.
    """
    
    @abc.abstractmethod
    def load_file(self, path: Union[str, os.PathLike]) -> Dict[str, Any]:
        """
        Método abstrato para carregar um arquivo de configuração.

        Args:
            path (str): Caminho para o arquivo de configuração.

        Returns:
            dict: Conteúdo carregado como um dicionário.
        """
        pass


class BaseDirectoryLoader(abc.ABC):
    """
    Classe abstrata base para carregadores de diretórios de configuração.
    Define a interface que todos os carregadores de diretórios devem implementar.
    """
    
    @abc.abstractmethod
    def load_directory(self, path: Union[str, os.PathLike]) -> Dict[str, Any]:
        """
        Método abstrato para carregar todos os arquivos de configuração em um diretório.

        Args:
            path (str): Caminho para o diretório de configuração.

        Returns:
            dict: Conteúdo carregado como um dicionário.
        """
        pass