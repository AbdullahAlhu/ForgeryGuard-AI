# Independent local deployment verification

The FastAPI deployment was tested independently on Windows outside Kaggle.

| Item | Verified value |
|---|---|
| Python | 3.13.17, 64-bit |
| Service host | `127.0.0.1:8000` |
| Device | CPU |
| `GET /health` | `200`, `{"status":"ok","device":"cpu"}` |
| `POST /predict` | HTTP 200 with JSON response |
| Test response | `no_region_detected`, zero boxes, zero mask pixels |
| Observed request latency | 194.37 ms on the tested Windows machine |

The submitted test image visibly contained duplicated trees, while the service
returned no detected region. This is retained as a qualitative false-negative
example and is consistent with the detector's measured recall limitation. The
Windows latency is a functional verification only; the report's controlled
benchmark uses a Tesla T4, batch size 1, 5 warm-ups, and 50 measured images.
