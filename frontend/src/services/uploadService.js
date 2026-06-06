const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ||
  "https://airag-0g3a.onrender.com";

export const uploadFiles = async (files) => {
  try {
    const formData = new FormData();

    files.forEach((file) => {
      formData.append("files", file);
    });

    const response = await fetch(
      `${API_BASE_URL}/upload`,
      {
        method: "POST",
        body: formData,
      }
    );

    if (!response.ok) {
      const errorText = await response.text();
      console.error("Upload failed response:", errorText);
      throw new Error(errorText || "Upload failed");
    }

    const data = await response.json();
    return data;

  } catch (error) {
    console.error("Upload error:", error);
    throw error;
  }
};