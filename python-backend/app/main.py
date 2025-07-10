import logging

logging.basicConfig(level=logging.INFO)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import api_router
from .core.config import settings
from app.core.database import engine
from sqlalchemy import text

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Python FastAPI Backend",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
async def root():
    return {"message": "Python FastAPI Backend is running!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


def check_mysql_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logging.info("✅ MySQL 연결 성공!")
    except Exception as e:
        logging.error(f"❌ MySQL 연결 실패: {e}")


@app.on_event("startup")
async def startup_event():
    check_mysql_connection()
    # 테이블 생성
    from app.core.database import create_tables

    create_tables()
    logging.info("✅ 데이터베이스 테이블 생성 완료!")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
