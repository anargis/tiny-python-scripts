from playwright.sync_api import sync_playwright
# Add your credentials 'email' and 'password' to the file tutonota_credentials.py
from tutanota_credentials import EMAIL, PASSWORD

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False, slow_mo=500)

    # Grant notification permission before creating the page
    context = browser.new_context()
    context.grant_permissions(["notifications"], origin="https://app.tuta.com")

    page = context.new_page()
    page.set_viewport_size({"width":1200, "height":900})

    page.goto("https://app.tuta.com/login")

    email_input = page.locator('input[type="email"]')
    email_input.fill(EMAIL)

    password_input = page.locator('input[type="password"]')
    password_input.fill(PASSWORD)

    next_btn = page.get_by_title("Log in")
    next_btn.click()

    spam_button = page.locator('[data-testid="btn:folder:Spam"]')
    spam_button.wait_for(state="visible")
    spam_button.click()

    clear_spam_folder = page.get_by_title("Clear folder")
    clear_spam_folder.click()

    ok_button = page.locator('[data-testid="btn:ok_action"]')
    ok_button.wait_for(state="visible")
    ok_button.click()

    exit_b = input("Enter a key for exit the browser")
    if exit_b:
        page.close()