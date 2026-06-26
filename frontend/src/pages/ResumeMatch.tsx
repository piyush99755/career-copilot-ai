import { useState } from "react";
import { matchResume } from "../services/api";

interface ResumeMatchResult {
  match_score: number;
  matched_skills: string[];
  missing_skills: string[];
}

const ResumeMatch = () => {
    const [jobDescription, setJobDescription] = useState("");
    const [resumeMatch, setResumeMatch] = useState<ResumeMatchResult | null>(null);
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState("");
    
    const handleResumeMatch = async() => {

        if(!jobDescription.trim()) {
            setMessage("Please enter a job description.");
            return; 
        }
        setLoading(true);
        setMessage("");

        try{
            const response = await matchResume(jobDescription);
             setResumeMatch(response);
             setMessage("Resume match results fecthed successfully!!!")
             
        } 
             
        catch{
            setMessage("Failed to fetch resume match!!!")
        }
        finally {
            setLoading(false);
        }
    }

    return (
  <div className="min-h-screen bg-slate-100 flex justify-center">
    <div className="w-full max-w-4xl p-10">

      <h1 className="text-4xl font-bold mb-8">
        Resume Match
      </h1>

      <textarea
        className="w-full h-56 border rounded-lg p-4"
        placeholder="Paste a job description here..."
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />

      <button
        onClick={handleResumeMatch}
        className="mt-5 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg"
      >
        Compare Resume
      </button>

      {loading && (
        <p className="mt-5 text-gray-600">
          Comparing...
        </p>
      )}

      {message && (
        <p className="mt-5 text-blue-600">
          {message}
        </p>
      )}

      {resumeMatch && (
        <div className="mt-8 bg-white rounded-lg shadow p-6">

          <h2 className="text-2xl font-bold mb-4">
            Match Score
          </h2>

          <p className="text-4xl text-green-600 font-bold mb-6">
            {resumeMatch.match_score}%
          </p>

          <h3 className="font-bold mb-2">
            Matched Skills
          </h3>

          <div className="flex flex-wrap gap-2 mb-6">
            {resumeMatch.matched_skills.map((skill: string) => (
              <span
                key={skill}
                className="bg-green-100 px-3 py-1 rounded-full"
              >
                {skill}
              </span>
            ))}
          </div>

          <h3 className="font-bold mb-2">
            Missing Skills
          </h3>

          <div className="flex flex-wrap gap-2">
            {resumeMatch.missing_skills.map((skill: string) => (
              <span
                key={skill}
                className="bg-red-100 px-3 py-1 rounded-full"
              >
                {skill}
              </span>
            ))}
          </div>

        </div>
      )}

    </div>
  </div>
);


}

export default ResumeMatch;