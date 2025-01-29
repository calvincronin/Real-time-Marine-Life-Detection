import requests

def get_last_image():
    serial_number = 'C3471350123961'  # Replace with your GoPro's serial number
    ip_address = f'172.2{serial_number[-3]}.1{serial_number[-2:]}.51'
    url = f'http://{ip_address}:8080/gopro/media/list'

    response = requests.get(url)
    if response.status_code == 200:
        media_list = response.json()
        if media_list and 'media' in media_list:
            last_media = media_list['media'][0]['fs'][-1]['n']
            download_url = f'http://{ip_address}:8080/videos/DCIM/100GOPRO/{last_media}'
            image_data = requests.get(download_url).content
            with open("latest_image.jpg", "wb") as f:
                f.write(image_data)
    #         #print("Image downloaded as latest_image.jpg")
    #     else:
    #         print("No media found.")
    # else:
    #     print("Failed to retrieve media list.")
    #     print(response.text)

get_last_image()