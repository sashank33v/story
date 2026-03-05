# Telugu Story Text To Speech (Sarvam AI)

Generate Telugu story audio (`te-IN`) from text using Sarvam AI.

## 1) Install dependencies

```bash
pip install -r requirements.txt
```

## 2) Set API key

```bash
export SARVAM_API_KEY="your_sarvam_api_key"
```

You can also use `SARVAM_API_SUBSCRIPTION_KEY`.

## 3) Run with a story file

```bash
python sarvam_tts_telugu.py --input story.txt --output audio/story_telugu.wav
```

## 4) Run with inline text

```bash
python sarvam_tts_telugu.py --text "ఒక చిన్న కథ..." --output audio/story_telugu.wav
```

## Optional arguments

- `--speaker` (default: `shubh`)
- `--model` (default: `bulbul:v3`)
- `--language` (default: `te-IN`)

## Backward compatibility

You can still run:

```bash
python generate_audio.py --input story.txt --output audio/story_telugu.wav
```
