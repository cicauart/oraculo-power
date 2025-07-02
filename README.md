# Oraculo Power

Este repositorio contiene un esqueleto de proyecto para ensamblar un sistema musical personalizado que combine varias herramientas open-source.

## Componentes principales
- **SongBloom**: motor de generación musical.
- **RVC v2**: clonador de voz para reemplazar la voz en las canciones.
- **Bark** (opcional): síntesis de voz rápida para prototipos.
- **Matchering 2.0**: herramienta de masterización automática.
- **LyricJam** (opcional): generación de letras.
- **OMI**: entrada de audio para capturar referencia vocal.
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
    ├── rvc.py         # voz clonada con RVC
    ├── lyric_ai.py    # generación de letras y prompts
    ├── database.py    # base de datos ligera
    ├── telegram_bot.py# envío a Telegram
    └── omi_listener.py# captura de audio por OMI
```

Este proyecto es solo un punto de partida. Cada módulo contiene ejemplos de cómo llamar a las herramientas externas. La integración completa requerirá configurar credenciales de Telegram, OpenRouter y la instalación de cada librería.
