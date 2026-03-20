import streamlit as st
from extractor import extract_text_from_pdf
from preprocess import preprocess_text
from features import get_tfidf_vectors
from similarity import calculate_similarity
from skills import extract_skills
from suggestions import get_missing_skills, generate_suggestions

st.title("Smart Resume Analyzer")

resume_file = st.file_uploader("Upload Resume (PDF)")
jd_text = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume_file and jd_text:
        resume_text = extract_text_from_pdf(resume_file)
        clean_resume = preprocess_text(resume_text)
        clean_jd = preprocess_text(jd_text)

        vectors = get_tfidf_vectors(clean_resume, clean_jd)
        score = calculate_similarity(vectors)

        resume_skills = extract_skills(clean_resume)
        jd_skills = extract_skills(clean_jd)

        missing = get_missing_skills(jd_skills, resume_skills)
        suggestions = generate_suggestions(missing)

        st.subheader(f"Match Score: {score}%")

        st.write("### Missing Skills")
        st.write(missing)

        st.write("### Suggestions")
        st.write(suggestions)

    else:
        st.warning("Please upload resume and enter job description")
