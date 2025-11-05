# Space Station Manager

A space station building and management game built with Pygame.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python main.py
```

## Architecture

- **backend/**: Pure Python game logic (no Pygame dependencies)
- **frontend/**: Pygame rendering and input handling
- **assets/**: Game assets (audio, graphics, data)
- **utils/**: Shared utilities

## Development

The game uses a clean separation between backend (logic) and frontend (presentation).
This allows for easy testing and the ability to swap view modes (side view vs top-down).

## Testing

Run tests with:
```bash
pytest tests/
```
