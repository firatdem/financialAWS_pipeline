from pydantic import BaseModel


class ParsedFields(BaseModel):
    invoice_number: str | None
    invoice_date: str | None
    total_amount: str | None
