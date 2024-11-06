#!/bin/bash
pip install Flask torch torchvision nltk
python -c "import nltk; nltk.download('punkt')"
python -c "import nltk; nltk.download('punkt_tab')"  # for windows
python chatbot/train.py
