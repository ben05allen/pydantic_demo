import datetime

from pydantic import BaseModel, Field, validator





def wrangle_dates(value):
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d/%m/%y",
        "%d-%m-%Y",
        "%d-%b-%Y",
    ]

    for format in formats:
        try:
            return datetime.datetime.strptime(str(value).strip(), format)
        except ValueError:
            continue

    raise ValueError(f"Format of date {value} does not match any known pattern.")


def drop_units(value):
    if isinstance(value, str):
        return float(value.replace("kg", "").replace(",", "").strip())
    return value


class Sale(BaseModel):

    date: datetime.date
    customer_name: str
    size_kg: float = Field(alias="Size (kg)")
    amount: int
    unit_price: int
    total_sale: int | None = None

    
    class Config:
        
        @classmethod
        def alias_generator(cls, string: str) -> str:  # this needs to be called "alias_generator"
            return " ".join(word.capitalize() for word in string.split("_"))

    @validator('date', pre=True)
    def wrangle_dates(value):
        formats = [
            "%Y-%m-%d",
            "%d/%m/%Y",
            "%d/%m/%y",
            "%d-%m-%Y",
            "%d-%b-%Y",
        ]

        for format in formats:
            try:
                return datetime.datetime.strptime(str(value).strip(), format)
            except ValueError:
                continue

        raise ValueError(f"Format of date {value} does not match any known pattern.")

    @validator('size_kg', pre=True)
    def drop_units(value):
        if isinstance(value, str):
            return float(value.replace("kg", "").replace(",", "").strip())
        return value

    

    # validate_units = field_validator("size_kg", mode="before")(drop_units)

    # @model_validator(mode="after")
    # def calc_total(self):
    #     self.total_sale = self.amount * self.unit_price
