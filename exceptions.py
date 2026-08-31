from fastapi import HTTPException


def expense_not_found():

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )