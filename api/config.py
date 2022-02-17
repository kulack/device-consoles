#
# Copyright 2022 Fred A. Kulack kulack@gmail.com
#
import os
from dataclasses import dataclass
from getpass import getpass

@dataclass()
class Config:
    url: str
    user: str
    password: str
    group: str  # Optional

    @staticmethod
    def from_environment():
        """
        Initialize the API configuration from environment variables, raising an exception
        if the required environment variables are not found.
        """
        url = os.environ["DRM_URL"] if "DRM_URL" in os.environ else "https://remotemanager.digi.com"
        group = os.environ["DRM_GROUP"] if "DRM_GROUP" in os.environ else ""

        if 'DRM_USER' in os.environ and os.environ['DRM_USER']:
            user = os.environ['DRM_USER']
        else:
            user = input(f"Username for {url}: ")

        if 'DRM_PASSWORD' in os.environ and os.environ['DRM_PASSWORD']:
            password = os.environ['DRM_PASSWORD']
        else:
            password = getpass(f"Password for user {user} at {url}:")
        return Config(url, user, password, group)
