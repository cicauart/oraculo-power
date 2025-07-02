"""Generación de letras y prompts con modelos de OpenRouter."""

from pathlib import Path
from typing import List

# Ejemplo de modelos gratuitos compatibles con OpenRouter
FREE_MODELS = [
    "openrouter/cinematika-7b",  # pensamiento creativo
    "openrouter/freehuggingmistral-7b",  # razonamiento general
    "openrouter/openchat-3.5-1210"  # diálogo adicional
]


def generate_lyrics(reference: Path) -> str:
    """Genera letras basadas en el audio de referencia."""
    print("[LyricAI] Generando letras usando modelos de OpenRouter...")
    # TODO: conectar con la API de OpenRouter y combinar los tres modelos.
    lyrics = "Letras generadas de ejemplo"
    return lyrics
