from typing import Optional, List

from pydantic.main import BaseModel


class Instrument(BaseModel):
    name: str
    full_name: str
    port_name: str
    description: str
    controls_prefix: Optional[str]
    endstations: List[str] = []
