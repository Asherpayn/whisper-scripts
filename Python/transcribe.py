import whisper

model_prompt_info = """Available Whisper models:
  tiny    ( 39M) | ~1GB  VRAM | ~10x speed | English: tiny.en
  base    ( 74M) | ~1GB  VRAM | ~ 7x speed | English: base.en
  small   (244M) | ~2GB  VRAM | ~ 4x speed | English: small.en
  medium  (769M) | ~5GB  VRAM | ~ 2x speed | English: medium.en
  large  (1550M) | ~10GB VRAM | ~ 1x speed | Multilingual only
  turbo   (809M) | ~6GB  VRAM | ~ 8x speed | Multilingual only
"""
model = whisper.load_model(input(f"Choose a model, \n {model_prompt_info} >>> ").lower())

if input("Do you want to view this models info? (y/n) \n >>> ").strip().lower() == "y":
    print(model)

