# GDis-transcribe

This is an HTTP wrapper for [rhasspy piper](https://github.com/rhasspy/piper)

It is intended to be used with [GDis-server](https://github.com/SquirrelsMcGee/GDis-server) but can be used on it's own

# Setup
These steps assume you have some python knowledge. Please search online for help if you get stuck, raise an issue if you really need it.

1. Ensure you have python installed (I'm using 3.10.6)
2. Install dependencies, [Pydantic](https://pypi.org/project/pydantic/), [fastapi](https://fastapi.tiangolo.com/tutorial/)
3. Download the [latest release build of Piper here](https://github.com/rhasspy/piper/releases/latest), for windows download piper_windows_amd64.zip
4. Extract the contents to {Gdis-piper-tts location}/piper

> ![image](https://github.com/user-attachments/assets/30f30c3b-c59b-4aec-9dba-9e6547518a43)

5. Create another folder called {GDis-piper-tts location}/voices

> ![image](https://github.com/user-attachments/assets/7b09043f-e1f6-4f81-9614-b016f9d1751f)

6. Download a compatible voice from [Piper's provided sample voices](https://github.com/rhasspy/piper/blob/master/VOICES.md), download both the model and the config file, and save them to the ./voices folder. ***I would recommend hfc_male or hfc_female as I had issues getting other voices to work***

7. Run using `run.ps1` or `uvicorn main:app --reload --port 5010`

> Note port 5010 is the default used by GDis

8. Generate a voice sample by making an HTTP post request to http://localhost:5010/api/tts with x-www-form-urlencoded data

> ![image](https://github.com/user-attachments/assets/65babf7e-8f79-4143-95eb-89181893f186)


