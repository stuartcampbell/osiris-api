from typing import Optional

from pydantic.main import BaseModel

from models.instrument import Instrument

class EndStation(BaseModel):
    name: str
    controls_prefix: Optional[str]
    instrument: Optional[Instrument]
