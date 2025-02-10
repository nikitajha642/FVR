from base import BaseClass


class AmountClass(BaseClass):
    amount = BaseClass(
        field_type = "number"
        label="amount"
        name=""
        required = False
        value = 10000000
        subtype = ""
        access=True
        className = "AmountClass"
    )
   