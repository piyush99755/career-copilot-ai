import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: API_BASE,
  /* headers: {
    "Content-Type": "application/json",
  }, */
});

export async function analyzeJob(jobDescription: string) {
  const response = await api.post("/analyze", {
    job_description: jobDescription,
  });

  return response.data;
}

export async function getHistory() {
  const response = await api.get("/history");
  return response.data;
}

export async function uploadResume(file: File) {
  
  const formData = new FormData();

  formData.append("file", file)
  const response = await api.post("/upload-resume", formData);
  return response.data;

}

export default api;