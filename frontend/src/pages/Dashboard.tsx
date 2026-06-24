import { useState } from "react";
import { analyzeJob } from "../services/api";

type AnalysisResult = {
  role: string;
  skills: string[];
  difficulty: string;
  market_demand: string;
  recommended_learning: string[];
  match_score: number;
  matched_skills: string[];
  missing_skills: string[];
};

export default function Dashboard() {
  const [jobDescription, setJobDescription] = useState("");

  const [result, setResult] =
    useState<AnalysisResult | null>(null);

  async function handleAnalyze() {
    try {
      const data = await analyzeJob(
        jobDescription
      );

      setResult(data);

    } catch (error) {
      console.error(error);

      alert("Analysis failed.");
    }
  }

  return (
    <div className="min-h-screen bg-slate-100 flex justify-center">

      <div className="w-full max-w-4xl p-10">

        <h1 className="text-5xl font-bold mb-8">
          Career Copilot AI
        </h1>

        <p className="mb-4">
          Paste a job description
        </p>

        <textarea
          className="w-full p-4 border rounded-lg"
          rows={10}
          value={jobDescription}
          onChange={(e) =>
            setJobDescription(
              e.target.value
            )
          }
        />

        <button
          className="bg-blue-600 text-white px-6 py-3 rounded-lg mt-5"
          onClick={handleAnalyze}
        >
          Analyze
        </button>

        {result && (

          <div className="mt-10 bg-white p-8 rounded-xl shadow">

            <h2 className="text-3xl font-bold mb-6">
              {result.role}
            </h2>

            <h3 className="font-bold mb-2">
              Skills
            </h3>

            <div className="flex flex-wrap gap-2 mb-8">

              {result.skills.map((skill) => (

                <span
                  key={skill}
                  className="bg-blue-100 px-3 py-1 rounded-full"
                >
                  {skill}
                </span>

              ))}

            </div>

            <h3 className="font-bold">
              Difficulty
            </h3>

            <p>
              {result.difficulty}
            </p>

            <h3 className="font-bold mt-5">
              Market Demand
            </h3>

            <p>
              {result.market_demand}
            </p>

            <h3 className="font-bold mt-5">
              Match Score
            </h3>

            <p className="text-2xl font-bold text-green-600">
              {result.match_score}%
            </p>

            <h3 className="font-bold mt-5">
              Matched Skills
            </h3>

            <div className="flex flex-wrap gap-2">

              {result.matched_skills.map((skill) => (

                <span
                  key={skill}
                  className="bg-green-100 px-3 py-1 rounded-full"
                >
                  {skill}
                </span>

              ))}

            </div>

            <h3 className="font-bold mt-5">
              Missing Skills
            </h3>

            <div className="flex flex-wrap gap-2">

              {result.missing_skills.map((skill) => (

                <span
                  key={skill}
                  className="bg-red-100 px-3 py-1 rounded-full"
                >
                  {skill}
                </span>

              ))}

            </div>

            <h3 className="font-bold mt-5">
              Recommended Learning
            </h3>

            <ul className="list-disc ml-6">

              {result.recommended_learning.map((item) => (

                <li key={item}>
                  {item}
                </li>

              ))}

            </ul>

          </div>

        )}

      </div>

    </div>
  );
}