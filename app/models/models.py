from sqlalchemy import Column, Integer, String, VARCHAR, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Tables should inherit from Base
class User():
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username =Column(VARCHAR(40), nullable=False, unique=True)
#    ✅ Create email column to store users emails, emails must be unique
#    ✅ Create passwrod column to store passwords, this column should not be nullable
#    ✅ Add created_at Column and set server_default value to to get current time from func.now()
#    ✅ Add updated_at Column and set server_default value to to get current time from func.now()
