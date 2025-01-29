import requests

def enable_usb_control(state):
    serial_number = 'C3471350123961'  # Replace with your GoPro's serial number
    ip_address = f'172.2{serial_number[-3]}.1{serial_number[-2:]}.51'
    url = f'http://{ip_address}:8080/gopro/camera/control/wired_usb?p=' + str(state)

    response = requests.get(url)
    # if response.status_code == 200:
	#     pass
    #     #print("USB control enabled successfully.")
    # else:
    #     print("Failed to enable USB control.")
    #     print(response.text)

enable_usb_control(1)