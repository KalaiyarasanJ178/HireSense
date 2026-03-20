async function analyzeResume() {
  const fileInput = document.getElementById("resumeFile");
  const jd = document.getElementById("jd").value;

  if (!fileInput.files[0] || !jd) {
    alert("Upload resume and enter job description");
    return;
  }

  document.getElementById("loader").classList.remove("hidden");
  document.getElementById("result").classList.add("hidden");

  const formData = new FormData();
  formData.append("resume", fileInput.files[0]);
  formData.append("jd", jd);

  try {
    const response = await fetch("http://localhost:5000/analyze", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    document.getElementById("loader").classList.add("hidden");
    document.getElementById("result").classList.remove("hidden");

    document.getElementById("score").innerText = `🎯 Match Score: ${data.score}%`;

    const missingList = document.getElementById("missing");
    missingList.innerHTML = "";
    data.missing.forEach(skill => {
      const li = document.createElement("li");
      li.innerText = skill;
      missingList.appendChild(li);
    });

    const suggestionList = document.getElementById("suggestions");
    suggestionList.innerHTML = "";
    data.suggestions.forEach(s => {
      const li = document.createElement("li");
      li.innerText = s;
      suggestionList.appendChild(li);
    });

  } catch (error) {
    alert("Backend error. Make sure Flask server is running.");
  }
}
