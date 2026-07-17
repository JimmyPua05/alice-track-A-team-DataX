"""
Thin HTTP client for the FastAPI backend (STUDENT scaffold).

The dashboard runs NO model logic itself: every prediction, metric and
optimization comes from the backend through these functions. Each returns a
tuple (ok: bool, data_or_error) so pages can show a clean message on failure.

This is the "connect the dashboard to the backend" exercise. Fill the TODOs.
"""
import requests

DEFAULT_BASE = "http://127.0.0.1:8000"


def _detail(resp) -> str:
    """Pull a human message out of an error response (GIVEN)."""
    try:
        detail = resp.json().get("detail", resp.text)
        if isinstance(detail, list):
            return "; ".join(
                f"{'.'.join(map(str, item.get('loc', [])))}: {item.get('msg', item)}"
                for item in detail
            )
        return str(detail)
    except Exception:
        return resp.text or f"HTTP {resp.status_code}"


def health(base: str):
    """GET /health -> (ok, data). GIVEN as the pattern to copy."""
    try:
        r = requests.get(f"{base}/health", timeout=10)
        r.raise_for_status()
        return True, r.json()
    except requests.HTTPError:
        return False, _detail(r)
    except Exception as exc:
        return False, str(exc)


def model_info(base: str):
    # TODO: GET {base}/model-info, same pattern as health(). Return (ok, data_or_error).
    ...


def forecast(base: str, file_bytes: bytes, filename: str, last_hours=None):
    # TODO: POST {base}/forecast as multipart:
    #   params = {"last_hours": last_hours} if last_hours else {}
    #   files  = {"file": (filename, file_bytes, "text/csv")}
    #   requests.post(f"{base}/forecast", files=files, params=params, timeout=120)
    # Return (True, r.json()) on success; (False, _detail(r)) on HTTPError; (False, str(exc)) otherwise.
    ...


def optimize(base: str, payload: dict):
    # TODO: POST {base}/optimize with json=payload, timeout=60. Same (ok, data_or_error) contract.
    ...
