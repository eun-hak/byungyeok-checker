from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQLAlchemy 엔진 생성
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# 세션 로컬 클래스 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# DB 세션 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 테이블 생성 함수
def create_tables():
    from app.models.company import Base as CompanyBase
    from app.models.military_company import Base as MilitaryCompanyBase

    CompanyBase.metadata.create_all(bind=engine)
    MilitaryCompanyBase.metadata.create_all(bind=engine)
