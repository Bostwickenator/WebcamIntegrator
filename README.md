# WebcamIntegrator

Integrates many webcam frames into a single image to reduce noise and improve clarity—similar to stacking exposures in astrophotography, but using a live camera feed.

## How it works

The script opens your default webcam and shows two windows:

| Window | Contents |
|--------|----------|
| **live** | The current camera frame |
| **integrate** | A running average of frames captured during integration mode |

When integration is active, each frame is accumulated in 64-bit buffers and divided by the frame count to produce a smoothed result. Random sensor noise tends to cancel out over many frames, while static scene detail remains.

After **100** integrated frames, the result is saved as a PNG in the working directory and the app returns to live-only mode until you start another integration.

## Requirements

- Python 3
- [OpenCV](https://opencv.org/) (`opencv-python`)
- [NumPy](https://numpy.org/)

## Installation

```bash
pip install opencv-python numpy
```

Clone the repository (or download `integrate.py`), then run from the project directory.

## Usage

```bash
python integrate.py
```

Focus the OpenCV window so key presses are received.

| Key | Action |
|-----|--------|
| **R** | Start integration (2 second pause, then averaging begins) |
| **Esc** | Quit |

During integration, keep the camera and subject as still as possible for the best result. The integrated image updates in real time in the **integrate** window.

Saved files are named `opencv_frame_<count>.png` (for example, `opencv_frame_101.png`).

## Configuration

Defaults in `integrate.py`:

- **Resolution:** 1280×720 (commented lines allow 1920×1080)
- **Integration length:** 100 frames before auto-save
- **Camera index:** `0` (first webcam)

To change resolution, uncomment or edit the `CAP_PROP_FRAME_WIDTH` / `CAP_PROP_FRAME_HEIGHT` settings. To integrate more or fewer frames before saving, change the `img_counter > 100` check.

## Platform notes

The script uses `cv2.CAP_DSHOW` (DirectShow), which is intended for **Windows**. On Linux or macOS, remove the backend flag or use the appropriate capture API for your system:

```python
cam = cv2.VideoCapture(0)  # Linux / macOS
```

You need a display attached for the OpenCV GUI windows (`imshow`).

## License

No license file is included in this repository. Contact the maintainer for usage terms if you plan to redistribute or modify the project.
