import { useState } from "react";
import { uploadResume } from "../services/api";

const Resume = () => {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [message, setMessage] = useState("");

    const handleFileChange = (
        event: React.ChangeEvent<HTMLInputElement>
    ) => {
        if(event.target.files && event.target.files.length > 0) {
            setSelectedFile(event.target.files[0]);
        }

    };

    const handleUpload = async() => {
      if(!selectedFile) {
        alert("Please select a resume");
        return;
     }
      

      try {
        await uploadResume(selectedFile);
        setMessage("Resume Uploaded Successfully!!!")
        setSelectedFile(null);
      }
      catch {
        setMessage("Resume Uploading failed!!!")
      }
    };

    return (
  <div className="max-w-5xl mx-auto">

    <h1 className="text-4xl font-bold text-slate-800 mb-3">
      Upload Resume
    </h1>

    <p className="text-slate-600 mb-8">
      Upload your latest resume and let AI analyze your skills,
      identify gaps, and generate a personalized learning roadmap.
    </p>

    <div className="bg-white rounded-2xl shadow-sm border p-8">

      <div
        className="
          border-2
          border-dashed
          border-blue-300
          rounded-2xl
          p-12
          text-center
          bg-slate-50
        "
      >

        <div className="text-6xl mb-4">
          📄
        </div>

        <h2 className="text-2xl font-semibold text-slate-800 mb-2">
          Upload Your Resume
        </h2>

        <p className="text-slate-500 mb-2">
          Supports PDF, DOC and DOCX files
        </p>

        <p className="text-slate-400 text-sm mb-6">
          Maximum file size: 10MB
        </p>

        <label
          className="
            inline-block
            cursor-pointer
            bg-blue-600
            hover:bg-blue-700
            transition
            text-white
            px-6
            py-3
            rounded-xl
            font-medium
          "
        >
          Choose Resume

          <input
            type="file"
            accept=".pdf,.doc,.docx"
            onChange={handleFileChange}
            className="hidden"
          />
        </label>

        <div className="mt-5">
          {selectedFile ? (
            <span
              className="
                bg-green-100
                text-green-700
                border
                border-green-200
                px-4
                py-2
                rounded-full
                font-medium
              "
            >
              ✓ {selectedFile.name}
            </span>
          ) : (
            <p className="text-slate-500">
              No file selected
            </p>
          )}
        </div>

      </div>

      <div className="mt-6">
        <button
          onClick={handleUpload}
          disabled={!selectedFile}
          className="
            bg-blue-600
            hover:bg-blue-700
            disabled:bg-gray-300
            disabled:cursor-not-allowed
            transition
            text-white
            px-6
            py-3
            rounded-xl
            font-medium
          "
        >
          Upload Resume
        </button>
      </div>

      {message && (
        <div
          className="
            mt-6
            bg-green-50
            border
            border-green-200
            text-green-700
            p-4
            rounded-xl
          "
        >
          {message}
        </div>
      )}
    </div>

    <div className="grid md:grid-cols-3 gap-6 mt-8">

      <div className="bg-white rounded-xl border p-6">
        <div className="text-3xl mb-3">
          🤖
        </div>

        <h3 className="font-bold mb-2">
          AI Skill Extraction
        </h3>

        <p className="text-slate-600 text-sm">
          Automatically extracts technical skills from your resume using local AI models.
        </p>
      </div>

      <div className="bg-white rounded-xl border p-6">
        <div className="text-3xl mb-3">
          🎯
        </div>

        <h3 className="font-bold mb-2">
          Resume Matching
        </h3>

        <p className="text-slate-600 text-sm">
          Compare your resume against job descriptions and identify missing skills.
        </p>
      </div>

      <div className="bg-white rounded-xl border p-6">
        <div className="text-3xl mb-3">
          🚀
        </div>

        <h3 className="font-bold mb-2">
          Learning Roadmap
        </h3>

        <p className="text-slate-600 text-sm">
          Receive a personalized AI-generated roadmap to close skill gaps.
        </p>
      </div>

    </div>

  </div>
);
};


export default Resume