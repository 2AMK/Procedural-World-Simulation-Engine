"""
Módulo utilitário para carregamento de arquivos YAML.

Esse módulo visa facilitar a leitura e manipulação de arquivos YAML, 
fornecendo funções para carregar e validar o conteúdo desses arquivos.

Utiliza a biblioteca 'pyaml' para o processamento dos arquivos YAML.

A ideia é usar esse módulo em outras partes do motor,
como no registro de materiais, camadas de geração, biomas, etc.
"""
import os
from typing import Any, Dict, Union
import yaml

from src.engine.config.loaders.base_loader import BaseFileLoader, BaseDirectoryLoader

class YamlFileLoader(BaseFileLoader):
    """
    Classe utilitária para carregar arquivos YAML.
    """
    def __init__(self):
        pass

    # Usando método estático para facilitar o uso sem instanciar a classe
    @staticmethod
    def _check_file_format(file_path: Union[str, os.PathLike]) -> bool:
        """
        Verifica se o arquivo possui a extensão YAML válida.

        Args:
            file_path (str): Caminho para o arquivo.

        Returns:
            bool: True se o arquivo for YAML, False caso contrário.
        """
        file_path = os.fspath(file_path)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")
            

        if not os.path.isfile(file_path):
            raise ValueError(f"O caminho {file_path} não é um arquivo válido.")
        
        extracted_extension = os.path.splitext(file_path)[1].lower()
        return extracted_extension == '.yaml' or extracted_extension == '.yml'

    @staticmethod
    def load_file(file_path: Union[str, os.PathLike]) -> Dict[str, Any]:
        """
        Carrega um arquivo YAML e retorna seu conteúdo como um dicionário.

        Args:
            file_path (str): Caminho para o arquivo YAML.

        Returns:
            dict: Conteúdo do arquivo YAML como um dicionário.
        """
        file_path = os.fspath(file_path)

        if not YamlFileLoader._check_file_format(file_path):
            raise ValueError(f"O arquivo {file_path} não é um arquivo YAML válido.")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)

        # Tratamento de exceções para erros comuns ao carregar arquivos YAML        
        except (PermissionError, FileNotFoundError, ValueError, yaml.YAMLError) as e:
            print(f"Erro ao carregar o arquivo {file_path}: {e}")
            raise e

        if data is None:
            return {}

        if not isinstance(data, dict):
            raise ValueError(f"O arquivo {file_path} não possui um YAML no formato de mapeamento (dict).")

        return data
    

class YamlDirectoryLoader(BaseDirectoryLoader):
    """
    Classe utilitária para carregar todos os arquivos YAML em um diretório.
    Utiliza a classe YamlFileLoader para carregar cada arquivo individualmente.
    """
    def __init__(self):
        self.yaml_loader = YamlFileLoader()
       

    def load_directory(self, directory_path: Union[str, os.PathLike]) -> Dict[str, Any]:
        """
        Carrega todos os arquivos YAML em um diretório e retorna um dicionário
        com o nome do arquivo (sem extensão) como chave e o conteúdo como valor.
        
        Args:
            directory_path (str): Caminho para o diretório contendo arquivos YAML.

        Returns:
            Dict[str, Any]: Dicionário com o conteúdo dos arquivos YAML.

        Examples:
            >>> yaml_data = YamlLoader.load_yaml_directory('config/yamls')
            >>> print(yaml_data['example'])  # Acessa o conteúdo do example.yaml
            
        """
        directory_path = os.fspath(directory_path)
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"O diretório {directory_path} não foi encontrado.")
        if not os.path.isdir(directory_path):
            raise ValueError(f"O caminho {directory_path} não é um diretório válido.")

        yaml_data = {}
        for filename in os.listdir(directory_path):
            try:
                file_path = os.path.join(directory_path, filename)
                extracted_extension = os.path.splitext(file_path)[1].lower()
                if extracted_extension not in ('.yaml', '.yml'):
                    continue
                data = self.yaml_loader.load_file(file_path)
                key = os.path.splitext(filename)[0]
                yaml_data[key] = data
            except (PermissionError, FileNotFoundError) as e:
                print(f"Erro ao carregar o arquivo {filename}: {e}")
        return yaml_data