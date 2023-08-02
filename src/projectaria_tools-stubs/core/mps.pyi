from typing import ClassVar, List, Optional

import _core_pybinds.calibration
import _core_pybinds.sophus
import datetime
import numpy

class ClosedLoopTrajectoryPose:
    angular_velocity_device: numpy.ndarray[numpy.float64[3,1]]
    device_linear_velocity_device: numpy.ndarray[numpy.float64[3,1]]
    graph_uid: str
    gravity_world: numpy.ndarray[numpy.float64[3,1]]
    quality_score: float
    tracking_timestamp: datetime.timedelta
    transform_world_device: _core_pybinds.sophus.SE3d
    utc_timestamp: datetime.timedelta
    def __init__(self, *args, **kwargs) -> None: ...

class EyeGaze:
    depth: float
    pitch: float
    pitch_high: float
    pitch_low: float
    tracking_timestamp: datetime.timedelta
    yaw: float
    yaw_high: float
    yaw_low: float
    def __init__(self, *args, **kwargs) -> None: ...

class GlobalPointPosition:
    distance_std: float
    graph_uid: str
    inverse_distance_std: float
    position_world: numpy.ndarray[numpy.float64[3,1]]
    uid: int
    def __init__(self, *args, **kwargs) -> None: ...

class OnlineCalibration:
    camera_calibs: List[_core_pybinds.calibration.CameraCalibration]
    imu_calibs: List[_core_pybinds.calibration.ImuCalibration]
    tracking_timestamp: datetime.timedelta
    utc_timestamp: datetime.timedelta
    def __init__(self, *args, **kwargs) -> None: ...

class OpenLoopTrajectoryPose:
    angular_velocity_device: numpy.ndarray[numpy.float64[3,1]]
    device_linear_velocity_odometry: numpy.ndarray[numpy.float64[3,1]]
    gravity_odometry: numpy.ndarray[numpy.float64[3,1]]
    quality_score: float
    session_uid: str
    tracking_timestamp: datetime.timedelta
    transform_odometry_device: _core_pybinds.sophus.SE3d
    utc_timestamp: datetime.timedelta
    def __init__(self, *args, **kwargs) -> None: ...

class PointObservation:
    camera_serial: str
    frame_capture_timestamp: datetime.timedelta
    point_uid: int
    uv: numpy.ndarray[numpy.float32[2,1]]
    def __init__(self, *args, **kwargs) -> None: ...

class StaticCameraCalibration:
    camera_uid: str
    end_frame_idx: Optional[int]
    graph_uid: str
    height: int
    intrinsics: numpy.ndarray[numpy.float32[8,1]]
    intrinsics_type: str
    start_frame_idx: Optional[int]
    transform_world_cam: _core_pybinds.sophus.SE3d
    width: int
    def __init__(self, *args, **kwargs) -> None: ...

class StreamCompressionMode:
    __members__: ClassVar[dict] = ...  # read-only
    GZIP: ClassVar[StreamCompressionMode] = ...
    NONE: ClassVar[StreamCompressionMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def get_eyegaze_point_at_depth(yaw_rads: float, pitch_rads: float, depth_m: float) -> numpy.ndarray[numpy.float64[3,1]]: ...
def read_closed_loop_trajectory(path: str) -> List[ClosedLoopTrajectoryPose]: ...
def read_eyegaze(path: str) -> List[EyeGaze]: ...
def read_global_point_cloud(path: str, compression: StreamCompressionMode) -> List[GlobalPointPosition]: ...
def read_online_calibration(path: str) -> List[OnlineCalibration]: ...
def read_open_loop_trajectory(path: str) -> List[OpenLoopTrajectoryPose]: ...
def read_point_observations(path: str, compression: StreamCompressionMode) -> List[PointObservation]: ...
def read_static_camera_calibrations(path: str) -> List[StaticCameraCalibration]: ...
