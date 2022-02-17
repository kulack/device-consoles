#
# Copyright 2022 Fred A. Kulack kulack@gmail.com
#
import json
import sys
import logging
from typing import Dict
import requests
from api.config import Config

log = logging.getLogger(__name__)


def login(config: Config) -> requests.Session:
    """
    Retrieve a logged in session given the host field in the arguments.
    Note that only on the first actual
    """
    session = requests.Session()
    session.auth = (config.user, config.password)
    rsp = session.get(f"{config.url}/ws/CheckStatus/.json")
    rsp.raise_for_status()
    return session


def get_devices(session: requests.Session, config: Config) -> [Dict]:
    """
    Return the list of device resource objects
    See the common arguments in the arguments module.
    """
    page = 1
    cursor = None
    items = []
    while True:
        page = get_devices_page(session, config, cursor=cursor)
        if "error_status" in page:
            log.error(f"Failed to retrieve devices: {page['error_message']}")
            sys.exit(1)

        for item in page["list"]:
            if log.isEnabledFor(logging.DEBUG):
                log.debug(json.dumps(item, sort_keys=True, indent=2, separators=(',', ': ')))
            items.append(item)

        if "cursor" not in page:
            # We've reached the end and must not continue
            return items
        # Otherwise, either more pages to read or we're polling
        cursor = page["cursor"]
        page += 1


def get_devices_page(session: requests.Session, config: Config, cursor: str = None):
    """
    Retrieve a devices v1 history page.
    See the common arguments in the arguments module.
    """
    sep = "?"
    url = f"{config.url}/ws/v1/devices/inventory"
    if config.group:
        url += f"{sep}query=group='{config.group}'"
        sep = "&"
    if cursor:
        url += f"{sep}cursor={cursor}"
        sep = "&"

    log.debug(f"Fetching devices page history url = {config.url}")

    rsp = session.get(url)
    rsp.raise_for_status()
    return json.loads(rsp.content)
