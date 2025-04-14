import token
from urllib import response
from authx import AuthX

from config import jwt_config

from database import get_session

from fastapi import APIRouter, Depends, HTTPException, Request, Response


from repositories.user import UserRepositories as user_repo
from schemas.users import UserLogin


router = APIRouter()


authx_security = AuthX(config=jwt_config)


@router.post("/login")
async def login(creds: UserLogin, response: Response, session=Depends(get_session)):
    repo = user_repo(session)
    user = await repo.get_by_email(creds.email)
    if user and user.password == creds.password:
        token = authx_security.create_access_token(uid=str(user.id))
        response.set_cookie(key="access_token", value=token)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.post("/register")
async def register():
    return {"message": "Register endpoint"}

@router.get("/logout")
async def logout():
    return {"message": "Logout endpoint"}

@router.get("/me")
async def me(request: Request, session=Depends(get_session)):
    
    uid = await get_current_user(request)
    repo = user_repo(session)
    user = await repo.get_user(uid)
    if uid:
        return {
            "id": user.id,
            "nickname": user.username,
            "email": user.email,
        }


    
async def get_current_user(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Token not found in cookies")

    try:
        payload = authx_security._decode_token(token)
        uid = payload.sub  # Assuming "sub" is an attribute of the TokenPayload object
        return uid
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")