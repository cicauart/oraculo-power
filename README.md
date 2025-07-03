# Oraculo Power

Este repositorio contiene un esqueleto de proyecto para ensamblar un sistema musical personalizado que combine varias herramientas open-source.

## Componentes principales
- **SongBloom**: motor de generación musical.
- **Kits.AI**: clonador de voz basado en API para aplicar la voz del artista.
- **Bark** (opcional): síntesis de voz rápida para prototipos.
- **Matchering 2.0**: herramienta de masterización automática.
- **LyricJam** (opcional): generación de letras.
- **Telegram**: canal de salida para recibir el audio final.

Incluye una base de datos simple para almacenar referencias de canciones, letras y emociones. También se muestra cómo integrar modelos gratuitos de [OpenRouter](https://openrouter.ai/models) para la generación de prompts.

Consulta `requirements.txt` para las dependencias necesarias.

## Estructura de carpetas
```
.
├── README.md
├── requirements.txt
├── data/
│   └── songs/         # canciones de referencia
└── src/
    ├── __init__.py
    ├── main.py        # punto de entrada
    ├── songbloom.py   # funciones de SongBloom
    ├── kits_voice.py  # integración con Kits.AI
    ├── lyric_ai.py    # generación de letras y prompts
    ├── database.py    # base de datos ligera
    ├── telegram_bot.py# envío a Telegram
```

### Variables de entorno
Configura un archivo `.env` (o variables del sistema) con:

```
KITS_API_KEY=tu_api_key
KITS_VOICE_ID=id_de_tu_voz
Este proyecto es solo un punto de partida. Cada módulo contiene ejemplos de cómo llamar a las herramientas externas. La integración completa requerirá configurar credenciales de Telegram, OpenRouter y la instalación de cada librería.
