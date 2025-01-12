discord_webhook_url = ''

def send_discord_embed(title, description, color):
    import requests
    data = {
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": color
            }
        ]
    }
    result = requests.post(discord_webhook_url, json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))


for i in range(0, 100):
    send_discord_embed('test', 'test', 0x00ff00)