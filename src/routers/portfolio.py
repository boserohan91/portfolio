from typing import List
from portfolio.backend.src.database import get_db
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from .. import models as mod
from ..database import get_db
from .. import schemas as sch

router = APIRouter(
    prefix='/portfolio/'
)

@router.post('', status_code=status.HTTP_201_CREATED)
async def create_basic(profile: sch.BasicDetails, db: Session = Depends(get_db)):
    new_profile = mod.BasicDetails(
        name=profile.name,
        address=profile.address,
        telephone=profile.telephone,
        email=profile.email,
        gender=profile.gender,
        dob=profile.dob,
        nationality=profile.nationality
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return {
        'id':new_profile.id,
        'name':new_profile.name
    }

@router.get('/listall', status_code=status.HTTP_200_OK, response_model=List[sch.User])
async def get_user_list(db: Session = Depends(get_db)):
    profiles = db.query(mod.BasicDetails).all()
    response_profiles : List[sch.User] = []
    for profile in profiles:
        each_profile = sch.User(
            id=profile.id,
            name=profile.name
        )
        response_profiles.append(each_profile)
    return response_profiles
