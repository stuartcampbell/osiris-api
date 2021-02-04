from typing import Optional

from pydantic.main import BaseModel


class Instrument(BaseModel):
    name: str
    full_name: str
    controls_prefix: Optional[str]
    # source: str
