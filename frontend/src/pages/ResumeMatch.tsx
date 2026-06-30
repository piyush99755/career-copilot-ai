import { useState } from "react";
import { matchResume } from "../services/api";

interface ResumeMatchResult {
  match_score: number
  matched_skills: string[]
  missing_skills: string[]
  roadmap: Record<string, string[]>
  recommended_project: string
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
      <div className="w-full max-w-5xl p-10">

        <h1 className="text-4xl font-bold text-slate-800 mb-8">
          Resume Match
        </h1>

        <div className="bg-white rounded-xl shadow-sm border p-6">
          <textarea
            className="w-full h-56 border border-slate-300 rounded-xl p-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Paste a job description here..."
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
          />

          <button
            onClick={handleResumeMatch}
            className="mt-5 bg-blue-600 hover:bg-blue-700 transition text-white px-6 py-3 rounded-xl font-medium"
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
        </div>

        {resumeMatch && (
          <div className="mt-8 bg-white rounded-xl shadow-sm border p-8">

            <h2 className="text-2xl font-bold text-slate-800 mb-6">
              AI Career Analysis
            </h2>

            <div className="flex items-center gap-4 mb-8">
              <div className="text-6xl font-bold text-green-600">
                {resumeMatch.match_score}%
              </div>

              <div>
                <p className="text-sm text-gray-500">
                  Resume Compatibility
                </p>

                <p className="font-semibold text-slate-700">
                  Strong Match
                </p>
              </div>
            </div>

            <div className="mb-8">
              <h3 className="font-bold text-lg mb-3">
                Matched Skills
              </h3>

              <div className="flex flex-wrap gap-2">
                {resumeMatch.matched_skills.map((skill: string) => (
                  <span
                    key={skill}
                    className="
                      bg-green-100
                      text-green-800
                      border
                      border-green-200
                      px-3
                      py-1
                      rounded-full
                      font-medium
                    "
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>

            <div className="mb-8">
              <h3 className="font-bold text-lg mb-3">
                Missing Skills
              </h3>

              <div className="flex flex-wrap gap-2">
                {resumeMatch.missing_skills.map((skill: string) => (
                  <span
                    key={skill}
                    className="
                      bg-red-100
                      text-red-800
                      border
                      border-red-200
                      px-3
                      py-1
                      rounded-full
                      font-medium
                    "
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>

            <h3 className="font-bold text-xl mb-4">
              Learning Roadmap
            </h3>

            <div className="space-y-5">
              {Object.entries(resumeMatch.roadmap).map(
                ([week, topics]) => (
                  <div
                    key={week}
                    className="
                      bg-slate-50
                      border
                      rounded-xl
                      p-5
                      shadow-sm
                      hover:shadow-md
                      transition
                    "
                  >
                    <h4
                      className="
                        text-lg
                        font-bold
                        text-blue-700
                        mb-3
                      "
                    >
                      {week.replace("_", " ").replace("week", "Week")}
                    </h4>

                    <ul className="list-disc list-inside space-y-2 text-slate-700">
                      {topics.map((topic) => (
                        <li key={topic}>
                          {topic}
                        </li>
                      ))}
                    </ul>
                  </div>
                )
              )}
            </div>

            <div className="mt-8">
              <h3 className="font-bold text-xl mb-3">
                🚀 Recommended Project
              </h3>

              <div
                className="
                  bg-linear-to-r
                  from-blue-50
                  to-indigo-50
                  border
                  border-blue-200
                  rounded-xl
                  p-5
                "
              >
                <p className="text-slate-700">
                  {resumeMatch.recommended_project}
                </p>
              </div>
            </div>

          </div>
        )}

      </div>
    </div>
);

}

export default ResumeMatch;