from authx import AuthX
from config import jwt_config
from database import get_session
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from passlib.context import CryptContext
from repositories.user import UserRepositories as user_repo
from schemas.users import UserCreate, UserLogin, UserOut

router = APIRouter()


authx_security = AuthX(config=jwt_config)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login")
async def login(creds: UserLogin, response: Response, session=Depends(get_session)):
    repo = user_repo(session)
    user = await repo.get_by_email(creds.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Use pwd_context.verify to compare the plain password with the hashed password
    if pwd_context.verify(creds.password, user.password):
        token = authx_security.create_access_token(uid=str(user.id))
        response.set_cookie(key="access_token", value=token)
        return {"access_token": token}

    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.post("/register")
async def register(creds: UserCreate, response: Response, session=Depends(get_session)):
    repo = user_repo(session)
    existing_user = await repo.get_by_email(creds.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = pwd_context.hash(creds.password)

    await repo.create_user(email=creds.email, password=hashed_password, username=creds.username)
    return {"msg": "User created successfully"}

@router.get("/logout")
async def logout():
    return {"message": "Logout endpoint"}

@router.get("/me", response_model=UserOut)
async def me(request: Request, session=Depends(get_session)):
    uid = await get_current_user(request)
    if not uid:
        raise HTTPException(status_code=401, detail="Unauthorized")

    repo = user_repo(session)
    try:
        user = await repo.get_user(uid)
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found or invalid token")
    user = await repo.get_user(uid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


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