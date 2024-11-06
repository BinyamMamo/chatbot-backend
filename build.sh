#!/bin/bash
pip install Flask torch torchvision nltk
python -c "import nltk; nltk.download('punkt')"
python train.py
python chat.py