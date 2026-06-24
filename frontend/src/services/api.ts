
const API_BASE = "http://127.0.0.1:8000";

export async function analyzeJob(
    jobDescription: string
) {
    const response = await fetch(
        `${API_BASE}/analyze`,
        {
            method:'POST',

        headers: {
            "Content-Type":"application/json",

        },

        body: JSON.stringify({
            job_description: jobDescription,

        }),
        

        }
    );
    return response.json();
}
