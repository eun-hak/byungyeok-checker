from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class MilitaryCompany(Base):
    __tablename__ = "military_companies"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(255), nullable=False, index=True)
    original_company_id = Column(Integer, nullable=True)  # 원본 companies 테이블의 id
    search_keyword = Column(
        String(100), nullable=False
    )  # 검색 키워드 (예: "프론트엔드")
    source = Column(String(50), nullable=False)  # 출처 (예: "wanted")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
