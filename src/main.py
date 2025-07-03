"""Punto de entrada principal del proyecto."""
from .omi_listener import record_reference
from .lyric_ai import generate_lyrics
from .songbloom import create_song
from .kits_voice import apply_voice_model
from .telegram_bot import send_audio
from .database import save_reference


def compose_song(trigger_seconds: int = 30) -> None:
    """Captura una referencia cantada, genera la canción y la envía a Telegram."""
    reference_path = record_reference(duration=trigger_seconds)
    save_reference(reference_path)
    lyrics = generate_lyrics(reference_path)
    song = create_song(lyrics, reference_path)
    final_mix = apply_voice_model(song)
    send_audio(final_mix)


if __name__ == "__main__":
    compose_song()
