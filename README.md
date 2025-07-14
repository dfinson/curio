# curio

Curio is an adaptive interview engine powered by CrewAI. It dynamically asks questions, pulls in optional web research, and compiles polished text.

## Development

### Backend (Python)

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and fill in your API keys and URLs.

3. Start the API server:

```bash
uvicorn src.app:app --reload
```

### Frontend (React)

1. Inside `widget/`, install npm dependencies:

```bash
cd widget
npm install
```

2. Copy `.env.example` to `.env` and adjust the `VITE_WS_URL` if needed.

3. Run the development server:

```bash
npm run dev
```

The React widget connects to the backend WebSocket defined in `VITE_WS_URL`.
