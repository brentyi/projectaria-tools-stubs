from enum import Enum
from typing import List, Optional

from _typeshed import Incomplete

CHUCK_SIZE_BYTE: int
STATUS_CODE_DEFAULT: int
DOWNLOAD_STATUS_FILE: str

class AriaDigitalTwinDataGroup(Enum):
    BENCHMARK: int
    CHALLENGE: int

class AriaDigitalTwinDataType(Enum):
    MAIN_DATA: int
    SEGMENTATIONS: int
    DEPTH_IMAGES: int
    SYNTHETIC: int

def calculate_file_sha1(file_path: str) -> str: ...

class AriaDigitalTwinDownloadStatusManager:
    status: Incomplete
    def __init__(self) -> None: ...
    def from_json(self, json_path: str): ...
    def to_json(self, json_path: str): ...
    def set_download_status(self, data_type: AriaDigitalTwinDataType, value: bool): ...
    def get_download_status(self, data_type: AriaDigitalTwinDataType) -> bool: ...

class AriaDigitalTwinDatasetDownloader:
    metadata: Incomplete
    data_group: Incomplete
    data_category: Incomplete
    data_types: Incomplete
    sequences: Incomplete
    overwrite: Incomplete
    def __init__(
        self,
        cdn_file: str,
        data_group: AriaDigitalTwinDataGroup,
        data_category: str,
        data_types: List[AriaDigitalTwinDataType],
        sequences: Optional[List[str]] = ...,
        overwrite: bool = ...,
    ) -> None: ...
    def download_data(self, output_folder: str): ...
