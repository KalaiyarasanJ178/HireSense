def get_missing_skills(jd_skills, resume_skills):
    return list(set(jd_skills) - set(resume_skills))


def generate_suggestions(missing_skills):
    suggestions = []
    for skill in missing_skills:
        suggestions.append(f"Consider adding projects or experience related to {skill}")
    return suggestions
