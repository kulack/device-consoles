#
# Copyright 2022 Fred A. Kulack kulack@gmail.com
#
# Use the non-slim version for shell and some utilities for a bit
FROM python:3.9-bullseye
# FROM python:3.9-slim-bullseye

WORKDIR /opt/code

# Python setup
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code over
COPY *.py /opt/code/
COPY api /opt/code/api/
RUN chmod a+x deviceConsole.py

ENV DRM_URL=https://remotemanager.digi.com
ENV DRM_USER=""
ENV DRM_PASSWORD=""
ENV DRM_GROUP=""

CMD ["/opt/code/deviceConsole.py"]
