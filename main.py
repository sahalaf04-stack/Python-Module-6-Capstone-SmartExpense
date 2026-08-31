from fastapi import (
    FastAPI,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session
from sqlalchemy import func

from database import (
    engine,
    Base,
    get_db
)

from models import Expense

from schemas import (
    ExpenseCreate,
    ExpenseResponse
)

from auth import verify_api_key

from logger import logger


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="SmartExpense API",
    description="Portfolio-ready Expense Tracker API",
    version="1.0.0"
)


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Welcome to SmartExpense",
        "docs": "/docs"
    }


# ============================================================
# CREATE EXPENSE
# ============================================================

@app.post(
    "/expenses",
    response_model=ExpenseResponse,
    dependencies=[Depends(verify_api_key)]
)
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db)
):

    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        description=expense.description
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    logger.info(
        f"Expense created: {new_expense.title}"
    )

    return new_expense


# ============================================================
# GET ALL EXPENSES
# ============================================================

@app.get(
    "/expenses",
    response_model=list[ExpenseResponse]
)
def get_expenses(
    db: Session = Depends(get_db)
):

    return db.query(
        Expense
    ).order_by(
        Expense.id.desc()
    ).all()


# ============================================================
# GET SINGLE EXPENSE
# ============================================================

@app.get(
    "/expenses/{expense_id}",
    response_model=ExpenseResponse
)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = db.query(
        Expense
    ).filter(
        Expense.id == expense_id
    ).first()

    if not expense:

        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return expense


# ============================================================
# UPDATE EXPENSE
# ============================================================

@app.put(
    "/expenses/{expense_id}",
    response_model=ExpenseResponse,
    dependencies=[Depends(verify_api_key)]
)
def update_expense(
    expense_id: int,
    data: ExpenseCreate,
    db: Session = Depends(get_db)
):

    expense = db.query(
        Expense
    ).filter(
        Expense.id == expense_id
    ).first()

    if not expense:

        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    expense.title = data.title
    expense.amount = data.amount
    expense.category = data.category
    expense.description = data.description

    db.commit()
    db.refresh(expense)

    logger.info(
        f"Expense updated: {expense_id}"
    )

    return expense


# ============================================================
# DELETE EXPENSE
# ============================================================

@app.delete(
    "/expenses/{expense_id}",
    dependencies=[Depends(verify_api_key)]
)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = db.query(
        Expense
    ).filter(
        Expense.id == expense_id
    ).first()

    if not expense:

        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    db.delete(expense)
    db.commit()

    logger.info(
        f"Expense deleted: {expense_id}"
    )

    return {
        "message": "Expense deleted successfully"
    }


# ============================================================
# EXPENSE SUMMARY
# ============================================================

@app.get("/summary")
def expense_summary(
    db: Session = Depends(get_db)
):

    total = db.query(
        func.sum(Expense.amount)
    ).scalar() or 0

    count = db.query(
        func.count(Expense.id)
    ).scalar() or 0

    categories = db.query(
        Expense.category,
        func.sum(Expense.amount)
    ).group_by(
        Expense.category
    ).all()

    category_summary = {
        category: amount
        for category, amount in categories
    }

    return {
        "total_expenses": count,
        "total_amount": round(total, 2),
        "category_summary": category_summary
    }