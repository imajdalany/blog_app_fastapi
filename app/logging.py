from time import perf_counter
from functools import wraps
import logging, asyncio

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)


def timed(fn):
    """A decorator that logs function run time."""
    fn_name = fn.__name__

    if asyncio.iscoroutinefunction(fn):

        @wraps(fn)
        async def async_wrapper(*args, **kwargs):
            start = perf_counter()
            try:
                return await fn(*args, **kwargs)
            finally:
                duration = perf_counter() - start
                logging.info(f"[metric:{fn_name}.time] %.3f", duration)

        return async_wrapper
    else:

        @wraps(fn)
        def sync_wrapper(*args, **kwargs):
            start = perf_counter()
            try:
                return fn(*args, **kwargs)
            finally:
                duration = perf_counter() - start
                logging.info(f"[metric:{fn_name}.time] %.3f", duration)

        return sync_wrapper
