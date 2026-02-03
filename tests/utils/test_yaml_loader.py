"""
Testes para o carregador YAML.
"""
import pytest

import os
from pathlib import Path
from textwrap import dedent
from yaml import YAMLError

from src.utils.yaml_loader import YamlFileLoader, YamlDirectoryLoader

class TestYamlFileLoader:
    @pytest.fixture
    def yaml_file_valid(self, tmp_path):
        """
        Montando o cenário de teste com arquivos YAML temporários.
        """
        tmp_path = Path(tmp_path)
        tmp_file = tmp_path / "test_layer_profile.yaml"

        tmp_file.write_text(dedent("""\
            id: plains_layer_profile
            layers:
              - id: rocky
                material: stone
                y_from: 1
                y_to: 60
              - id: dirt
                material: soil
                y_from: 61
                y_to: 80
            """))
        return tmp_file 
    
    @pytest.fixture
    def yaml_file_invalid(self, tmp_path):
        """
        Montando o cenário de teste com um arquivo YAML inválido.
        """
        tmp_path = Path(tmp_path)
        tmp_file = tmp_path / "invalid_layer_profile.yaml"

        tmp_file.write_text(dedent("""\
            id: invalid_layer_profile
            layers:
              - id: rocky
                material: stone
                y_from: 1
                y_to: 60
              - id: dirt
                material: soil
                y_from: 61
                y_to: 80
              - invalid_entry
                details: oops
              - id: broken
                y_to: [1, 2
            """))

        return tmp_file
    
    def test_load_yaml_file_success(self, yaml_file_valid):
        """
        Testa o carregamento bem-sucedido de um arquivo YAML.
        """
        result = YamlFileLoader.load_yaml_file(yaml_file_valid)
        assert result is not None
        assert result['id'] == 'plains_layer_profile'
        assert len(result['layers']) == 2
        assert result['layers'][1]['material'] == 'soil'


    def test_load_yaml_file_not_found(self, tmp_path):
        """
        Testa o comportamento ao tentar carregar um arquivo YAML que não existe.
        """
        nonexistent_file = tmp_path / "nonexistent.yaml"
        with pytest.raises(FileNotFoundError):
            YamlFileLoader.load_yaml_file(nonexistent_file)

    def test_load_yaml_file_invalid_format(self,yaml_file_invalid):
        """
        Testa o comportamento ao tentar carregar um arquivo YAML com formato inválido.
        """        
        with pytest.raises(YAMLError):
            YamlFileLoader.load_yaml_file(yaml_file_invalid)

    @pytest.mark.skipif(os.name == "nt", reason="chmod not reliable on Windows")
    def test_load_yaml_file_permission_denied(self, tmp_path):
        """
        Testa o comportamento ao tentar carregar um arquivo YAML sem permissão de leitura.
        """
        tmp_path = Path(tmp_path)
        tmp_file = tmp_path / "no_permission.yaml"

        tmp_file.write_text(dedent("""
            id: no_permission_test
            data: some_data
        """))

        # Remove a permissão de leitura
        tmp_file.chmod(0o000)

        with pytest.raises(PermissionError):
            YamlFileLoader.load_yaml_file(tmp_file)

    def test_load_yaml_not_yaml_file(self, tmp_path):
        """
        Testa o comportamento ao tentar carregar um arquivo que não é YAML.
        """
        tmp_path = Path(tmp_path)
        tmp_file = tmp_path / "not_a_yaml.txt"

        tmp_file.write_text("Just some text content.")

        with pytest.raises(ValueError):
            YamlFileLoader.load_yaml_file(tmp_file)   
        
class TestYamlLoaderFolderContext:
    @pytest.fixture
    def yaml_folder(self, tmp_path):
        """
        Montando o cenário de teste com uma pasta YAML temporária.
        """
        tmp_path = Path(tmp_path)
        folder_path = tmp_path / "yaml_folder"
        folder_path.mkdir()

        file1 = folder_path / "file1.yaml"
        file1.write_text(dedent("""\
            name: file1
            value: 123
            """))

        file2 = folder_path / "file2.yaml"
        file2.write_text(dedent("""\
            name: file2
            value: 456
            """))

        return folder_path

    def test_load_yaml_folder_success(self, yaml_folder):
        """
        Testa o carregamento bem-sucedido de uma pasta contendo arquivos YAML.
        """
        results = YamlDirectoryLoader().load_yaml_directory(yaml_folder)

        assert len(results) == 2
        names = {item['name'] for item in results.values()}
        assert 'file1' in names
        assert 'file2' in names

    def test_load_yaml_folder_empty(self, tmp_path):
        """
        Testa o comportamento ao carregar uma pasta vazia.
        """
        empty_folder = tmp_path / "empty_yaml_folder"
        empty_folder.mkdir()

        results = YamlDirectoryLoader().load_yaml_directory(empty_folder)

        assert results == {}
        assert len(results) == 0

    def test_load_yaml_folder_with_invalid_file(self, yaml_folder):
        """
        Testa o comportamento ao carregar uma pasta contendo um arquivo YAML inválido.
        """
        invalid_file = yaml_folder / "invalid.yaml"
        invalid_file.write_text("a: [1, 2")

        with pytest.raises(YAMLError):
            YamlDirectoryLoader().load_yaml_directory(yaml_folder)

    def test_load_yaml_folder_nonexistent_path(self):
        """
        Testa o comportamento ao tentar carregar uma pasta que não existe.
        """
        nonexistent_path = "nonexistent_folder"

        with pytest.raises(FileNotFoundError):
            YamlDirectoryLoader().load_yaml_directory(nonexistent_path)

    def test_load_yaml_folder_mixed_files(self, yaml_folder):
        """
        Testa o carregamento de uma pasta contendo arquivos YAML e não-YAML.
        """
        non_yaml_file = yaml_folder / "not_a_yaml.txt"
        non_yaml_file.write_text("Just some text content.")

        results = YamlDirectoryLoader().load_yaml_directory(yaml_folder)

        assert len(results) == 2
        names = {item['name'] for item in results.values()}
        assert 'file1' in names
        assert 'file2' in names
