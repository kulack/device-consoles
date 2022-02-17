#!/usr/bin/env python3
import json
import argparse
from api.config import Config
from api import drm


def main():
    config = Config.from_environment()
    session = drm.login(config)

    # We're not going to show any more than this many links
    limit = 500
    count = 0
    skipped = 0

    devices = drm.get_devices(session, config)
    devices = sorted(devices, key=lambda d: d['group'])

    print("<html>\n<title>Remote Manager Device Consoles</title>\n<body >\n<table>")
    print("<tr><th>Group</th><th>Name</th><th>ID/Console Link</th></tr>")
    for dev in devices:
        # Not all devices support a streaming console access to their local OS
        # or to backend managed devices
        if 'capabilities' in dev and 'cli_service_available' in dev['capabilities'] and dev['capabilities']['cli_service_available']:
            pass  # supported
        else:
            skipped += 1
            continue

        device_id = dev['id']
        name = f"{dev['name']}" if 'name' in dev else ''
        group = f"/{dev['group']}" if 'group' in dev and dev['group'] else '/'

        print(f'<tr>'
              f'<td >{group}</td>'
              f'<td style="text-align:center">{name}</td>'
              f'<td style="text-align:center"><tt><a href="https://remotemanager.digi.com/ui/console/{device_id}">{device_id}</a></tt></td>'
              f'</tr>')
        count += 1
        if limit and count >= limit:
            print(f"<p>Limit of {limit} reached</p>")
            break
    print("</table>\n")
    if skipped > 0:
        print(f"<p>Skipped {skipped} devices that do not support a streaming console service</p>")
    print("<body>\n</html>")


if __name__ == "__main__":
    main()
