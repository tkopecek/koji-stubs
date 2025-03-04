import logging
from koji.xmlrpcplus import ExtendedMarshaller
from typing import Any, Optional

class Marshaller(ExtendedMarshaller):
    dispatch: Any = ...
    def dump_datetime(self, value: Any, write: Any) -> None: ...

class HandlerRegistry:
    funcs: Any = ...
    argspec_cache: Any = ...
    def __init__(self) -> None: ...
    def register_function(self, function: Any, name: Optional[Any] = ...) -> None: ...
    def register_module(self, instance: Any, prefix: Optional[Any] = ...) -> None: ...
    def register_instance(self, instance: Any) -> None: ...
    def register_plugin(self, plugin: Any) -> None: ...
    def getargspec(self, func: Any): ...
    def list_api(self): ...
    def system_listMethods(self): ...
    def system_methodSignature(self, method: Any): ...
    def system_methodHelp(self, method: Any): ...
    def get(self, name: Any): ...

class HandlerAccess:
    def __init__(self, registry: Any) -> None: ...
    def call(self, __name: Any, *args: Any, **kwargs: Any): ...
    def get(self, name: Any): ...

class ModXMLRPCRequestHandler:
    traceback: bool = ...
    handlers: Any = ...
    logger: Any = ...
    def __init__(self, handlers: Any) -> None: ...
    def handle_upload(self, environ: Any): ...
    def handle_rpc(self, environ: Any): ...
    def check_session(self) -> None: ...
    def enforce_lockout(self) -> None: ...
    def multiCall(self, calls: Any): ...
    def handle_request(self, req: Any) -> None: ...

def offline_reply(start_response: Any, msg: Optional[Any] = ...): ...
def load_config(environ: Any): ...
def load_plugins(opts: Any): ...
def get_policy(opts: Any, plugins: Any): ...

class HubFormatter(logging.Formatter):
    def format(self, record: Any): ...

def setup_logging1() -> None: ...
def setup_logging2(opts: Any) -> None: ...
def load_scripts(environ: Any) -> None: ...
def get_memory_usage(): ...
def server_setup(environ: Any) -> None: ...

firstcall: bool
firstcall_lock: Any

def application(environ: Any, start_response: Any): ...
def get_registry(opts: Any, plugins: Any): ...
