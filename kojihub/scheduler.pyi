from _typeshed import Incomplete
from typing import Callable, Iterable, Optional, TypeAlias, TypedDict

from . import kojihub as kojihub
from .db import (
    DeleteProcessor,
    InsertProcessor,
    QueryProcessor,
    QueryView,
    UpdateProcessor,
    UpsertProcessor,
    db_lock,
)

logger: Incomplete

_Tables: TypeAlias = list[str]
_Clauses: TypeAlias = Iterable[str]
_JoinMap: TypeAlias = dict[str, str]
_FieldMap: TypeAlias = dict[str, list[str|None]]
_DefaultFields: TypeAlias = tuple[str]
_Fields: TypeAlias = Iterable[str]
_TaskRun: TypeAlias = dict

class _HostInfo(TypedDict):
    id: int
    user_id: int
    name: str
    update_ts: float
    ready: bool
    task_load: float
    arches: str
    capacity: float
    description: str
    comment: str
    enabled: bool

def log_db(msg, task_id: Optional[int] = None, host_id: Optional[int] = None) -> None:
    ...

def log_both(msg, task_id: Optional[int] = None, host_id: Optional[int] = None, level=...) -> None:
    ...

class LogMessagesQuery(QueryView):
    tables: _Tables
    joinmap: _JoinMap
    fieldmap: _FieldMap
    default_fields: _DefaultFields

def get_log_messages(
        clauses: Optional[_Clauses] = None,
        fields: Optional[Iterable[str]] = None):
    ...

def get_tasks_for_host(hostID: Optional[int], retry: bool = True):
    ...

def set_refusal(
        hostID: int,
        taskID: int,
        soft: bool = True,
        by_host: bool = False,
        msg: str = '') -> None:
    ...

class TaskRefusalsQuery(QueryView):
    tables: _Tables
    joinmap: _JoinMap
    fieldmap: _FieldMap
    default_fields: _DefaultFields

def get_task_refusals(
        clauses: Optional[_Clauses] = None,
        fields: Optional[_Fields] = None):
    ...

def get_host_data(hostID: Optional[int] = None): ...
def set_host_data(hostID: Optional[int], data: dict) -> None: ...

class TaskRunsQuery(QueryView):
    tables: _Tables
    joinmap: _JoinMap
    fieldmap: _FieldMap
    default_fields: _DefaultFields

def get_task_runs(
        clauses: Optional[_Clauses] = None,
        fields: Optional[_Fields] = None):
    ...

class TaskScheduler:
    hosts_by_bin: dict[str, list[_HostInfo]]
    hosts: dict[int, _HostInfo]
    active_tasks: list[dict]
    free_tasks: Iterable[dict]
    maxjobs: int
    capacity_overcommit: int
    ready_timeout: int
    assign_timeout: int
    soft_refusal_timeout: int
    host_timeout: int
    run_interval: int
    def __init__(self) -> None: ...
    def run(self, force: bool = False) -> bool: ...
    def check_ts(self) -> bool: ...
    def do_schedule(self) -> None: ...
    def check_active_tasks(self) -> None: ...
    def check_hosts(self) -> None: ...
    def get_active_runs(self) -> dict[int, list[_TaskRun]]: ...
    def get_tasks(self) -> None: ...
    def get_refusals(self) -> dict[int, dict]: ...
    def get_hosts(self) -> None: ...
    def assign(
            self,
            task = dict[str, int], # just task_id for now
            host = _HostInfo,
            force: bool = False,
            override: bool = False):
        ...

def do_assign(
    task_id: int,
    host: int,
    force: bool = False,
    override: bool = False):
    ...

class SchedulerExports:
    getTaskRuns: Callable
    getTaskRefusals: Callable
    getHostData: Callable
    getLogMessages: Callable
    def doRun(self, force: bool = False) -> bool: ...
