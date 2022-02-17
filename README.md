# Device Consoles
Generate Digi Remote Manager device console web pages

Source Repository: https://github.com/kulack/device-consoles

Generate a simple digest/table of contents web page linking to the device consoles in your <a href="https://remotemanager.digi.com">Digi Remote Manager</a> account.

Use the following environment variables to configure the container.

## Configuration

* DRM_USER: A user in the default account. If not specified, the app prompts for the username
* DRM_PASSWORD: The password for the user. If not specified, the app prompts for the password
* DRM_URL: The target Remote Manager cluster. Defaults to https://remotemanager.digi.com/
* DRM_GROUP: Default to generate links for all devices in the account. Specify 'Stores/Midwest' for example to only show device consoles for those devices in the "Stores/Midwest" group.

## Example Run
```
➜ docker run -it -e DRM_USER=user -e DRM_PASSWORD='xxxx' fkulack/device-consoles:1.0.0
<html>
<title>Remote Manager Device Consoles</title>
<body >
<table>
<tr><th>Group</th><th>Name</th><th>ID/Console Link</th></tr>
<tr><td >/</td><td style="text-align:center"></td><td style="text-align:center"><tt><a href="https://remotemanager.digi.com/ui/console/0008CAFE-FBB11BEF-26E805FF-FFE4412E">0008CAFE-FBB11BEF-26E805FF-FFE4412E</a></tt></td></tr>
<tr><td >/Stores</td><td style="text-align:center">Deadpool</td><td style="text-align:center"><tt><a href="https://remotemanager.digi.com/ui/console/00000000-00000000-0040FFFF-FF8001B0">00000000-00000000-0040FFFF-FF8001B0</a></tt></td></tr>
<tr><td >/Stores</td><td style="text-align:center">VirtualDAL</td><td style="text-align:center"><tt><a href="https://remotemanager.digi.com/ui/console/00000000-00000000-002704FF-FF4D936A">00000000-00000000-002704FF-FF4D936A</a></tt></td></tr>
</table>

<p>Skipped 10 devices that do not support a streaming console service</p>
<body>
</html>
</pre>
```

The file generated above looks like this:
<table>
<tr><th>Group</th><th>Name</th><th>ID/Console Link</th></tr>
<tr><td >/</td><td style="text-align:center"></td><td style="text-align:center"><tt><a href="https://remotemanager.digi.com/ui/console/0008CAFE-FBB11BEF-26E805FF-FFE4412E">0008CAFE-FBB11BEF-26E805FF-FFE4412E</a></tt></td></tr>
<tr><td >/Stores</td><td style="text-align:center">Deadpool</td><td style="text-align:center"><tt><a href="https://remotemanager.digi.com/ui/console/00000000-00000000-0040FFFF-FF8001B0">00000000-00000000-0040FFFF-FF8001B0</a></tt></td></tr>
<tr><td >/Stores</td><td style="text-align:center">VirtualDAL</td><td style="text-align:center"><tt><a href="https://remotemanager.digi.com/ui/console/00000000-00000000-002704FF-FF4D936A">00000000-00000000-002704FF-FF4D936A</a></tt></td></tr>
</table>
<p>Skipped 10 devices that do not support a streaming console service</p>


# Notes and todo:

* Add a CSTID parameter so that you can target devices in a subaccount
  generating the page for your reseller.

* Keep the container running
  * Serve the page live with a small web server 
  * Cache the page
  * Cron job to refresh the page every intermittently 

