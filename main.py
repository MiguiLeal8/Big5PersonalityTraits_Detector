from Emotions.translator import *
from Emotions.emotionsModel import *
from Big5.toBig5 import *
from Big5.personalityUpdate import *
from SpaCy.spacy import *

big5_previous_points = {
    "Neuroticism": 20,
    "Extraversion": 25,
    "Openness": 40,
    "Agreeableness": 30,
    "Conscientiousness": 35
}

# If 0.3, it gives 30% weight to the new info and 70% to the previous one
alpha = 0.3

# Ask the user for the language
language = input("Will you use Spanish or English? / ¿Vas a usar Español o Inglés? (es/en): ").strip().lower()

# Ask the user to write some sentences
if language=="es":
    text = input("Por favor escribe algunas frases: ").strip()
else:
    text = input("Please write some sentences: ").strip()

print("Updated Big5 personality traits:\n", updatePersonality(text, big5_previous_points, alpha, language))
print("Max text emotion:", get_max_emotion(text, language))
print("Max text big5 trait:", get_max_big5(text, language))