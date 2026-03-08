"""
Testes unitários para o materials registry.

"""

import pytest

import src.engine.config.registry.materials_registry as materials_registry

class TestMaterialsRegistry:
    @pytest.fixture
    def registry(self):
        return materials_registry.MaterialsRegistry()
    
    def test_register_and_get_material(self, registry):
        material_id = "stone"
        material_data = {
            "name": "Stone",
            "density": 2.5,
            "strength": 10,
            "inflamability": False
        }
        
        registry.register_material(material_id, material_data)
        retrieved_material = registry.get_material(material_id)
        
        assert retrieved_material == material_data

    def test_get_nonexistent_material(self, registry):
        retrieved_material = registry.get_material("nonexistent")
        
        assert retrieved_material is None


    def test_load_materials_from_directory(self, tmp_path, registry):
        # Cria arquivos de materiais temporários
        material1 = tmp_path / "material1.yaml"
        material1.write_text("""
id: stone
name: Stone
density: 2.5
strength: 10
inflamability: false
""")
        material2 = tmp_path / "material2.yaml"
        material2.write_text("""
id: dirt
name: Dirt
density: 1.5
strength: 5
inflamability: false
""")
        # Usa o loader de diretório para carregar os materiais
        directory_loader = materials_registry.DirectoryLoader()
        materials_data = directory_loader.load(tmp_path)
        
        for material_id, material_data in materials_data.items():
            registry.register_material(material_id, material_data)
        
        # Verifica se os materiais foram registrados corretamente
        retrieved_material1 = registry.get_material("stone")
        retrieved_material2 = registry.get_material("dirt")
        
        assert retrieved_material1['name'] == 'Stone'
        assert retrieved_material2['name'] == 'Dirt'