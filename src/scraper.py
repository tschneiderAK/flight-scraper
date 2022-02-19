import asyncio
import pyppeteer as pyp


origin = 'LAX'
destination = 'JFK'
depart = '04/01/2022'
rtrn = '04-08-2022'

async def main(origin, destination, depart, rtrn):
    browser = await pyp.launch()
    page = await browser.newPage()
    await page.goto('https://matrix.itasoftware.com/search')
    await page.type('[id=mat-chip-list-input-0]', origin)
    await page.type('[id=mat-chip-list-input-1]', destination)
    await page.type('[id=mat-date-range-input-0]', depart)
    await page.type('Tab')
    await page.type('[id=mat-chip-list-input-1]', rtrn)

    await page.screenshot({'path': 'test.png'})

    await browser.close()

asyncio.get_event_loop().run_until_complete(main(origin, destination, depart, rtrn))