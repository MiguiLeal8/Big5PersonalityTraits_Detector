questions_en = {
    "BFI1": "Talks a lot.",
    "BFI2": "Notices the weaknesses of others.",
    "BFI3": "Does things carefully and thoroughly.",
    "BFI4": "Is sad, depressed.",
    "BFI5": "Is original, comes up with new ideas.",
    "BFI6": "Keeps thoughts to themselves.",
    "BFI7": "Is helpful and unselfish with others.",
    "BFI8": "Can be a bit careless.",
    "BFI9": "Is relaxed, handles stress well.",
    "BFI10": "Is curious about many different things.",
    "BFI11": "Has a lot of energy.",
    "BFI12": "Starts arguments with others.",
    "BFI13": "Is a good worker, hard-working.",
    "BFI14": "Can be tense; not always easy-going.",
    "BFI15": "Is intelligent; thinks a lot.",
    "BFI16": "Makes things exciting.",
    "BFI17": "Forgives others easily.",
    "BFI18": "Is not very organized.",
    "BFI19": "Worries a lot.",
    "BFI20": "Has a good active imagination.",
    "BFI21": "Tends to be quiet.",
    "BFI22": "Generally trusts people.",
    "BFI23": "Tends to be lazy.",
    "BFI24": "Does not get upset easily; is stable.",
    "BFI25": "Is creative and inventive.",
    "BFI26": "Has a strong personality.",
    "BFI27": "Can be cold and distant with others.",
    "BFI28": "Keeps working until things are done.",
    "BFI29": "Can be moody.",
    "BFI30": "Likes artistic and creative experiences.",
    "BFI31": "Is a bit shy.",
    "BFI32": "Kind and considerate to almost everyone.",
    "BFI33": "Does things quickly and carefully.",
    "BFI34": "Stays calm in difficult situations.",
    "BFI35": "Likes work that is the same every time.",
    "BFI36": "Is outgoing; likes being with people.",
    "BFI37": "Is sometimes rude to others.",
    "BFI38": "Makes plans and follows through with them.",
    "BFI39": "Gets nervous easily.",
    "BFI40": "Likes to think and play with ideas.",
    "BFI41": "Does not like artistic things (plays, music).",
    "BFI42": "Likes to cooperate; gets along well with others.",
    "BFI43": "Has trouble paying attention.",
    "BFI44": "Knows a lot about art, music, and books."
}

questions_es = {
    "BFI1": "Habla mucho.",
    "BFI2": "Nota los puntos débiles de otras personas.",
    "BFI3": "Hace las cosas con cuidado y completamente.",
    "BFI4": "Está triste, deprimido.",
    "BFI5": "Es original, se le ocurren nuevas ideas.",
    "BFI6": "Guarda sus pensamientos para sí mismo.",
    "BFI7": "Es servicial y no egoísta con los demás.",
    "BFI8": "Puede ser un poco descuidado.",
    "BFI9": "Está relajado, maneja bien el estrés.",
    "BFI10": "Es curioso sobre muchas cosas diferentes.",
    "BFI11": "Tiene mucha energía.",
    "BFI12": "Inicia discusiones con otros.",
    "BFI13": "Es un buen trabajador, trabajador duro.",
    "BFI14": "Puede estar tenso; no siempre es fácil de llevar.",
    "BFI15": "Es inteligente; piensa mucho.",
    "BFI16": "Hace las cosas emocionantes.",
    "BFI17": "Perdona a los demás fácilmente.",
    "BFI18": "No es muy organizado.",
    "BFI19": "Se preocupa mucho.",
    "BFI20": "Tiene una buena imaginación activa.",
    "BFI21": "Tiende a ser callado.",
    "BFI22": "Generalmente confía en las personas.",
    "BFI23": "Tiende a ser perezoso.",
    "BFI24": "No se molesta fácilmente; es estable.",
    "BFI25": "Es creativo e inventivo.",
    "BFI26": "Tiene una buena personalidad fuerte.",
    "BFI27": "Puede ser frío y distante con los demás.",
    "BFI28": "Sigue trabajando hasta que las cosas están hechas.",
    "BFI29": "Puede estar de mal humor.",
    "BFI30": "Le gustan las experiencias artísticas y creativas.",
    "BFI31": "Es un poco tímido.",
    "BFI32": "Amable y considerado con casi todos.",
    "BFI33": "Hace las cosas rápida y cuidadosamente.",
    "BFI34": "Permanece tranquilo en situaciones difíciles.",
    "BFI35": "Le gusta el trabajo que es el mismo cada vez.",
    "BFI36": "Es extrovertido; le gusta estar con la gente.",
    "BFI37": "A veces es grosero con los demás.",
    "BFI38": "Hace planes y los sigue.",
    "BFI39": "Se pone nervioso fácilmente.",
    "BFI40": "Le gusta pensar y jugar con ideas.",
    "BFI41": "No le gustan las cosas artísticas (obras de teatro, música).",
    "BFI42": "Le gusta cooperar; se lleva bien con los demás.",
    "BFI43": "Tiene problemas para prestar atención.",
    "BFI44": "Sabe mucho sobre arte, música y libros."
}
    
# Define which questions are Forward and Reverse for each trait
bfi_map = {
    "Extraversion": {
        "Forward": ["BFI1", "BFI11", "BFI26", "BFI36"],
        "Reverse": ["BFI6", "BFI21", "BFI31"]
    },
    "Agreeableness": {
        "Forward": ["BFI7", "BFI17", "BFI22", "BFI32", "BFI42"],
        "Reverse": ["BFI2", "BFI12", "BFI27", "BFI37"]
    },
    "Conscientiousness": {
        "Forward": ["BFI3", "BFI13", "BFI28", "BFI33", "BFI38"],
        "Reverse": ["BFI8", "BFI18", "BFI23", "BFI43"]
    },
    "Neuroticism": {
        "Forward": ["BFI4", "BFI14", "BFI19", "BFI29", "BFI39"],
        "Reverse": ["BFI9", "BFI24", "BFI34"]
    },
    "Openness": {
        "Forward": ["BFI5", "BFI10", "BFI15", "BFI20", "BFI25", "BFI30", "BFI40", "BFI44"],
        "Reverse": ["BFI35", "BFI41"]
    }
}

answers = {}

def get_answers(language):
    print("BFI-44 TEST:")
    if language == "es":
        print("Para cada question, ingresa un número del 1 al 5:")
        print("1 = Muy en desacuerdo, 2 = En desacuerdo, 3 = Neutral, 4 = De acuerdo, 5 = Muy de acuerdo\n")

        for code, question in questions_es.items():
            answer = int(input(question + " (1-5): "))
            if answer in range(1, 6):
                answers[code] = answer
            else:
                print("Por favor, ingresa un número entre 1 y 5.")
                while answer not in range(1, 6):
                    answer = int(input(question + " (1-5): "))
                answers[code] = answer
    else:
        print("For each question, enter a number from 1 to 5:")
        print("1 = Strongly Disagree, 2 = Disagree, 3 = Neutral, 4 = Agree, 5 = Strongly Agree\n")

        for code, question in questions_en.items():
            answer = int(input(question + " (1-5): "))
            if answer in range(1, 6):
                answers[code] = answer
            else:
                print("Please enter a number between 1 and 5.")
                while answer not in range(1, 6):
                    answer = int(input(question + " (1-5): "))
                answers[code] = answer

    return answers

# Función para calcular los puntajes BFI
def bfi_to_big5(answers):
    big5_score = {}

    for trait, items in bfi_map.items():
        # Sum the Forward (direct) scores
        forward_sum = sum(answers[q] for q in items["Forward"])

        # Sum the Reverse (inverting them with the formula (6 - answer))
        reverse_sum = sum(6 - answers[q] for q in items["Reverse"])

        # Calculate the total score for each trait
        big5_score[trait] = forward_sum + reverse_sum

    return big5_score

# Calcular los puntajes de Big Five
def bfi44_test(language):
    answers = get_answers(language)
    big5_score = bfi_to_big5(answers)
    
    return big5_score
