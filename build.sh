#!/bin/bash
# python -c "import nltk; nltk.download('punkt')"
# pip install torch torchvision nltk python-dotenv
# pip install Flask python-dotenv
# pip install -q -U google-generativeai

pip install Flask torch nltk
python -c "import nltk; nltk.download('punkt_tab')"  # for windows
python chatbot/train.py
