"""Funciones relacionadas con SongBloom."""

from pathlib import Path


def create_song(lyrics: str, reference: Path) -> Path:
    """Genera una canción utilizando SongBloom a partir de unas letras.

    Args:
        lyrics: Letras generadas por IA.
        reference: Archivo de referencia para extraer emoción y tono.

    Returns:
        Ruta al archivo de audio generado.
    """
    print("[SongBloom] Generando pista instrumental...")
    # TODO: Llamar a SongBloom API/script con las letras.
    generated_path = Path("song.wav")
    print("[SongBloom] Canción generada")
    return generated_path
