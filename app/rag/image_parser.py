from google import genai
from app.core.config import GEMINI_API_KEY

client = genai.Client(
    api_key=GEMINI_API_KEY
)

def extract_image_text(image_path):

    uploaded_file = client.files.upload(
        file=image_path
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            uploaded_file,
            """
            Extract all visible text from this image.
            If it is a document, preserve formatting.
            Return only the extracted content.
            """
        ]
    )

    return response.text