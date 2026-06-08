"""
DTW Ignite 2026 Agenda Scraper
Uses Playwright with Edge browser to navigate the agenda page,
click through all days, scroll to load all sessions, and extract session data.
Output: JSON files per day in calendar/raw/
"""

import json
import time
import os
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.tmforum.org/events/dtw/whats-on/agenda"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def accept_cookies(page):
    """Try to accept cookie consent — click 'Allow all' button."""
    try:
        # The cookie dialog has "Allow all" as a dark button
        allow_all = page.locator("button:has-text('Allow all')")
        if allow_all.is_visible(timeout=8000):
            allow_all.click()
            time.sleep(2)
            print("  Accepted cookies (clicked 'Allow all')")
            return
    except:
        pass

    # Fallback: try other selectors
    for selector in [
        "#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll",
        "button:has-text('Accept all')",
        "[id*='accept']",
        "[class*='accept']",
    ]:
        try:
            btn = page.locator(selector).first
            if btn.is_visible(timeout=2000):
                btn.click()
                time.sleep(2)
                print(f"  Accepted cookies via: {selector}")
                return
        except:
            continue

    print("  WARNING: Could not find cookie accept button")


def count_session_links(page):
    """Count current number of session links on page."""
    return len(page.locator("a[href*='session-detail-page-2026']").all())


def load_all_sessions(page):
    """Scroll until no new sessions appear after 2 seconds."""
    prev_count = count_session_links(page)
    print(f"  Initial sessions visible: {prev_count}")

    while True:
        # Scroll to bottom
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)

        # Check if new sessions appeared
        new_count = count_session_links(page)
        if new_count > prev_count:
            print(f"  Loaded more: {prev_count} -> {new_count}")
            prev_count = new_count
        else:
            # No new elements after 2s — done
            print(f"  Done loading. Total: {new_count}")
            break

    return new_count


def extract_sessions(page):
    """Extract all visible session cards from the page."""
    sessions = []
    session_elements = page.locator("a[href*='session-detail-page-2026']").all()

    for elem in session_elements:
        try:
            text = elem.inner_text(timeout=3000)
            href = elem.get_attribute("href") or ""
            lines = [l.strip() for l in text.split("\n") if l.strip()]

            session = {
                "title": "",
                "type": "",
                "date_time": "",
                "stage": "",
                "description": "",
                "url": href,
                "raw_lines": lines
            }

            # Parse lines — typical pattern:
            # Line with title, line with type, line with "DD June 2026 HH:MM-HH:MM", line with stage, description
            for line in lines:
                if "June 2026" in line and (":" in line or "-" in line):
                    session["date_time"] = line
                elif any(word in line.lower() for word in ["stage", "garage", "arena", "showcase", "circle", "loft"]):
                    if not session["stage"]:
                        session["stage"] = line
                elif any(word in line for word in ["Keynote", "Masterclass", "Spotlight", "Catalyst", "Session", "Panel"]):
                    if not session["type"]:
                        session["type"] = line

            # Title is usually the first meaningful line (not a type label)
            for line in lines:
                if line and line != session["type"] and "June 2026" not in line and line != session["stage"]:
                    session["title"] = line
                    break

            # Description is remaining text after known fields
            known = {session["title"], session["type"], session["date_time"], session["stage"]}
            desc_lines = [l for l in lines if l not in known and l]
            if desc_lines:
                session["description"] = " ".join(desc_lines[-3:])  # last few lines are usually description

            if session["title"]:
                sessions.append(session)
        except Exception as e:
            continue

    return sessions


def scrape_day(page, day_index):
    """Click on a day tab and scrape all sessions."""
    day_numbers = ["23", "24", "25"]
    day_names = ["Tuesday 23 June", "Wednesday 24 June", "Thursday 25 June"]
    day_num = day_numbers[day_index]
    day_name = day_names[day_index]

    print(f"\n{'='*60}")
    print(f"Scraping: {day_name}")
    print(f"{'='*60}")

    # Click on day tab — buttons with class "Buttonstyles__Container"
    # containing spans with data-desktop="true" text like "Tuesday 23", "Wednesday 24", "Thursday 25"
    clicked = False
    day_labels = ["Tuesday 23", "Wednesday 24", "Thursday 25"]
    target_label = day_labels[day_index]

    try:
        btn = page.locator(f"button.Buttonstyles__Container-sc-z90oc8-0:has(span[data-desktop='true']:has-text('{target_label}'))")
        if btn.first.is_visible(timeout=3000):
            btn.first.click()
            time.sleep(3)
            clicked = True
            print(f"  Clicked day tab: '{target_label}'")
    except:
        pass

    if not clicked:
        # Fallback: find button containing the mobile span with just the number
        try:
            btn = page.locator(f"button:has(span[data-mobile='true']:text-is('{day_num}'))")
            if btn.first.is_visible(timeout=3000):
                btn.first.click()
                time.sleep(3)
                clicked = True
                print(f"  Clicked day tab (mobile fallback): '{day_num}'")
        except:
            pass

    if not clicked:
        print(f"  WARNING: Could not find day tab for {day_name}")

    # Wait for content to update
    time.sleep(2)

    # Load all sessions by scrolling/clicking
    total = load_all_sessions(page)

    # Extract session data
    sessions = extract_sessions(page)
    print(f"  Extracted {len(sessions)} sessions with data")

    return sessions


def main():
    print("DTW Ignite 2026 Agenda Scraper")
    print("=" * 60)
    print(f"URL: {BASE_URL}")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Browser: Edge (visible)")
    print()

    with sync_playwright() as p:
        # Launch Edge browser (visible)
        browser = p.chromium.launch(
            channel="msedge",
            headless=False,
            slow_mo=300
        )
        context = browser.new_context(
            viewport={"width": 1024, "height": 900}
        )
        page = context.new_page()

        # Navigate to agenda
        print("Navigating to agenda page...")
        try:
            page.goto(BASE_URL, wait_until="domcontentloaded", timeout=30000)
        except:
            page.goto(BASE_URL, timeout=60000)
        time.sleep(5)

        # Accept cookies
        accept_cookies(page)
        time.sleep(2)

        # Take initial screenshot
        page.screenshot(path=os.path.join(OUTPUT_DIR, "00_page_loaded.png"))
        print("  Page loaded, screenshot saved")

        # Scrape each day
        days = [
            ("day1_tuesday_23.json", "screenshot_day1.png"),
            ("day2_wednesday_24.json", "screenshot_day2.png"),
            ("day3_thursday_25.json", "screenshot_day3.png"),
        ]

        all_sessions = {}
        day_names = ["Tuesday 23 June", "Wednesday 24 June", "Thursday 25 June"]

        for i, (json_file, screenshot_file) in enumerate(days):
            sessions = scrape_day(page, i)
            all_sessions[day_names[i]] = sessions

            # Save JSON
            output_path = os.path.join(OUTPUT_DIR, json_file)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(sessions, f, indent=2, ensure_ascii=False)
            print(f"  Saved to {json_file}")

            # Screenshot
            page.screenshot(path=os.path.join(OUTPUT_DIR, screenshot_file))

            # Scroll back to top for next day
            page.evaluate("window.scrollTo(0, 0)")
            time.sleep(1)

        # Save combined
        combined_path = os.path.join(OUTPUT_DIR, "all_sessions.json")
        with open(combined_path, "w", encoding="utf-8") as f:
            json.dump(all_sessions, f, indent=2, ensure_ascii=False)

        # Summary
        print(f"\n{'='*60}")
        print("DONE — Summary:")
        print(f"{'='*60}")
        for day_name, sessions in all_sessions.items():
            print(f"  {day_name}: {len(sessions)} sessions")
        total = sum(len(s) for s in all_sessions.values())
        print(f"  TOTAL: {total} sessions")
        print(f"\nFiles saved to: {OUTPUT_DIR}")

        browser.close()


if __name__ == "__main__":
    main()
