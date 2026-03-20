skill_list = [
    "python", "java", "c++", "machine learning", "deep learning",
    "nlp", "sql", "react", "node", "data analysis"
]

def extract_skills(text):
    found = []
    for skill in skill_list:
        if skill in text:
            found.append(skill)
    return found
