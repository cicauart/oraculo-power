"""Aplicación de RVC para clonar la voz."""

from pathlib import Path


def apply_voice_model(audio: Path) -> Path:
    """Aplica el modelo de voz entrenado con RVC al audio generado."""
    print("[RVC] Procesando voz con el modelo personalizado...")
    # TODO: Utilizar RVC v2 para convertir la voz.
    processed = Path("final_mix.wav")
    print("[RVC] Voz procesada")
    return processed
