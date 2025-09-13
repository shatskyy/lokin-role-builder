from __future__ import annotations

from fastapi import FastAPI


app = FastAPI(title="lokin-role-builder")


@app.get("/healthz")
def healthz() -> dict[str, bool]:
    return {"ok": True}


