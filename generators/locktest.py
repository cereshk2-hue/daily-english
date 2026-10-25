import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':400,'height':900})
        await pg.goto('file:///home/claude/proj/dist/preview-m1-chunjae-L6-2hmac.html')
        await pg.fill('#nm','테스트'); await pg.click('#nameform button')
        await pg.click('[data-tab=text]'); print('before start, passage visible:', await pg.locator('#script').count())
        await pg.click('[data-tab=today]'); await pg.click('[data-go="0"]')
        await pg.click('#gostart'); await pg.click('.opt >> nth=0'); await pg.click('#quit')
        await pg.click('[data-tab=text]')
        print('in progress, passage:', await pg.locator('#script').count(), 'lock:', await pg.locator('.lockcard').count())
        await pg.screenshot(path='lock_text.png')
        await pg.click('[data-tab=types]'); print('types lock:', await pg.locator('.lockcard').count(), 'typebtn:', await pg.locator('.typebtn').count())
        await pg.click('[data-sel="1"]'); print('DAY2 not started, typebtn:', await pg.locator('.typebtn').count())
        await pg.click('[data-sel="0"]'); await pg.click('[data-golock="0"]')
        print('resumed qcard:', await pg.locator('#qcard').count())
        await b.close()
asyncio.run(main())
