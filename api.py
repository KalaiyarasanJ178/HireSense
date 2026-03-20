from flask import Flask, request, jsonify
from extractor import extract_text_from_pdf
from preprocess import preprocess_text
from features import get_tfidf_vectors
from similarity import calculate_similarity
from skills import extract_skills
from suggestions import get_missing_skills, generate_suggestions

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    jd = request.form['jd']

    resume_text = extract_text_from_pdf(file)
    clean_resume = preprocess_text(resume_text)
    clean_jd = preprocess_text(jd)

    vectors = get_tfidf_vectors(clean_resume, clean_jd)
    score = calculate_similarity(vectors)

    resume_skills = extract_skills(clean_resume)
    jd_skills = extract_skills(clean_jd)

    missing = get_missing_skills(jd_skills, resume_skills)
    suggestions = generate_suggestions(missing)

    return jsonify({
        "score": score,
        "missing": missing,
        "suggestions": suggestions
    })

if __name__ == '__main__':
    app.run(debug=True)
