from Big5.big5_ranges import bfi_ranges

def get_objectives(big5_scores, language):
    objetives = []
    
    if language == "es":
        for trait, score in big5_scores.items():
            min_val, max_val = bfi_ranges[trait]
            mid = (min_val + max_val) / 2
            
            if trait == "Neuroticism":
                if score > mid+10:
                    objetives.append("Soy una persona emocionalmente inestable y quiero reducir mi neuroticismo.")
                elif score < mid-10:
                    objetives.append("Soy una persona emocionalmente estable y quiero mantener mi equilibrio.")
                    
            elif trait == "Extraversion":
                if score > mid+10:
                    objetives.append("Soy una persona extrovertida y quiero mantener mi energía social.")
                elif score < mid-10:
                    objetives.append("Soy una persona introvertida y quiero aumentar mi extraversión.")    
            
            elif trait == "Openness":
                if score > mid+10:
                    objetives.append("Soy una persona abierta a nuevas experiencias y quiero potenciar mi creatividad.")
                elif score < mid-10:
                    objetives.append("Soy una persona con poca apertura a la experiencia y quiero aumentar mi creatividad y curiosidad.")
                 
            elif trait == "Agreeableness":
                if score > mid+10:
                    objetives.append("Soy una persona muy colaborativa y quiero mantener mi alta empatía.")
                elif score < mid-10:
                    objetives.append("Soy una persona poco colaborativa y quiero aumentar mi empatía y amabilidad.")  

            elif trait == "Conscientiousness":
                if score > mid+10:
                    objetives.append("Soy una persona organizada y quiero mantener mi alto nivel de compromiso.")
                if score < mid-10:
                    objetives.append("Soy una persona desorganizada y quiero aumentar mi responsabilidad y organización.")
    
    else:
        for trait, score in big5_scores.items():
            min_val, max_val = bfi_ranges[trait]
            mid = (min_val + max_val) / 2
            
            if trait == "Neuroticism":
                if score > mid+10:
                    objetives.append("I am an emotionally unstable person and I want to reduce my neuroticism.")
                elif score < mid-10:
                    objetives.append("I am an emotionally stable person and I want to maintain my balance.")
                    
            elif trait == "Extraversion":
                if score > mid+10:
                    objetives.append("I am an extroverted person and I want to maintain my social energy.")
                elif score < mid-10:
                    objetives.append("I am an introverted person and I want to increase my extraversion.")    
            
            elif trait == "Openness":
                if score > mid+10:
                    objetives.append("I am a person open to new experiences and I want to enhance my creativity.")
                elif score < mid-10:
                    objetives.append("I am a person with little openness to experience and I want to increase my creativity and curiosity.")
                 
            elif trait == "Agreeableness":
                if score > mid+10:
                    objetives.append("I am a very cooperative person and I want to maintain my high empathy.")
                elif score < mid-10:
                    objetives.append("I am a less cooperative person and I want to increase my empathy and kindness.")
                 
            elif trait == "Conscientiousness":
                if score > mid+10:
                    objetives.append("I am an organized person and I want to maintain my high level of commitment.")
                elif score < mid-10:
                    objetives.append("I am a disorganized person and I want to increase my responsibility and organization.")

    return objetives