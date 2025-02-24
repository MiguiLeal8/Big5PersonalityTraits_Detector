from Emotions.translator import *
from Emotions.emotionsModel import *
from Big5.toBig5 import *
from Big5.personalityUpdate import *
from Objectives.objectives import *

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
stop = False

while not stop:
    # Ask the user to write some sentences
    if language == "es":
        text = input("Por favor escribe algunas frases: ").strip()
        user_big5=updatePersonality(text, big5_previous_points, alpha, language)
        print("Emoción máxima del texto:", max_emotion(text, language))
        print("Rasgo Big5 máximo del texto:", max_big5(text, language))
        print("Rasgos de personalidad Big5 actualizados:\n", user_big5)
        
        if input("¿Quieres ver tus objetivos? (si/no): ").strip().lower() == "si":
            objetives = get_objectives(user_big5, language)
            for obj in objetives:
                print(obj)
        
        if input("¿Quieres parar? (si/no): ").strip().lower() == "si":
            stop = True

    else:
        text = input("Please write some sentences: ").strip()
        user_big5=updatePersonality(text, big5_previous_points, alpha, language)
        print("Max text emotion:", max_emotion(text, language))
        print("Max text big5 trait:", max_big5(text, language))
        print("Updated Big5 personality traits:\n", user_big5)

        # Ask if the user wants to see their goals
        if input("Do you want to see your objectives? (yes/no): ").strip().lower() == "yes":
            objetives = get_objectives(user_big5, language)
            for obj in objetives:
                print(obj)

        # Ask if the user wants to stop
        if input("Do you want to stop? (yes/no): ").strip().lower() == "yes":
            stop = True