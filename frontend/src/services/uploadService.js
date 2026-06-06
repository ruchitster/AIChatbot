const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL;

export const uploadFiles = async (
  files
) => {
  const formData = new FormData();

  files.forEach((file) => {
    formData.append(
      "files",
      file
    );
  });

  const response = await fetch(
    `${API_BASE_URL}/upload`,
    {
      method: "POST",
      body: formData,
    }
  );

  if (!response.ok) {
    throw new Error(
      "Upload failed"
    );
  }

  return await response.json();
};