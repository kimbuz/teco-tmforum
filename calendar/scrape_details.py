"""
DTW Ignite 2026 — Session Detail Scraper (Full)
Reads session URLs from per-day JSON files, navigates to each detail page,
extracts structured data, and updates the JSON files with enriched info.
"""

import json
import time
import os
import re
from playwright.sync_api import sync_playwright

RAW_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw")


def accept_cookies(page):
    """Click 'Allow all' on cookie banner."""
    try:
        btn = page.locator("button:has-text('Allow all')")
        if btn.is_visible(timeout=5000):
            btn.click()
            time.sleep(1)
    except:
        pass


def parse_main_text(text):
    """Parse the main text block into structured fields."""
    detail = {
        "full_title": "",
        "date": "",
        "time_slot": "",
        "stage": "",
        "tracks": [],
        "session_type": "",
        "description": "",
        "speakers": [],
    }

    # Remove navigation/header noise
    lines = text.split("\n")
    # Find where content starts (after "Get tickets" or the title)
    start_idx = 0
    for i, line in enumerate(lines):
        if "Get tickets" in line:
            start_idx = i + 1
            break
    content_lines = [l.strip() for l in lines[start_idx:] if l.strip()]

    if not content_lines:
        return detail

    # First meaningful line is usually the title
    detail["full_title"] = content_lines[0] if content_lines else ""

    # Parse date/time — look for pattern like "25 de junio de 2026" or "23 June 2026"
    for line in content_lines[:10]:
        if "junio de 2026" in line or "June 2026" in line:
            detail["date"] = line
        time_match = re.search(r'(\d{1,2}:\d{2})\s*[-–]\s*(\d{1,2}:\d{2})', line)
        if time_match and not detail["time_slot"]:
            # Normalize: remove spaces around dash
            detail["time_slot"] = f"{time_match.group(1)}-{time_match.group(2)}"

    # Find stage — match against known stage names
    KNOWN_STAGES = [
        "Park stage",
        "Autonomous Networks Mission Garage",
        "CIT&E Mission Garage",
        "Trustworthy AI & Data Mission Garage",
        "TM Forum industry showcase stage",
        "Catalyst showcase",
        "The Loft",
        "Spotlight Stage",
        "Future skills stage",
        "Vision stage",
        "Build stage",
        "Growth stage",
        "Composable IT & Ecosystems Mission Garage",
        "Catalyst Moonshot showcase",
        "M4 (Meeting Room 4)",
        "TEN100 | Meeting room 5",
        "Innovation arena stage",
        "The Loft Stage",
    ]
    for line in content_lines[:15]:
        for stage_name in KNOWN_STAGES:
            if line.strip() == stage_name:
                detail["stage"] = stage_name
                break
        if detail["stage"]:
            break

    # Find session type — match against known types (exact line or title prefix)
    KNOWN_TYPES = ["Keynote", "Catalyst", "Spotlight", "Awards", "Masterclass"]
    for line in content_lines[:15]:
        for type_name in KNOWN_TYPES:
            if line.strip() == type_name:
                detail["session_type"] = type_name
                break
        if detail["session_type"]:
            break
    # Fallback: check if title starts with a known type
    if not detail["session_type"]:
        title_check = detail.get("full_title", "") or (content_lines[0] if content_lines else "")
        for type_name in KNOWN_TYPES:
            if title_check.startswith(type_name):
                detail["session_type"] = type_name
                break

    # Find tracks — only short known track labels, not descriptions
    KNOWN_TRACKS = [
        "Autonomous Networks",
        "Autonomous operations",
        "AI & Data",
        "AI (Artificial Intelligence)",
        "Composable IT & Ecosystems",
        "Leadership",
        "Customer experience",
        "Network transformation",
        "IT transformation",
        "5G monetization",
        "Business models",
        "B2B services",
        "Ecosystem management",
        "Marketplaces",
        "Open APIs",
        "Cloud migration",
        "Skills transformation",
        "Innovation",
        "Quantum computing",
        "Social activities",
        "AI readiness",
        "AI management",
        "Data management",
        "BSS (Business Support Systems)",
        "IT & process automation",
        "ODA (Open Digital Architecture)",
        "Closed loop automation",
        "Networks",
    ]
    for line in content_lines[:20]:
        if line in KNOWN_TRACKS:
            detail["tracks"].append(line)

    # Find description — paragraphs between type/tracks and speakers section
    desc_started = False
    desc_lines = []
    for line in content_lines:
        if line == "Session speakers" or line == "Also running at this time":
            break
        # Skip header lines we already parsed
        if line == detail["full_title"] or line == detail["date"] or line == detail["time_slot"]:
            continue
        if line == detail["stage"] or line == detail["session_type"]:
            continue
        if line in detail["tracks"]:
            continue
        # Description is usually longer text
        if len(line) > 30 or desc_started:
            desc_started = True
            desc_lines.append(line)

    detail["description"] = "\n".join(desc_lines)

    # Extract key topics (lines that look like bullet points)
    for line in desc_lines:
        if line.startswith(("- ", "• ", "· ")) or (len(line) < 100 and line[0].isupper() and not line.endswith(".")):
            # Could be a topic/bullet
            pass

    # Find speakers section
    speakers_started = False
    speaker_lines = []
    for line in content_lines:
        if line == "Session speakers":
            speakers_started = True
            continue
        if line == "Also running at this time":
            break
        if speakers_started:
            speaker_lines.append(line)

    # Parse speakers — they come in pairs: Name, then Title
    i = 0
    while i < len(speaker_lines):
        name = speaker_lines[i]
        title = speaker_lines[i + 1] if i + 1 < len(speaker_lines) else ""
        # Skip if it looks like a session title (too long or contains time)
        if len(name) < 60 and ":" not in name[:5] and "June" not in name:
            detail["speakers"].append({"name": name, "role": title})
            i += 2
        else:
            i += 1

    return detail


def main():
    print("DTW Ignite 2026 — Full Session Detail Scraper")
    print("=" * 60)

    # Load all sessions
    day_files = ["day1_tuesday_23.json", "day2_wednesday_24.json", "day3_thursday_25.json"]
    all_days_data = {}
    all_urls = []

    for filename in day_files:
        filepath = os.path.join(RAW_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            sessions = json.load(f)
        all_days_data[filename] = sessions
        for i, session in enumerate(sessions):
            url = session.get("url", "")
            if url and "session-detail" in url:
                if not url.startswith("http"):
                    url = "https://www.tmforum.org" + url
                all_urls.append((filename, i, url))

    print(f"Total sessions to scrape: {len(all_urls)}")
    print()

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=False, slow_mo=150)
        context = browser.new_context(viewport={"width": 1024, "height": 900})
        page = context.new_page()

        # First page — accept cookies
        page.goto(all_urls[0][2], wait_until="domcontentloaded", timeout=20000)
        time.sleep(3)
        accept_cookies(page)
        time.sleep(1)

        for idx, (day_file, session_idx, url) in enumerate(all_urls):
            print(f"[{idx+1}/{len(all_urls)}] ", end="")

            try:
                page.goto(url, wait_until="domcontentloaded", timeout=15000)
                time.sleep(2)

                # Get the real title from h1 (not the nav breadcrumb)
                real_title = ""
                try:
                    h1_elements = page.locator("h1").all()
                    for h1 in h1_elements:
                        txt = h1.inner_text(timeout=2000).strip()
                        if txt and txt != "DTW Ignite" and len(txt) > 3:
                            real_title = txt
                            break
                except:
                    pass

                # Get main text — handle unicode properly
                try:
                    main_text = page.locator("main").first.inner_text(timeout=5000)
                except:
                    main_text = page.locator("body").inner_text(timeout=5000)

                # Normalize unicode characters that cause encoding issues
                main_text = main_text.replace('\u2011', '-').replace('\u2013', '-').replace('\u2014', '-')
                main_text = main_text.replace('\u2018', "'").replace('\u2019', "'")
                main_text = main_text.replace('\u201c', '"').replace('\u201d', '"')
                main_text = main_text.replace('\u00a0', ' ')

                if real_title:
                    real_title = real_title.replace('\u2011', '-').replace('\u2013', '-').replace('\u2014', '-')

                # Parse
                detail = parse_main_text(main_text[:8000])

                # Override title with the real h1
                if real_title:
                    detail["full_title"] = real_title

                # Normalize time_slot — remove extra spaces around dash
                if detail["time_slot"]:
                    detail["time_slot"] = re.sub(r'\s*[-–]\s*', '-', detail["time_slot"])

                all_days_data[day_file][session_idx]["detail"] = detail

                title = detail["full_title"][:60]
                n_speakers = len(detail["speakers"])
                print(f"'{title}' | {n_speakers} spk | {detail['time_slot']}")

            except Exception as e:
                print(f"ERROR: {e}")
                all_days_data[day_file][session_idx]["detail"] = {"_error": str(e)}

        browser.close()

    # Save enriched JSONs
    print(f"\n{'='*60}")
    print("Saving enriched data...")
    for filename, sessions in all_days_data.items():
        filepath = os.path.join(RAW_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(sessions, f, indent=2, ensure_ascii=False)
        enriched = sum(1 for s in sessions if "detail" in s and "_error" not in s.get("detail", {}))
        print(f"  {filename}: {enriched}/{len(sessions)} sessions enriched")

    print("\nDONE!")


if __name__ == "__main__":
    main()
