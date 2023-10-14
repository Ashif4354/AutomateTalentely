from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from requests import get
from aiohttp import ClientSession
import asyncio

# driver = webdriver.Edge()
# driver.get("http://localhost:3000/")
# sleep(5)

# check_box = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
# check_box.click()
# sleep(10)

async def get_request(session):    

    response = await session.get('http://localhost:3000/')
    print(response.status)


async def main():
    async with ClientSession() as session:
        tasks = []
        for i in range(0, 10000):
            tasks.append(asyncio.create_task(get_request(session)))
        
        await asyncio.gather(*tasks)

    

asyncio.run(main())