# Hint: You'll need imports from FastAPI, SQLAlchemy, and your project files.



# ❗ TODO: Create your Fastapi app here



# ❗ TODO: Create all tables using SQLAlchemy (bind metadata to engine)


# ❗ TODO: Rewrite the welcome endpoint and set path to root
"""@app.get()
def welcome() -> str:
    # ✅ Return a welcome message
    return "welcome"
"""



# ❗ TODO : Compelete the user registration endpoint with correct HTTP method
"""@app ✅ Add appropriate response model (e.g., User from schemas)
def user_register(
    user_credentials,  # ✅ Add appropriate schema (e.g., BaseUser)
    db  # ✅ Inject a Session using Depends
):
    
    Registers a new user.
    - Checks if the email is already used.
    - If not, creates and returns the new user information
    
    # ✅ Query DB to find existing user by email
    # ❗ If user exists, raise HTTPException(409)
    # ✅ Else, add and commit new user

"""



# ❗ TODO : wrtie a endpoint to query users from database
"""
@app(   ✅ Add appropriate response model (e.g., User). Import List from typing and set response model to List[User]
def get_users(
    sort_by_created_at,  # ✅ Add Optional[bool] with Query
    limit,               # ✅ Add Optional[int] with Query
    db                   # ✅ Inject session
):
    
    Get list of users.
    - Optionally sorted by created_at (ascending if True)
    - Limit results if limit is provided else should return all users
    
    # ✅ Use .order_by() with asc/desc
    # ✅ Use .limit() if provided

    # - Add optional email filter: search_email: Optional[str] = Query(None)

    pass
"""