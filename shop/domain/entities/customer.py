from dataclasses import dataclass

@dataclass
class Customer:
    id: str
    user_id: int
    first_name: str
    last_name: str
    