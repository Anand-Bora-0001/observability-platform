import grpc
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.pb import auth_pb2, auth_pb2_grpc

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login/access-token")

# In production, pull this from settings
IDENTITY_GRPC_TARGET = "identity-go:50051"

def get_identity_client() -> auth_pb2_grpc.AuthServiceStub:
    channel = grpc.insecure_channel(IDENTITY_GRPC_TARGET)
    return auth_pb2_grpc.AuthServiceStub(channel)

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
    identity_client: auth_pb2_grpc.AuthServiceStub = Depends(get_identity_client)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Call the Go Identity Service via gRPC
        req = auth_pb2.ValidateTokenRequest(token=token)
        resp = identity_client.ValidateToken(req)
        
        if not resp.is_valid:
            raise credentials_exception
            
        user_id = resp.user_id
    except Exception as e:
        # Catch gRPC or connection errors
        raise HTTPException(status_code=500, detail=f"Identity service error: {str(e)}")
        
    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
