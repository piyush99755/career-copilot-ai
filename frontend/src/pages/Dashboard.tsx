import { useState } from "react";

import { analyzeJob } from "../services/api" ;

export default function Dashboard() {

    type AnalysisResult = {
        role: string;
        skills: string[];
        roadmap: string[];
    };

  const [jobDescription, setJobDescription] =
    useState("");

  const [result, setResult] =
    useState<AnalysisResult | null>(null);

  async function handleAnalyze() {

    const data = await analyzeJob(
      jobDescription
    );

    setResult(data);
  }

  return (
    <div style={{ padding: "30px" }}>

      <h1>Career Copilot AI</h1>

      <p>
        Paste a job description
      </p>

      <textarea

        rows={10}

        cols={80}

        value={jobDescription}

        onChange={(e) =>
          setJobDescription(
            e.target.value
          )
        }

      />

      <br />

      <button
        onClick={handleAnalyze}
      >

        Analyze

      </button>

      {result && (

        <div>

          <h3>

            {result.role}

          </h3>

          <ul>

            {result.skills.map(
              (skill: string) => (

                <li key={skill}>

                  {skill}

                </li>

              )
            )}

          </ul>

        </div>

      )}

    </div>
  );
}