# kiki
Learn it on the go, remember it for good.
Presented at the Youth Coders Collective hackathon: [detailed information](https://devpost.com/software/kiki-5i6u7v)

## Local development setup 
To get the backend for the project running you need to first have some environment variables set up. Follow the below steps to do that.
We are assuming that you are in the root directory.

**Part A: Environment variables**
1. First, create a `.env` file in the below folder:
    ```bash
    cd backend/kiki/
    touch .env
    ```
2. Now get your Google Gemini API Key from Google's AI Playground. Also get your ElevenLabs API key from the ElevenLabs website. Add both as environment variables:
    ```env
    ELEVENLABS_API_KEY=sk_...
    GEMINI_API_KEY=AI...
    ```
You are done now!

**Part B: Getting the backend to run**
1. First, we need to install the requirements.
    ```bash
    cd backend
    uv venv # create a virtual environment
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    uv pip install -r requirements.txt
    ```
2. Next, some database migrations need to be made.
    ```bash
    cd kiki
    python manage.py migrate
    ```
3. Now we can create a superuser to log into the admin panel (`/mothership` here).  
    ```bash
    # inside backend/kiki/
    python manage.py createsuperuser
    ```
4. Lastly, we can use Django to start a server at the default port (or specify a port).
    ```bash
    python manage.py runserver
    ```
The server should now be running at `http://localhost:8000/`.

**Part C: Getting the user interface to run**

No build step is needed here as the frontend is made with a decoupled Vanilla JavaScript/HTML setup.
1. First, change into the frontend folder
    ```bash
    cd frontend
    ```
2. Now you can serve the files using any local server; we use Python's builtin server here.
    ```bash
    python -m http.server 5500
    ```
You should now be able to access the user interface at `http://localhost:5500`.
