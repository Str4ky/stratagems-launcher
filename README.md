# Stratagems Launcher
A way to use Helldivers 2's Stratagems remotely<br><br>
<img src="https://i.imgur.com/tpuMrtY.png" width="250">

## Installation

- Head over to the <a href="/releases">releases</a> and download the zip
- Unzip it and go the extracted folder
- Open `launcher.exe`
- Go to `<local_ip_address>:<web_port>` on your other device's web browser

## Configuration
- Go to `assets/json` and open `config.json`<br><br>
It will look like this
```json
{
    "url": "http://192.168.1.15",
    "server_port": 5000,
    "web_port": 5500,
    "keys": {
        "up": "up",
        "down": "down",
        "left": "left",
        "right": "right",
        "open": "alt"
    }
}
```
- Edit the url with your computer's local ip address
- Edit the ports if you really want to but I suggest you to leave that alone
- Edit the keys with your ingame keybinds to open and uses stratagems
- Change your inggame open stratagems list keybing from `hold` to `press`

## Runinng locally without the releases

- Download the zip file of the repo under the `Code` button
- Unzip it and do the config as explained above
- Run `pip install -r requirements.txt` in a cmd prompt
- Run `py script.py` in the same cmd prompt
- Go to `<local_ip_address>:<web_port>` on your other device's web browser
