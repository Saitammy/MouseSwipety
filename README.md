# MouseSwipety

**MouseSwipety** is a Python-based utility that detects whether your mouse is swiping to the left or to the right. It’s perfect for tracking directional swipe gestures or building gesture-based applications.

---

## Features

- Detects horizontal mouse swipe direction (left or right).
- ⏱ Responsive, with real-time detection.
- Minimal configuration required.

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Saitammy/MouseSwipety.git
   cd MouseSwipety
   ```

2. **Set up your environment**

   It's recommended to use a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate     # On Unix or macOS
   venv\Scripts\activate.bat    # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *If there's no `requirements.txt`, specify dependencies manually here (e.g., `pyautogui`, `pynput`, etc.).*

---

## Usage

Run the main script:

```bash
python MouseSwipety.py
```

Once running, move your mouse horizontally (left or right) to trigger detection. Based on the movement, appropriate feedback will be provided (e.g., console messages or callback invocations).

Customize behavior by editing parameters like swipe threshold, direction sensitivity, or output handling (e.g., trigger events or logs).

---

## Examples

```python
# Example pseudocode integration:

from MouseSwipety import SwipeDetector

def on_swipe(direction):
    print(f"Detected swipe: {direction}")

detector = SwipeDetector(on_swipe_callback=on_swipe, threshold=50)
detector.start()
```

---

## Configuration

| Option       | Description                            | Default |
|--------------|----------------------------------------|---------|
| `threshold`  | Minimum horizontal movement (pixels) to trigger a swipe | `50`     |
| `callback`   | Function to invoke when a swipe is detected | `None`  |

*(Update table based on actual implementation details.)*

---

## Contribution

Contributions, suggestions, and pull requests are welcome! To contribute:

1. Fork the repo.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes and push the branch.
4. Open a Pull Request.

---

## License

Specify the project’s license here—e.g., MIT License, Apache 2.0, etc. *(Add `LICENSE` file if available.)*

---

## Acknowledgements

- Based on idea: *Checks if your mouse is swiping right or left* ([github.com](https://github.com/Saitammy/MouseSwipety)).
- Contributors and inspirations.

---
