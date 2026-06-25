import { useState } from "react";

const Resume = () => {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);

    const handleFileChange = (
        event: React.ChangeEvent<HTMLInputElement>
    ) => {
        if(event.target.files && event.target.files.length > 0) {
            setSelectedFile(event.target.files[0]);
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
        >
          Upload Resume
        </button>

      </div>
    </div>
  );
};


export default Resume