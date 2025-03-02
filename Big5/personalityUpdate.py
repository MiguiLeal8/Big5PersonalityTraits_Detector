from Emotions.translator import *
from Emotions.emotionsModel import *
from Big5.toBig5 import *

#Function to get the most predominant emotion in a text
def max_emotion(text, language):
    if language=="es":
        text = traducir_es_en(text)
    emotions_results = get_emotions(text)
    emotion_max = max(emotions_results, key=emotions_results.get)
    return emotion_max
#Function to get the most predominant Big5 factor in a text
def max_big5(text, language):
    if language=="es":
        text = traducir_es_en(text)
    emotions_results = get_emotions(text)
    big5_results = calculate_big5(emotions_results)
    factor_max = max(big5_results, key=big5_results.get)
    return factor_max

#Function to update the Big5 personality traits based on a text
def updatePersonality(text, big5_previous_points, alpha, language):
    if language=="es":
        text = traducir_es_en(text)
    emotions_results = get_emotions(text)
    big5_results = calculate_big5(emotions_results)

    big5_scalated = scale_scores(big5_results)
    sorted_emotions = dict(sorted(emotions_results.items(), key=lambda item: item[1], reverse=True))
    '''
    if language=="es":
        print("Emociones del texto (ordenadas):\n", sorted_emotions)
        print("Rasgos de personalidad del texto:\n", big5_scalated)
    else:
        print("Emotions from text (sorted):\n", sorted_emotions)
        print("Personality traits from text:\n", big5_scalated)
    '''
    big5_updated = update_big5(big5_previous_points, big5_scalated, alpha)

    return big5_updated