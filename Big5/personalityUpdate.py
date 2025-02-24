from Emotions.translator import *
from Emotions.emotionsModel import *
from Big5.toBig5 import *
from SpaCy.spacy import *
import json

#Function to get the most predominant emotion in a text
def get_max_emotion(text, language):
    if language=="es":
        text = traducir_es_en(text)
    #text = text_processor(text)
    emotions_results = get_emotions(text)
    emotion_max = max(emotions_results, key=emotions_results.get)
    return emotion_max
#Function to get the most predominant Big5 factor in a text
def get_max_big5(text, language):
    if language=="es":
        text = traducir_es_en(text)
    #text = text_processor(text)
    emotions_results = get_emotions(text)
    big5_results = calculate_big5(emotions_results)
    factor_max = max(big5_results, key=big5_results.get)
    return factor_max

#Function to update the Big5 personality traits based on a text
def updatePersonality(text, big5_previous_points, alpha, language):
    if language=="es":
        text = traducir_es_en(text)
    #text = text_processor(text)
    emotions_results = get_emotions(text)
    big5_results = calculate_big5(emotions_results)

    big5_scalated = scale_scores(big5_results, bfi_ranges)

    big5_puntajes_actualizados = update_big5(big5_previous_points, big5_scalated, alpha)
    print("\nPrevious personality traits:\n", big5_previous_points)
    print("Emotions from text:\n", emotions_results)
    print("Personality traits from text:\n", big5_scalated)

    json_big5 = json.dumps(big5_puntajes_actualizados, indent=4)

    return json_big5

big5_previous_points = {
    "Neuroticism": 20,
    "Extraversion": 25,
    "Openness": 40,
    "Agreeableness": 30,
    "Conscientiousness": 35
}