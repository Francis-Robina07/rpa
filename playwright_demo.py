import asyncio
from playwright.async_api import async_playwright

async def wikipedia_extractor():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Open Wikipedia
        await page.goto("https://www.wikipedia.org/")

        # Search topic
        topic = "Artificial Intelligence"
        await page.fill("input[name='search']", topic)
        await page.press("input[name='search']", "Enter")

        # Wait until page loads
        await page.wait_for_load_state("domcontentloaded")

        # Get all paragraphs inside main content
        paragraphs = await page.locator("#mw-content-text p").all()

        first_valid_paragraph = ""

        for para in paragraphs:
            text = await para.inner_text()
            if text.strip():   # Skip empty paragraphs
                first_valid_paragraph = text
                break

        # Clean unwanted line breaks
        clean_text = " ".join(first_valid_paragraph.split())

        # Format into readable multiple lines (sentence-wise)
        formatted_text = "\n\n".join(clean_text.split(". "))

        # Save to file
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(f"Topic: {topic}\n\n")
            file.write(formatted_text)

        print("✅ Data saved successfully in output.txt")

        await browser.close()

asyncio.run(wikipedia_extractor())