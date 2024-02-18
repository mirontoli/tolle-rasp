'''
https://www.raspberrypi.com/tutorials/host-a-hotel-wifi-hotspot/
Running on Raspberry Pi 3B+
With a built-in wifi (wlan0) and a wifi dongle (wlan1)

Enable NetworkManager in raspi-config

sudo apt update && sudo apt full-upgrade -y

sudo apt install python3-flask -y
cd
mkdir wifi-portal
cd wifi-portal
nano app.py

sudo crontab -e
@reboot sudo python3 /home/mirontoli/wifi-portal/app.py

'''

from flask import Flask,request
import subprocess

app = Flask(__name__)

wifi_device = "wlan0"

@app.route('/')
def index():
    result = subprocess.check_output(["nmcli", "--colors", "no", "-m", "multiline", "--get-value", "SSID", "dev", "wifi", "list", "ifname", wifi_device])
    ssids_list = result.decode().split('\n')
    dropdowndisplay = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Wifi Control</title>
        </head>
        <body>
            <h1>Wifi Control</h1>
            <form action="/submit" method="post">
                <label for="ssid">Choose a WiFi network:</label>
                <select name="ssid" id="ssid">
        """
    for ssid in ssids_list:
        only_ssid = ssid.removeprefix("SSID:")
        if len(only_ssid) > 0:
            dropdowndisplay += f"""
                    <option value="{only_ssid}">{only_ssid}</option>
            """
    dropdowndisplay += f"""
                </select>
                <p/>
                <label for="password">Password: <input type="password" name="password"/></label>
                <p/>
                <input type="submit" value="Connect">
            </form>
            <br>
            <a href="/shutdown">want to shut down</a>
        </body>
        </html>
        """
    return dropdowndisplay


@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':
        print(*list(request.form.keys()), sep = ", ")
        ssid = request.form['ssid']
        password = request.form['password']
        connection_command = ["nmcli", "--colors", "no", "device", "wifi", "connect", ssid, "ifname", wifi_device]
        if len(password) > 0:
          connection_command.append("password")
          connection_command.append(password)
        result = subprocess.run(connection_command, capture_output=True)
        if result.stderr:
            return "Error: failed to connect to wifi network: <i>%s</i>" % result.stderr.decode()
        elif result.stdout:
            return "Success: <i>%s</i>" % result.stdout.decode()
        return "Error: failed to connect."

# safe shutdown from the web browser
# todo add reboot
@app.route('/shutdown')
def shutdown_page():
    body = f'''
        <form action="/shutdown" method="post">
            <input type="submit" value="shutdown">
        </form>
    '''
    return body

@app.route('/shutdown',methods=['POST'])
def shutdown():
    subprocess.run(['shutdown', '-h', 'now'])
    return "shutting down"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)