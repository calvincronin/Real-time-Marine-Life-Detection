import requests
import time

def capture_image():
    serial_number = 'C3471350123961'  # Replace with your GoPro's serial number
    ip_address = f'172.2{serial_number[-3]}.1{serial_number[-2:]}.51'
    url = f'http://{ip_address}:8080/gopro/camera/shutter/start'

    response = requests.get(url)
    # if response.status_code == 200:
	#     pass
    #     #print("Image capture initiated.")
    # else:
    #     print("Failed to capture image.")
    #     print(response.text)

capture_image()
time.sleep(2)


        


