# conftest.py
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import os
import pytest
from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page

@pytest.fixture(scope="session")
def playwright_instance():
    """Start Playwright once per session."""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Browser:
    """
    Launch a Chromium browser for the whole test session.
    HEADLESS env var controls headless vs headed.
    """
    headless = os.getenv("HEADLESS", "true").lower() in ("true", "1")
    # safe args help CI environments
    browser = playwright_instance.chromium.launch(headless=headless,
                                                  args=["--no-sandbox", "--disable-dev-shm-usage"])
    yield browser
    browser.close()

@pytest.fixture()
def context(browser: Browser) -> BrowserContext:
    """New browser context for each test to isolate storage/state."""
    ctx = browser.new_context(viewport={"width": 1280, "height": 800})
    yield ctx
    ctx.close()

@pytest.fixture()
def page(context: BrowserContext) -> Page:
    """New page for each test."""
    page = context.new_page()
    yield page
    page.close()
