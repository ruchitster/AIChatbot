import { useState } from "react";
import { uploadFiles } from "../services/uploadService";

export default function FileUpload({ setError }) {
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [successMsg, setSuccessMsg] = useState("");

  const handleUpload = async () => {
    if (!files || files.length === 0) return;

    try {
      setLoading(true);
      setSuccessMsg("");
      setError("");

      const result = await uploadFiles(Array.from(files));

      setSuccessMsg(
        `${result.documents.length} file(s) uploaded successfully`
      );

      setFiles([]);
    } catch (error) {
      console.error(error);
      setError("❌ Upload failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginBottom: "15px" }}>

      <input
        type="file"
        multiple
        accept=".pdf,image/*"
        onChange={(e) => setFiles(e.target.files)}
      />

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Uploading..." : "Upload"}
      </button>

      {/* SUCCESS MESSAGE */}
      {successMsg && (
        <div style={{ color: "green", marginTop: "8px", fontSize: "13px" }}>
          {successMsg}
        </div>
      )}

      {/* FILE LIST */}
      {files?.length > 0 && (
        <div style={{ marginTop: "10px", fontSize: "14px" }}>
          Selected:
          <ul>
            {Array.from(files).map((file, index) => (
              <li key={index}>{file.name}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}