"""Punto de entrada principal del proyecto."""
from .lyric_ai import generate_lyrics
from .songbloom import create_song
from .kits_voice import apply_voice_model
from .telegram_bot import send_audio
from .database import save_reference


def compose_song(reference_path: str = "data/input.wav") -> None:
    """Genera la canción a partir de un audio existente y la envía a Telegram."""
    save_reference(reference_path)
    lyrics = generate_lyrics(reference_path)
    song = create_song(lyrics, reference_path)
    final_mix = apply_voice_model(song)
    send_audio(final_mix)


if __name__ == "__main__":
    compose_song()
