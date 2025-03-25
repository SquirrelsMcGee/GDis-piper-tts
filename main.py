from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel
import subprocess
import os

app = FastAPI()

# Define the path to your Piper executable and model
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Get the directory where the script is located
PIPER_PATH = os.path.join(BASE_DIR, "piper", "piper.exe")
MODEL_PATH = os.path.join(BASE_DIR, "voices", "en_US-hfc_male-medium.onnx")

print(f"Using BASE_DIR {BASE_DIR}")
print(f"Using PIPER_PATH {PIPER_PATH}")
print(f"Using MODEL_PATH {MODEL_PATH}")

try:
    process = subprocess.run(
        [PIPER_PATH, "--help"],
        check=True
    )

    print("Piper is accessible.")
except Exception as e:
    print(f"Error accessing Piper: {e}")

# Pydantic model for request validation
class TextInput(BaseModel):
    text: str

@app.post("/api/tts")
async def generate_audio(
    text: str = Form(...)
):
    try:
        # Ensure text is provided
        input_text = text.strip()
        if not input_text:
            raise HTTPException(status_code=400, detail="No text provided")

        # Define output file
        output_file = os.path.join(BASE_DIR, "output.wav")

        # Construct the command
        
        print(PIPER_PATH)
        print(MODEL_PATH)
        print(output_file)
        
        process = subprocess.run(
            [PIPER_PATH, "--model", MODEL_PATH, "--output_file", output_file],
            input=input_text.encode(),  # Pass text as stdin
            check=True,
            capture_output=True
        )

        # Run the command
        #subprocess.run(command, shell=False, check=True)

        # Check if the file was created
        if not os.path.exists(output_file):
            raise HTTPException(status_code=500, detail="Failed to generate audio file")

        # Return the output file
        return FileResponse(output_file, media_type="audio/wav", filename=output_file)

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Command execution failed: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

