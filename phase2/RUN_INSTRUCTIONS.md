# ForgeryGuard AI — Phase 2 run instructions

## 1. Download the portable service

Download the `phase2-v1` release or the Blackboard source archive. The API needs
these files in the same `M8_deployment` directory:

- `phase2_api.py`
- `m4_detector.pt`
- `m5_segmenter.ts`

The original DEFACTO/MSCOCO dataset is not needed for inference.

## 2. Windows prerequisites

Use **64-bit Python 3.13**. Python 3.14 was not used for the verified run. Install
the **Microsoft Visual C++ Redistributable 2015–2022 (x64)** before importing
PyTorch; a missing runtime may produce a `c10.dll` / `WinError 1114` error.

Verify Python:

```powershell
py -3.13 --version
```

## 3. Windows PowerShell setup

Open PowerShell in the extracted source folder, which contains
`requirements.txt` and `M8_deployment`:

```powershell
py -3.13 -m venv M8_deployment\.venv
.\M8_deployment\.venv\Scripts\python.exe -m pip install --upgrade pip
.\M8_deployment\.venv\Scripts\python.exe -m pip install -r requirements.txt
cd M8_deployment
.\.venv\Scripts\python.exe -m uvicorn phase2_api:app --host 127.0.0.1 --port 8000
```

If PowerShell is already inside `M8_deployment`, use:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r ..\requirements.txt
.\.venv\Scripts\python.exe -m uvicorn phase2_api:app --host 127.0.0.1 --port 8000
```

## 4. macOS/Linux setup

Run from the extracted source folder:

```bash
python3.13 -m venv M8_deployment/.venv
M8_deployment/.venv/bin/python -m pip install --upgrade pip
M8_deployment/.venv/bin/python -m pip install -r requirements.txt
cd M8_deployment
.venv/bin/python -m uvicorn phase2_api:app --host 127.0.0.1 --port 8000
```

## 5. Verify the service

Open:

- Swagger UI: <http://127.0.0.1:8000/docs>
- Health check: <http://127.0.0.1:8000/health>

Expected health response:

```json
{"status":"ok","device":"cpu"}
```

Test a JPG or PNG from a second PowerShell window:

```powershell
curl.exe -X POST "http://127.0.0.1:8000/predict" -F "file=@C:\path\to\test.jpg"
```

The independently verified Windows run used Python `3.13.17`, returned HTTP
`200` from `/predict`, and loaded both models on CPU. CPU latency is machine
dependent and is not comparable to the Tesla T4 benchmark in the report.

## 6. Full Kaggle notebook reproduction

1. Open `ForgeryGuard_AI_Phase2_M4_M5_M8.ipynb` in Kaggle.
2. Attach the project manifest/originals input and the authorised DEFACTO
   Copy-Move forged-image/mask input.
3. Enable a GPU and Internet.
4. Add `WANDB_API_KEY` through Kaggle Secrets for a new online run.
5. Run cells in order and complete the displayed human-review fields from the
   actual galleries.

Exact Kaggle versions are stored in `reproducibility/requirements-kaggle.txt`.

## Scope

The final decision is `NO_GO_FOR_AUTONOMOUS_USE`. The service is an academic
demonstration and human-review aid; it is not legal proof of forgery.
