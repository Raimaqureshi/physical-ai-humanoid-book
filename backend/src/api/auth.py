# backend/src/api/auth.py

from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any

from backend.src.services.user_service import user_service
from backend.src.services.auth_external import external_auth_service
from backend.src.models.user import UserCreate, User, Token, TokenData, UserInDB

# Configuration for JWT (from .env.example)
SECRET_KEY = "your_super_secret_key" # TODO: Load from environment variable
ALGORITHM = "HS256" # TODO: Load from environment variable
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # TODO: Load from environment variable

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = await user_service.get_user_by_email(token_data.email)
    if user is None:
        raise credentials_exception
    return User.model_validate(user)

@router.post("/signup", response_model=User, status_code=status.HTTP_201_CREATED)
async def signup(user_create: UserCreate):
    """
    Register a new user in the system.
    """
    try:
        new_user_in_db = await external_auth_service.register_external_user(user_create)
        return User.model_validate(new_user_in_db)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/signin", response_model=Token)
async def signin(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate user and issue an access token.
    """
    user_in_db = await external_auth_service.authenticate_external_user(form_data.username, form_data.password)
    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_in_db.email}, expires_delta=access_token_expires
    )
    
    # Optionally set http-only cookie for better security
    # response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True, samesite="Lax")
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    """
    Get the current authenticated user's profile.
    """
    return current_user

# --- JWT imports needed after defining SECRET_KEY etc. (dynamic import workaround) ---
# This is a common pattern for FastAPI if you prefer to define constants first.
# In a real project, these would likely be loaded from a config module.
from jose import JWTError, jwt
