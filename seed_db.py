import os
from dotenv import load_dotenv;
from database import engine, User, Session
from sqlmodel import select

load dotenv();

def seed_admin():
    admin_email = os.getenv("ADMIN_EMAIL")
    admin_password = os.getenv("ADMIN_PASSWORD")

    with Session(engine) as session:
        statement = select(User).where(User.email == "admin_email")
        existing_admin = session.exec(statement).first()
        
        if not existing_admin:
            admin = User(
                email="admin_email",
                password="admin_password",
                name="System Admin",
                role="Admin"
            )
            session.add(admin)
            session.commit()
            print("✅ Admin user created: admin_email / admin_password")
        else:
            print("Admin user already exists.")

if __name__ == "__main__":
    seed_admin()
