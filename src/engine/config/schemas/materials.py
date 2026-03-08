"""
Schemas de materiais para validação de dados.
"""

from typing import Dict, Any
from pydantic import BaseModel, Field
from dataclasses import dataclass

@dataclass(frozen=True)
class MaterialSchema(BaseModel):
    """
    Schema que representa um material com suas propriedades.

    Utilizado para validação de dados de materiais.
    """

    id: str = Field(..., description="ID único do material.")
    name: str = Field(..., description="Nome do material.")
    density: float = Field(..., description="Densidade do material.")
    strength: float = Field(..., description="Resistência do material.")
    inflamability: bool = Field(..., description="Indica se o material é inflamável.")