import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':420,'height':1400})
        await pg.goto('file:///home/claude/proj/dist/preview-h2-mock-2609-angok-etlg7.html')
        await pg.fill('#nm','테스트'); await pg.click('#nameform button')
        await pg.click('[data-tab=types]'); await pg.click('[data-sel="%s"]'%sys.argv[1])
        await pg.click('[data-free="1"]')
        for i in range(int(sys.argv[2])):
            t=await pg.inner_text('#qcard')
            if sys.argv[3] in t: break
            await pg.click('.opt >> nth=0'); await pg.click('#nx')
        await pg.screenshot(path='shot_%s.png'%sys.argv[1],full_page=True)
        await b.close()
asyncio.run(main())
