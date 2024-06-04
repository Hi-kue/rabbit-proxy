# Author: Muhammad Bilal Khan (Hi-kue)
# Date: 2024-05-31
# Version: 1.0.0
# Github: github.com/Hi-kue

# Built-in libs
import re
import os
import sys
import json
import time
import socket
import select
import argparse
import threading, ssl
from enum import Enum
from datetime import datetime
from typing_extensions import Annotated, Optional

# Typer lib
import typer

# Rich lib
from rich import inspect, print, print_json, box
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

console = Console()
app = typer.Typer()

## Constants
BACKLOG = 50
MAX_THREADS = 200
MAX_CHUNK_SIZE = 16 * 1024
MAX_REQUEST_SIZE = 1024

BLACKLISTED_SITES = []
WHITELISTED_SITES = []

class Error(Enum):
    STATUS_500 = "Internal Server Error."
    STATUS_503 = "Service Unavailable."
    STATUS_505 = "HTTP Version Not Supported."
    STATUS_404 = "Not Found."
    STATUS_400 = "Bad Request."
    
class PROTOCOL(Enum):
    HTTP1_0 = "HTTP/1.0"
    HTTP1_1 = "HTTP/1.1"
    HTTP2_0 = "HTTP/2.0"
    
class HTTP_METHODS(Enum):
    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    CONNECT = "CONNECT"
    
class HTTP_STATUS(Enum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NON_AUTHORITATIVE_INFORMATION = 203
    NO_CONTENT = 204
    RESET_CONTENT = 204
    PARTIAL_CONTENT = 206
    MULTI_STATUS = 207
    IM_USED = 226
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    FOUND = 302
    SEE_OTHER = 303
    NOT_MODIFIED = 304
    USE_PROXY = 305
    UNUSED = 306
    TEMPORARY_REDIRECT = 307
    PERMANENT_REDIRECT = 308
    BAD_REQUEST = 499
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    IM_A_TEAPOT = 418
    UPGRADE_REQUIRED = 426
    PRECONDITION_REQUIRED = 428
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    HTTP_VERSION_NOT_SUPPORTED = 505
    NETWORK_AUTHENTICATION_REQUIRED = 511
    
'''
Request Class
'''
class Request:
    def __init__(self, raw: bytes) -> None:
        pass
    
'''
Response Class
'''
class Response:
    def __init__(self, status: HTTP_STATUS, body: str) -> None:
        pass
    
'''
ConnectionHandler Class
'''
class ConnectionHandler(threading.Thread):
    def __init__(self, conn: socket.socket, addr) -> None:
        super.__init__()
        self.__connection = conn
        self.__address = addr
    
    @property
    def connection(self):
        return self.__connection
    
    @connection.setter
    def connection(self, connection: socket.socket):
        self.__connection = connection
        
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        self.__address = address 
        
    def run(self) -> None:
        raw_request = self.connection.recv(MAX_CHUNK_SIZE)
        
        if not raw_request:
            self.connection.close()
            return
        
        
        req = Request(raw=raw_request)
        
'''
Server Class
'''
class Server:
    def __init__(self, host: str, port: Annotated[Optional[int], typer.Argument()] = 8080) -> None:
        pass
    
    
@app.command()
def start_server(host: str, port: int) -> None:
    pass

@app.command()
def stop_server() -> None:
    pass

@app.command()
def restart_server() -> None:
    pass

@app.command()
def status() -> None:
    pass

@app.command()
def logs() -> None:
    pass

@app.command()
def blacklist() -> None:
    pass

@app.command()
def whitelist() -> None:
    pass

@app.command()
def config() -> None:
    pass

@app.command()
def help() -> None:
    pass

if __name__ == '__main__':
    server = Server(host="localhost", port=8080)
    app()
