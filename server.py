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

# Logger lib
from loguru import Logger


console = Console()
app = typer.Typer()


# Constants
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


class HTTPMETHODS(Enum):
    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    CONNECT = "CONNECT"


class HTTPSTATUS(Enum):
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


"""
Request Class
"""


class Request:
    def __init__(self, raw: bytes) -> None:
        pass


""""
Response Class
"""


class Response:
    def __init__(self, status: HTTPSTATUS, body: str) -> None:
        super().__init__()


"""
ConnectionHandler Class
"""


class ConnectionHandler(threading.Thread):
    def __init__(self, conn: socket.socket, addr) -> None:
        super().__init__()
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


class Server:
    def __init__(self, host: str, port: int) -> None:
        self.__host = host
        self.__port = port

    def __start_server(self) -> None:
        pass


@app.command()
def rabbit_start_server(host: str, port: Annotated[Optional[int], typer.Argument()] = 8080) -> None:
    """Command: rabbit_start_server

    Parameters:
        host: str - Hostname or IP address.
        port: int - Port number, defaults to 8080.

    Description:
        This command will start the server dependent on the host and port
        provided through the command line arguments.

    Returns:
        None
    """
    pass


@app.command()
def rabbit_stop_server() -> None:
    """Command: rabbit_stop_server

    Description:
        This command will stop any and all servers that are currently running,
        with their defined host and port numbers.

    Returns:
    None
    """
    pass


@app.command()
def rabbit_restart_server(host: str, port: Annotated[Optional[int], typer.Argument()] = 8080) -> None:
    """Command: rabbit_restart_server

    Parameters:
        host: str - Hostname or IP address.
        port: int - Port number, defaults to 8080.

    Description:
        This command will restart the server dependent on the host and port
        provided through the command line arguments.

    Returns:
        None
    """
    pass


@app.command()
def rabbit_status() -> None:
    """Command: rabbit_status

    Description:
        This command will display the status of the current server, including
        the number of active connections, the host and port number.

    Returns:
        None
    """
    pass


@app.command()
def rabbit_view_logs() -> None:
    """Command: rabbit_view_logs

    Description:
        This command will display all active log files that are currently being
        written to and updated by the server. During a connection, or request,
        the server will write to a log file, which can be viewed using this command.

        Alternatively, the log files can also be viewed by heading over to the
        `logs` directory in the root of the project.

    Returns:
        None
    """
    pass


@app.command()
def rabbit_show_blacklisted() -> list[str]:
    """Command: rabbit_show_blacklisted

    Description:
        This command will display all the blacklisted sites that are currently
        being blocked by the server. The server will block any incoming requests
        from the blacklisted sites, and will return a 403 Forbidden status code,
        given that the site is blacklisted and isn't manually whitelisted.

    Returns:
        list[str]
    """
    pass


@app.command()
def rabbit_show_whitelisted() -> list[str]:
    """Command: rabbit_show_whitelist

    Description:
        This command will display all the whitelisted sites that are currently
        allowed by the server instance. The server will allow any incoming requests
        from whitelisted sites, and will return a 200 OK status code, given that
        the site is whitelisted.

    Returns:
        list[str]
    """
    pass

@app.command()
def rabbit_blacklist(site: str) -> HTTPSTATUS.FORBIDDEN:
    """Command: rabbit_blacklist

    Parameters:
        site: str - The site that you want to blacklist.

    Description:
        This command will blacklist a site, and block any incoming requests from
        the site. The server will return a 403 Forbidden status code, given that
        the site is blacklisted and isn't manually whitelisted.

    Returns:
        HTTPSTATUS.FORBIDDEN
    """
    pass

@app.command()
def rabbit_whitelist(site: str) -> HTTPSTATUS.OK:
    """Command: rabbit_whitelist

    Parameters:
        site: str - The site that you want to whitelist.

    Description:
        This command will whitelist a site, and allow any incoming requests from
        the site. The server will return a 200 OK status code, given that the site
        is whitelisted.

    Returns:
        HTTPSTATUS.OK
    """
    pass


@app.command()
def rabbit_display_config() -> None:
    """Command: rabbit_config

    Description:
        This command will display the current configuration of the server, including
        but not limited to the host, port, blacklisted sites, whitelisted sites, and
        the number of active connections.

    Returns:
        None
    """
    pass


@app.command()
def rabbit_help() -> None:
    """Command: rabbit_help

    Description:
        This command will display all the available commands and their respective
        descriptions, including the parameters that they accept, this is useful for
        understanding the functionality of each command and how to use them.

    Returns:
        None
    """
    pass


if __name__ == '__main__':
    app()
