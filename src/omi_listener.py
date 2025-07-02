"""Módulo para captura de audio mediante OMI."""
from pathlib import Path


def record_reference(duration: int = 30) -> Path:
    """Graba la voz del usuario utilizando OMI durante `duration` segundos."""
    # Aquí se debería inicializar la API de OMI y grabar.
    out_path = Path("reference.wav")
    print(f"[OMI] Grabando referencia durante {duration} segundos...")
    # TODO: integrar omi.audio para capturar el audio real.
    print("[OMI] Grabación completa")
    return out_path
