"""Integración con Kits.AI para convertir la voz generada."""

from pathlib import Path
import time
import requests
from typing import Optional

from .config import KITS_API_KEY, KITS_VOICE_ID


def upload_audio(path: Path) -> Optional[str]:
    """Sube el audio a file.io y devuelve la URL pública."""
    print("[Upload] Subiendo audio temporal...")
    try:
        with open(path, "rb") as f:
            resp = requests.post("https://file.io", files={"file": f})
        resp.raise_for_status()
        data = resp.json()
        url = data.get("link")
        if not url:
            print("[Upload] Respuesta sin URL")
            return None
        print(f"[Upload] Archivo subido: {url}")
        return url
    except Exception as err:
        print(f"[Upload] Error al subir audio: {err}")
        return None


def convertir_voz_con_kits(input_audio_url: str, voice_model_id: str, api_key: str) -> Optional[str]:
    """Convierte la voz usando el API de Kits.AI y devuelve la URL resultante."""
    print("[Kits.AI] Enviando petición de conversión...")
    payload = {
        "voice_model_id": voice_model_id,
        "input_audio_url": input_audio_url,
        "output_format": "mp3",
    }
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        resp = requests.post(
            "https://api.kits.ai/voice-conversion/convert",
            json=payload,
            headers=headers,
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        url = data.get("output_url") or data.get("url")
        if not url:
            print("[Kits.AI] Respuesta sin URL de salida")
            return None
        print("[Kits.AI] Conversión completada")
        return url
    except Exception as err:
        print(f"[Kits.AI] Error: {err}")
        return None


def apply_voice_model(audio: Path) -> Path:
    """Sube el audio y aplica la voz clonada con Kits.AI."""
    temp_url = upload_audio(audio)
    if not temp_url:
        raise RuntimeError("No se pudo subir el audio para la conversión")

    result_url = convertir_voz_con_kits(temp_url, KITS_VOICE_ID, KITS_API_KEY)
    if not result_url:
        raise RuntimeError("Fallo la conversión en Kits.AI")

    print("[Kits.AI] Descargando resultado...")
    resp = requests.get(result_url)
    resp.raise_for_status()
    filename = f"final_{int(time.time())}.mp3"
    out_path = Path(filename)
    with open(out_path, "wb") as f:
        f.write(resp.content)
    print(f"[Kits.AI] Audio final guardado en {out_path}")
    return out_path
