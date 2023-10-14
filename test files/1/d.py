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
    webhook_url = 'https://discord.com/api/webhooks/1134892597668753448/RaoYzDR_O6P07whGZ_GiSJnT2j4p3HRgHisSaJ31TeAo5VHCstYOTBFymq6Nher1jlUI'
    screenshot_file = 'a.png'

    send_screenshot(webhook_url, screenshot_file)
