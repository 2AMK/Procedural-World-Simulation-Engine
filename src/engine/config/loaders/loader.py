"""
Um Adaptador base para carregadores de arquivos, aceitando vários formatos.
"""

from typing import Union, Dict, Any
import os

from src.engine.config.loaders.yaml_loader import YamlFileLoader, YamlDirectoryLoader

class FileLoader:
    """
    Uma interface unificada para carregar arquivos de diferentes formatos.
    """

    def __init__(self):
        self.loaders = {
            '.yaml': YamlFileLoader,
            '.yml': YamlFileLoader,
            # Outros formatos podem ser adicionados aqui
        }
    def load(self, file_path: Union[str, os.PathLike]) -> Dict[str, Any]:
        """
        Carrega um arquivo usando o carregador apropriado com base na extensão do arquivo.

        Args:
            file_path (str): Caminho para o arquivo a ser carregado.

        Returns:
            dict: Conteúdo do arquivo carregado como um dicionário.
        """
        file_path = os.fspath(file_path)
        extension = os.path.splitext(file_path)[1].lower()

        loader_class = self.loaders.get(extension)
        if not loader_class:
            raise ValueError(f"Nenhum carregador disponível para a extensão de arquivo: {extension}")

        loader = loader_class()
        return loader.load_file(file_path)
    
class DirectoryLoader:
    def __init__(self):
        self.loaders = {
            '.yaml': YamlDirectoryLoader,
            '.yml': YamlDirectoryLoader,
            # Outros formatos podem ser adicionados aqui
        }
    def load(self, dir_path: Union[str, os.PathLike]) -> Dict[str, Any]:
        """
        Carrega todos os arquivos em um diretório usando o carregador apropriado com base na extensão dos arquivos.
        
        Args:
            dir_path (str): Caminho para o diretório contendo arquivos de configuração.

        Returns:
            dict: Dicionário com os dados carregados de todos os arquivos.
        """
        dir_path = os.fspath(dir_path)
        
        if not os.path.isdir(dir_path):
            raise ValueError(f"O caminho {dir_path} não é um diretório válido.")
        
        # Para diretórios, usamos YamlDirectoryLoader por padrão
        # pois ele processa todos os arquivos .yaml/.yml no diretório
        loader = YamlDirectoryLoader()
        return loader.load_directory(dir_path)