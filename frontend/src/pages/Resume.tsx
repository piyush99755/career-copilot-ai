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
    <div className="max-w-2xl">
      <h1 className="text-3xl font-bold mb-6">
        Upload Resume
      </h1>

      <div className="bg-white shadow rounded-lg p-6 space-y-4">

        <input
          type="file"
          accept=".pdf,.doc,.docx"
          onChange={handleFileChange}
          className="block w-full"
        />

        <p className="text-gray-600">
          {selectedFile
            ? `Selected: ${selectedFile.name}`
            : "No file selected"}
        </p>

        <button
          className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded"
          onClick={handleUpload}
        >
          Upload Resume
        </button>

        {message && (
          <p className="mt-4 text-green-600 font-medium">
            {message}
          </p>
        )}

      </div>
    </div>
  );
};


export default Resume