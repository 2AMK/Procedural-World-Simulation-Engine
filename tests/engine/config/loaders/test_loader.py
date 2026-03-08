"""
Teste unitário para o carregador de arquivos de materiais.

"""

import os
import pytest
import pathlib

from src.engine.config.loaders.loader import FileLoader, DirectoryLoader
from src.engine.config.loaders.yaml_loader import YamlFileLoader, YamlDirectoryLoader

class TestFileLoader:
    def test_valid_yaml_file(self, tmp_path):
        tmp_file = tmp_path / "material.yaml"
        tmp_file.write_text("id: stone\nhardness: 5\n")
        
        loader = FileLoader()
        data = loader.load(tmp_file)
        assert data['id'] == 'stone'
        assert data['hardness'] == 5

    def test_invalid_file_extension(self, tmp_path):
        tmp_file = tmp_path / "material.txt"
        tmp_file.write_text("id: stone\nhardness: 5\n")
        
        loader = FileLoader()
        with pytest.raises(ValueError) as excinfo:
            loader.load(tmp_file)
        assert "Nenhum carregador disponível para a extensão de arquivo" in str(excinfo.value)

    def test_json_file_not_supported(self, tmp_path):
        tmp_file = tmp_path / "material.json"
        tmp_file.write_text('{"id": "stone", "hardness": 5}')
        
        loader = FileLoader()
        with pytest.raises(ValueError) as excinfo:
            loader.load(tmp_file)
        assert "Nenhum carregador disponível para a extensão de arquivo" in str(excinfo.value)

    def test_empty_file(self, tmp_path):
        tmp_file = tmp_path / "empty.yaml"
        tmp_file.write_text("")
        
        loader = FileLoader()
        data = loader.load(tmp_file)
        assert data == {}

    def test_file_not_found(self, tmp_path):
        tmp_file = tmp_path / "nonexistent.yaml"
        
        loader = FileLoader()
        with pytest.raises(FileNotFoundError):
            loader.load(tmp_file)

    def test_file_with_malformed_yaml(self, tmp_path):
        tmp_file = tmp_path / "malformed.yaml"
        tmp_file.write_text("id: stone\n  invalid indentation: value\n:bad")
        
        loader = FileLoader()
        with pytest.raises(Exception):  # yaml.YAMLError ou similares
            loader.load(tmp_file)

    def test_file_with_list_instead_of_dict(self, tmp_path):
        tmp_file = tmp_path / "list.yaml"
        tmp_file.write_text("- item1\n- item2\n- item3\n")
        
        loader = FileLoader()
        with pytest.raises(ValueError) as excinfo:
            loader.load(tmp_file)
        assert "não possui um YAML no formato de mapeamento" in str(excinfo.value)

    def test_yml_extension(self, tmp_path):
        tmp_file = tmp_path / "material.yml"
        tmp_file.write_text("id: diamond\nhardness: 10\n")
        
        loader = FileLoader()
        data = loader.load(tmp_file)
        assert data['id'] == 'diamond'
        assert data['hardness'] == 10

    def test_pathlike_object(self, tmp_path):
        tmp_file = tmp_path / "material.yaml"
        tmp_file.write_text("id: coal\ncolor: black\n")
        
        loader = FileLoader()
        # Usar pathlib.Path em vez de string
        data = loader.load(pathlib.Path(tmp_file))
        assert data['id'] == 'coal'
        assert data['color'] == 'black'


class TestDirectoryLoader:
    def test_valid_yaml_directory(self, tmp_path):
        dir_path = tmp_path / "configs"
        dir_path.mkdir()

        file1 = dir_path / "material1.yaml"
        file1.write_text("id: stone\nhardness: 5\n")

        file2 = dir_path / "material2.yaml"
        file2.write_text("id: dirt\nhardness: 2\n")

        loader = DirectoryLoader()
        data = loader.load(dir_path)
        
        assert 'material1' in data
        assert 'material2' in data
        assert data['material1']['id'] == 'stone'
        assert data['material2']['id'] == 'dirt'

    def test_invalid_directory_extension(self, tmp_path):
        # Este teste verifica se passa um arquivo em vez de diretório
        tmp_file = tmp_path / "material.yaml"
        tmp_file.write_text("id: stone\n")
        
        loader = DirectoryLoader()
        with pytest.raises(ValueError) as excinfo:
            loader.load(tmp_file)
        assert "não é um diretório válido" in str(excinfo.value)

    def test_empty_directory(self, tmp_path):
        dir_path = tmp_path / "empty_configs"
        dir_path.mkdir()

        loader = DirectoryLoader()
        data = loader.load(dir_path)
        assert data == {}

    def test_directory_with_non_yaml_file(self, tmp_path):
        dir_path = tmp_path / "mixed_configs"
        dir_path.mkdir()

        file1 = dir_path / "material1.yaml"
        file1.write_text("id: stone\nhardness: 5\n")

        file2 = dir_path / "notes.txt"
        file2.write_text("This is a text file and should be ignored.")

        loader = DirectoryLoader()
        data = loader.load(dir_path)
        
        # Apenas o arquivo YAML deve ser carregado
        assert 'material1' in data
        assert 'notes' not in data
        assert len(data) == 1

    def test_directory_with_yml_files(self, tmp_path):
        dir_path = tmp_path / "yml_configs"
        dir_path.mkdir()

        file1 = dir_path / "material1.yml"
        file1.write_text("id: wood\nhardness: 2\n")

        file2 = dir_path / "material2.yaml"
        file2.write_text("id: iron\nhardness: 8\n")

        loader = DirectoryLoader()
        data = loader.load(dir_path)
        
        assert 'material1' in data
        assert 'material2' in data
        assert data['material1']['id'] == 'wood'
        assert data['material2']['id'] == 'iron'

    def test_nonexistent_directory(self, tmp_path):
        dir_path = tmp_path / "nonexistent_dir"
        
        loader = DirectoryLoader()
        with pytest.raises(ValueError) as excinfo:
            loader.load(dir_path)
        assert "não é um diretório válido" in str(excinfo.value)

    def test_pathlike_directory_object(self, tmp_path):
        dir_path = pathlib.Path(tmp_path / "pathlike_configs")
        dir_path.mkdir()

        file1 = dir_path / "material1.yaml"
        file1.write_text("id: gold\nhardness: 3\n")

        loader = DirectoryLoader()
        data = loader.load(dir_path)
        
        assert 'material1' in data
        assert data['material1']['id'] == 'gold'

    
    def test_empty_file(self, tmp_path):
        tmp_file = tmp_path / "empty.yaml"
        tmp_file.write_text("")
        
        loader = FileLoader()
        data = loader.load(tmp_file)
        assert data is None or data == {}

class TestDirectoryLoader:
    def test_valid_yaml_directory(self, tmp_path):
        dir_path = tmp_path / "configs"
        dir_path.mkdir()
        
        file1 = dir_path / "material1.yaml"
        file1.write_text("id: stone\nhardness: 5\n")
        
        file2 = dir_path / "material2.yaml"
        file2.write_text("id: dirt\nhardness: 2\n")
        
        loader = DirectoryLoader()
        data = loader.load(dir_path)
        
        assert 'material1' in data
        assert data['material1']['id'] == 'stone'
        assert 'material2' in data
        assert data['material2']['id'] == 'dirt'

    def test_invalid_directory_extension(self, tmp_path):
        # Este teste verifica se passa um arquivo em vez de diretório
        tmp_file = tmp_path / "material.yaml"
        tmp_file.write_text("id: stone\n")
        
        loader = DirectoryLoader()
        with pytest.raises(ValueError) as excinfo:
            loader.load(tmp_file)
        assert "não é um diretório válido" in str(excinfo.value)

    def test_empty_directory(self, tmp_path):
        dir_path = tmp_path / "empty_configs"
        dir_path.mkdir()
        
        loader = DirectoryLoader()
        data = loader.load(dir_path)
        
        assert data == {}

    def test_directory_with_non_yaml_file(self, tmp_path):
        dir_path = tmp_path / "mixed_configs"
        dir_path.mkdir()
        
        file1 = dir_path / "material1.yaml"
        file1.write_text("id: stone\nhardness: 5\n")
        
        file2 = dir_path / "notes.txt"
        file2.write_text("This is a text file and should be ignored.")
        
        loader = DirectoryLoader()
        data = loader.load(dir_path)
        
        assert 'material1' in data
        assert data['material1']['id'] == 'stone'
        assert 'notes' not in data