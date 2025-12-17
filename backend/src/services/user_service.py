# backend/src/services/user_service.py

from typing import Optional, Dict, Any
from passlib.context import CryptContext
from backend.src.models.user import UserCreate, UserInDB, User
import datetime

# In-memory "database" for demonstration purposes
# In a real application, this would interact with Neon Serverless Postgres
_users_db: Dict[str, UserInDB] = {}

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def get_password_hash(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    async def get_user_by_email(self, email: str) -> Optional[UserInDB]:
        for user_id, user in _users_db.items():
            if user.email == email:
                return user
        return None

    async def get_user_by_id(self, user_id: str) -> Optional[UserInDB]:
        return _users_db.get(user_id)

    async def create_user(self, user: UserCreate) -> UserInDB:
        if await self.get_user_by_email(user.email):
            raise ValueError("Email already registered")

        hashed_password = self.get_password_hash(user.password)
        db_user = UserInDB(
            email=user.email,
            hashed_password=hashed_password,
            software_background=user.software_background,
            hardware_robotics_background=user.hardware_robotics_background,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        _users_db[db_user.id] = db_user
        return db_user

    async def update_user(self, user_id: str, updates: Dict[str, Any]) -> Optional[UserInDB]:
        user = await self.get_user_by_id(user_id)
        if not user:
            return None
        
        for key, value in updates.items():
            if key == "password": # Handle password change separately
                user.hashed_password = self.get_password_hash(value)
            elif hasattr(user, key):
                setattr(user, key, value)
        user.updated_at = datetime.datetime.utcnow()
        _users_db[user_id] = user # Ensure the updated object is stored back
        return user

    async def delete_user(self, user_id: str) -> bool:
        if user_id in _users_db:
            del _users_db[user_id]
            return True
        return False

user_service = UserService()
