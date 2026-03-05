#!/usr/bin/env python3
"""Generate Telugu story audio using Sarvam AI Text-to-Speech."""

import argparse
import base64
import os
from pathlib import Path

from dotenv import load_dotenv
from sarvamai import SarvamAI


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert Telugu story text to speech using Sarvam AI."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input", type=Path, help="Path to a UTF-8 text file")
    group.add_argument("--text", help="Story text provided directly")

    parser.add_argument(
        "--output",
        type=Path,
        default=Path("audio/story_telugu.wav"),
        help="Output audio file path (default: audio/story_telugu.wav)",
    )
    parser.add_argument(
        "--language",
        default="te-IN",
        help="Target language code (default: te-IN)",
    )
    parser.add_argument(
        "--speaker",
        default="shubh",
        help="Sarvam speaker voice (default: shubh)",
    )
    parser.add_argument(
        "--model",
        default="bulbul:v3",
        help="Sarvam TTS model (default: bulbul:v3)",
    )
    return parser.parse_args()


def read_story_text(args: argparse.Namespace) -> str:
    if args.text:
        return args.text.strip()

    content = args.input.read_text(encoding="utf-8").strip()
    if not content:
        raise ValueError(f"Input file is empty: {args.input}")
    return content


def extract_audio_base64(response) -> str:
    # SDK response can be an object or dict depending on version.
    audios = None
    if hasattr(response, "audios"):
        audios = response.audios
    elif isinstance(response, dict):
        audios = response.get("audios")
    elif hasattr(response, "model_dump"):
        audios = response.model_dump().get("audios")

    if not audios:
        raise ValueError("No audio returned by Sarvam TTS API")
    return audios[0]


def main() -> None:
    load_dotenv()
    args = parse_args()

    api_key = os.getenv("SARVAM_API_KEY") or os.getenv("SARVAM_API_SUBSCRIPTION_KEY")
    if not api_key:
        raise EnvironmentError(
            "Missing API key. Set SARVAM_API_KEY (or SARVAM_API_SUBSCRIPTION_KEY)."
        )

    story_text = read_story_text(args)

    client = SarvamAI(api_subscription_key=api_key)
    response = client.text_to_speech.convert(
        text=story_text,
        target_language_code=args.language,
        speaker=args.speaker,
        model=args.model,
    )

    audio_base64 = extract_audio_base64(response)
    audio_bytes = base64.b64decode(audio_base64)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(audio_bytes)
    print(f"Saved Telugu story audio to: {args.output}")


if __name__ == "__main__":
    main()
