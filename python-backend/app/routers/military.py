from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.military_company import MilitaryCompany

router = APIRouter()


@router.get("/military-companies/frontend")
def get_frontend_military_companies(db: Session = Depends(get_db)):
    companies = (
        db.query(MilitaryCompany)
        .filter(MilitaryCompany.search_keyword == "프론트엔드")
        .all()
    )
    return [
        {
            "id": c.id,
            "company_name": c.company_name,
            "source": c.source,
            "created_at": c.created_at,
        }
        for c in companies
    ]
