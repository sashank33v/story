# Telugu Story Text To Speech (Sarvam AI)

Generate Telugu story audio (`te-IN`) from text using Sarvam AI.

## Story Text

```text
Oka chinna gramam lo Ramu ane oka abbayi undevadu. Ataniki prakruthi (nature) ante chala istam.
Prathi roju school ki velladaniki mundu, tana gramam daggara unna cheruvu daggara ki velladu.
Akkada paksulu, chetlu chusthu chala santhoshamga untadu.

Oka roju, cheruvu daggara oka gaya padina chinna pakshi ni chusadu.
Ramu danini jagrathaga intiki teesukoni velladu.
Daniki neellu ichadu, mandhu vesadu, mariyu konni rojulu chala jagrathaga chusukunnadu.

Konni rojula tharvatha, aa pakshi malli eguragaligindi.
Ramu chala santhosham tho danini akasham lo vidichadu.
Pakshi santhoshamga eguripoyindi.

Aa roju Ramu oka mukhyamaina lesson nerchukunnadu:
chinna sahayam kuda oka jeevitham lo pedda maarpu teesukosthundi.
Appati nundi Ramu eppudu avasaram unna variki sahayam cheyyadaniki try chesadu.
```

## Listen To The Story

<audio controls>
  <source src="audio/story1.mp3" type="audio/mpeg">
  <source src="audio/story1.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

- [Play/Download MP3](audio/story1.mp3)
- [Play/Download WAV](audio/story1.wav)

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
