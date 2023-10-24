import errno
from pathlib import Path
import logging as log

import requests

ENCODING = "UTF-8"


def sanitize_ident(ident: str):
    """Naive ident sanitizer"""

    for illegal in r'/\|!?[]<>.,:;"*':
        ident = ident.replace(illegal, "_")

    return ident


def download(url: str, path: Path):
    """Downloads a file over http(s), returns (err, path)."""

    path = Path(path).resolve()
    if path.is_dir():
        path = path / url.split("/")[-1]
    if not (path.parent.is_dir() and path.parent.exists()):
        return errno.EINVAL, path

    with requests.get(url, stream=True) as request:
        request.raise_for_status()
        with path.open("wb") as local:
            for chunk in request.iter_content(chunk_size=8192):
                local.write(chunk)

    return 0, path


class CijoeLogFormatter(log.Formatter):
    """Logging colored formatter"""

    cyan = '\x1b[36m'
    green = '\x1b[32m'
    red = '\x1b[38;5;196m'
    white = '\x1b[37m'
    reset = '\x1b[0m'

    format_str = "%(levelname)s:%(module)s:%(funcName)s(): %(message)s"
    format_trace_str = "%(message)s"
    TRACE = log.INFO + 1

    def __init__(self):
        super().__init__()
        self.FORMATS = {
            log.DEBUG: self.cyan + self.format_str + self.reset,
            log.INFO: self.green + self.format_str + self.reset,
            log.ERROR: self.red + self.format_str + self.reset,
            self.TRACE: self.white + self.format_trace_str + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = log.Formatter(log_fmt)
        return formatter.format(record)
