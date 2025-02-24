from Emotions.translator import *
from Emotions.emotionsModel import *
from Big5.initialTest import *
from Big5.toBig5 import *
from Big5.personalityUpdate import *
from Objectives.objectives import *
import pandas as pd

# Initial Big5 personality traits for testing
'''
big5_personality = {
    "Extraversion": 25,
    "Agreeableness": 30,
    "Conscientiousness": 35,
    "Neuroticism": 20,
    "Openness": 40
}
'''

# If 0.3, it gives 30% weight to the new info and 70% to the previous one
alpha = 0.3

# Ask the user for the language
language = input("Will you use Spanish or English? / ¿Vas a usar Español o Inglés? (es/en): ").strip().lower()

stop = False

if language == "es":

    big5_personality=bfi44_test(language)

    big5_personality_df = pd.DataFrame(list(big5_personality.items()), columns=["Trait", "Score"])
    print("Rasgos de personalidad Big5 iniciales:\n", big5_personality_df)

    while not stop:
            
        # Ask the user to write some sentences
        text = input("Por favor escribe algunas frases: ").strip()
        big5_personality=updatePersonality(text, big5_personality, alpha, language)
        print("Emoción máxima del texto:", max_emotion(text, language))
        print("Rasgo Big5 máximo del texto:", max_big5(text, language))
        big5_personality_df = pd.DataFrame(list(big5_personality.items()), columns=["Trait", "Score"])
        print("Rasgos de personalidad Big5 actualizados:\n", big5_personality_df)
            
        if input("¿Quieres ver tus objetivos? (si/no): ").strip().lower() == "si":
            objetives = get_objectives(big5_personality, language)
            for obj in objetives:
                print(obj)
            if objetives == []:
                print("No se encontraron objetivos.")
          
        if input("¿Quieres parar? (si/no): ").strip().lower() == "si":
            stop = True

else:
    
    big5_personality=bfi44_test(language)

    big5_personality_df = pd.DataFrame(list(big5_personality.items()), columns=["Trait", "Score"])
    print("Initial Big5 personality traits:\n", big5_personality_df)

    while not stop:
        text = input("Please write some sentences: ").strip()
        big5_personality=updatePersonality(text, big5_personality, alpha, language)
        print("Max text emotion:", max_emotion(text, language))
        print("Max text big5 trait:", max_big5(text, language))
        big5_personality_df = pd.DataFrame(list(big5_personality.items()), columns=["Trait", "Score"])
        print("Updated Big5 personality traits:\n", big5_personality_df)

        # Ask if the user wants to see their goals
        if input("Do you want to see your objectives? (yes/no): ").strip().lower() == "yes":
            objetives = get_objectives(big5_personality, language)
            for obj in objetives:
                print(obj)
            if objetives == []:
                print("No objectives found.")

        # Ask if the user wants to stop
        if input("Do you want to stop? (yes/no): ").strip().lower() == "yes":
            stop = True