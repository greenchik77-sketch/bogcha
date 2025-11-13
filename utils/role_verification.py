from fastapi import HTTPException


def admin_verification(user_data):
    if user_data.role != "admin":
        raise HTTPException(status_code=400, detail="Admin role required")