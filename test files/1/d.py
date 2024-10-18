import requests
import json

def send_screenshot(webhook_url, screenshot_file):
    data = {
        'content': 'Screenshot',
        'file': open(screenshot_file, 'rb')
    }

    response = requests.post(webhook_url, files=data)

    if response.status_code == 200:
        print('Screenshot sent successfully!')
    else:
        print('Error sending screenshot: {}'.format(response.status_code))

if __name__ == '__main__':
    webhook_url = ''
    screenshot_file = 'a.png'

    send_screenshot(webhook_url, screenshot_file)
