from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time

from src.api.routers import (
    health,
    companies,
    screener,
    sectors,
    peers,
    valuation,
    portfolio,
    documents
)

app = FastAPI(
    title="Nifty100 Analytics API",
    description="Financial Intelligence Platform API",
    version="1.0.0"
)

# -------------------------------
# CORS Middleware
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------
# Request Logging Middleware
# -------------------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    process_time = time.time() - start

    print(
        f"{request.method} {request.url.path} "
        f"{process_time:.3f} sec"
    )

    return response


# -------------------------------
# Home Endpoint
# -------------------------------
@app.get("/")
def home():
    return {
        "message": "Welcome to Nifty100 Analytics API",
        "docs": "/docs",
        "version": "1.0.0"
    }


# -------------------------------
# API Routers
# -------------------------------
app.include_router(
    health.router,
    prefix="/api/v1/health",
    tags=["Health"]
)

app.include_router(
    companies.router,
    prefix="/api/v1/companies",
    tags=["Companies"]
)

app.include_router(
    screener.router,
    prefix="/api/v1/screener",
    tags=["Screener"]
)

app.include_router(
    sectors.router,
    prefix="/api/v1/sectors",
    tags=["Sectors"]
)

app.include_router(
    peers.router,
    prefix="/api/v1/peers",
    tags=["Peers"]
)

app.include_router(
    valuation.router,
    prefix="/api/v1/valuation",
    tags=["Valuation"]
)

app.include_router(
    portfolio.router,
    prefix="/api/v1/portfolio",
    tags=["Portfolio"]
)

app.include_router(
    documents.router,
    prefix="/api/v1/documents",
    tags=["Documents"]
)