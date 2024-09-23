from _typeshed import Incomplete
from typing import Any, Iterable, Optional, Callable, Tuple, Union, TypeAlias
import logging

from koji.context import ThreadLocal

context: Incomplete
POSITIONAL_RE: Any
NAMED_RE: Any
logger: Incomplete

'''
class _QueryOpts(TypedDict, total=False):
    countOnly: bool
    order: str
    offset: int
    limit: int
'''
_QueryOpts: TypeAlias = dict[str, Any]


class DBWrapper:
    cnx: Incomplete

    def __init__(self, cnx: ThreadLocal) -> None:
        ...

    def __getattr__(self, key: Any):
        ...

    def cursor(self, *args: Any, **kw: Any):
        ...

    def close(self) -> None:
        ...


class CursorWrapper:
    cursor: Incomplete
    logger: logging.Logger
    def __init__(self, cursor) -> None: ...
    def __getattr__(self, key: str) -> Any: ...
    def fetchone(self, *args, **kwargs): ...
    def fetchall(self, *args, **kwargs): ...
    def quote(self, operation: str, parameters: dict[str, Any]) -> str: ...
    def preformat(self, sql: str, params: dict[str, Any]): ...
    def execute(self, operation: str, parameters=list, log_errors: bool = ...): ...


def provideDBopts(**opts: Any) -> None: ...
def setDBopts(**opts: Any) -> None: ...
def getDBopts() -> dict[str, Any]: ...
def connect() -> DBWrapper: ...


class QueryProcessor:
    iterchunksize: int
    columns: Optional[list[str]]
    aliases: Optional[list[str]]
    colsByAlias: dict[str, str]
    tables: Optional[list[str]]
    joins: Optional[list[str]]
    clauses: Optional[list[str]]
    cursors: int
    values: dict[str, Any]
    transform: Callable
    opts: _QueryOpts
    enable_group: bool
    logger: logging.Logger

    def __init__(self,
                 columns: Optional[Iterable[str]] = ...,
                 aliases: Optional[Iterable[str]] = ...,
                 tables: Optional[Iterable[str]] = ...,
                 joins: Optional[Iterable[str]] = ...,
                 clauses: Optional[Iterable[str]] = ...,
                 values: Optional[dict[str, Any]] = ...,
                 transform: Optional[Callable] = ...,
                 opts: Optional[_QueryOpts] = ...,
                 enable_group: bool = ...) -> None:
        ...

    def countOnly(self, count: int) -> None: ...
    def singleValue(self, strict: bool = ...): ...
    def execute(self) -> list[dict[str, Any]]: ...
    #def execute(self) -> None: ...
    def iterate(self) -> Iterable[dict[str, Any]]: ...
    def executeOne(self, strict: bool = ...) -> Optional[dict[str, Any]]: ...


class QueryView:
    tables = list[str]
    joins = list[str]
    joinmap = dict[str, str]
    fieldmap = dict[str, str]
    default_fields: Iterable[str]
    clauses: Optional[list]
    fields: Optional[Iterable[str]]
    opts: _QueryOpts
    extra_joins: list
    values: dict
    order_map: dict[str, str]

    def __init__(self,
                 clauses: Optional[Iterable] = None,
                 fields: Optional[Iterable[str]] = None,
                 opts: Optional[_QueryOpts] = None) -> None:
        ...

    @property
    def query(self): ...


    def get_query(self): ...
    def get_fields(self, fields): ...
    def check_opts(self) -> None: ...
    def map_field(self, field): ...
    def get_clauses(self): ...
    def get_joins(self): ...
    def execute(self): ...
    def executeOne(self, strict: bool = False): ...
    def iterate(self): ...
    def singleValue(self, strict: bool = True): ...

def convert_timestamp(float) -> str: ...
def get_event() -> int: ...
def nextval(sequence: str) -> int: ...
def currval(sequence: str) -> int: ...
def db_lock(name: str, wait: bool = ...) -> bool: ...

class Savepoint:
    name: str
    def __init__(self, name: str) -> None: ...
    def rollback(self) -> None: ...

class InsertProcessor:
    table: str
    data: dict[str, Any]
    rawdata: dict[str, Any]

    def __init__(self,
                 table: str,
                 data: Optional[dict[str, Any]] = ...,
                 rawdata: Optional[dict[str, Any]] = ...) -> None:
        ...

    def set(self, **kwargs: Any) -> None: ...
    def rawset(self, **kwargs: Any) -> None: ...
    def make_create(self,
                    event_id: Optional[int] = ...,
                    user_id: Optional[int] = ...) -> None:
        ...

    def dup_check(self) -> bool: ...
    def execute(self) -> int: ...


class UpdateProcessor:
    table: str
    data: dict[str, Any]
    rawdata: dict[str, Any]
    clauses: list[str]
    values: dict[str, Any]
    def __init__(self,
                 table: str,
                 data: Optional[dict[str, Any]] = ...,
                 rawdata: Optional[dict[str, Any]] = ...,
                 clauses: Optional[Iterable[str]] = ...,
                 values: Optional[dict[str, Any]] = ...) -> None:
        ...

    def get_values(self) -> dict[str, Any]: ...
    def set(self, **kwargs: Any) -> None: ...
    def rawset(self, **kwargs: Any) -> None: ...
    def make_revoke(self,
                    event_id: Optional[int] = ...,
                    user_id: Optional[int] = ...) -> None:
        ...

    def execute(self) -> int: ...


class DeleteProcessor:
    table: str
    clauses: list[str]
    values: dict[str, Any]
    def __init__(self,
                 table: str,
                 clauses: Optional[Iterable[str]] = ...,
                 values: Optional[dict[str, Any]] = ...) -> None:
        ...

    def get_values(self) -> dict[str, Any]: ...
    def execute(self) -> int: ...


class BulkInsertProcessor:
    table: str
    data: dict[str, Any]
    columns: list[str]
    strict: bool
    batch: int
    def __init__(
        self,
        table: str,
        data: Optional[list[dict[str, Any]]] = ...,
        columns: Optional[list[str]] = ...,
        strict: bool = ...,
        batch: int = ...) -> None:
        ...

    def __str__(self) -> str: ...
    def _get_insert(self, data: list[dict[str, Any]]) -> Tuple[str, dict[str, Any]]: ...
    def __repr__(self) -> str: ...
    def add_record(self, **kwargs: Any) -> None: ...
    def execute(self) -> None: ...
    def _one_insert(self, data: dict[str, Any]) -> None: ...

class UpsertProcessor(InsertProcessor):
    keys: Optional[Iterable[str]]
    skip_dup: bool

    def __init__(
            self,
            table,
            data: Optional[dict[str, Any]] = None,
            rawdata: Optional[dict] = None,
            keys: Optional[Iterable[str]]  = None,
            skip_dup: bool = False) -> None:
        ...

def _applyQueryOpts(
        results: list[dict[str, Any]],
        queryOpts: _QueryOpts) -> Union[int, list[dict]]:
    ...

def _dml(
    operation: str,
    values: dict[str, Any],
    log_errors: bool = True):
    ...


def _fetchMulti(
    query: str,
    values: dict[str, Any]):
    ...

def _fetchSingle(
        query: str,
        values: dict[str, Any],
        strict: bool = False):
    ...

def _singleValue(
        query: str,
        values: Optional[dict[str, Any]] = None,
        strict: bool =True):
    ...

def _multiRow(
        query: str,
        values: dict[str, Any],
        fields: Iterable[str]):
    ...

def _singleRow(
        query: str,
        values: dict[str, Any],
        fields: Iterable[str],
        strict: bool = False):
    ...
