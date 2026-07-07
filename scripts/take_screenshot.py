import os
import time
import requests
from playwright.sync_api import sync_playwright

FRONTEND_URL = "http://localhost:5173"

def take_screenshot():
    print("Waiting for frontend server...")
    for _ in range(30):
        try:
            response = requests.get(FRONTEND_URL)
            if response.status_code == 200:
                print("Frontend is up!")
                break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    else:
        print("Frontend did not start in time.")
        return

    print("Opening browser to take screenshot...")
    docs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs")
    os.makedirs(docs_dir, exist_ok=True)
    screenshot_path = os.path.join(docs_dir, "frontend_ui.png")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 800})
        
        # Dashboard
        print("Navigating to Dashboard UI...")
        page.goto(FRONTEND_URL, wait_until="networkidle")
        time.sleep(2)
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        # Servers
        servers_path = os.path.join(docs_dir, "servers_ui.png")
        print("Navigating to Servers UI...")
        page.goto(f"{FRONTEND_URL}/servers", wait_until="networkidle")
        time.sleep(2)
        page.screenshot(path=servers_path, full_page=True)
        print(f"Screenshot saved to {servers_path}")

        # Incidents
        incidents_path = os.path.join(docs_dir, "incidents_ui.png")
        print("Navigating to Incidents UI...")
        page.goto(f"{FRONTEND_URL}/incidents", wait_until="networkidle")
        time.sleep(2)
        page.screenshot(path=incidents_path, full_page=True)
        print(f"Screenshot saved to {incidents_path}")

        # Tickets
        tickets_path = os.path.join(docs_dir, "tickets_ui.png")
        print("Navigating to Tickets UI...")
        page.goto(f"{FRONTEND_URL}/tickets", wait_until="networkidle")
        time.sleep(2)
        page.screenshot(path=tickets_path, full_page=True)
        print(f"Screenshot saved to {tickets_path}")

        browser.close()

if __name__ == "__main__":
    take_screenshot()
