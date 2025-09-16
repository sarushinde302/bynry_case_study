import os
import time
import pytest
from bynry_case_study.pages.login_page import LoginPage
from bynry_case_study.pages.projects_page import ProjectsPage
from bynry_case_study.services.api_client import APIClient

BASE = os.getenv("APP_URL", "https://app.workflowpro.com")
API_BASE = os.getenv("API_BASE", BASE)  # if API base differs, set API_BASE env var


@pytest.mark.skipif(os.getenv("TEST_API_TOKEN") in ["", None],
                    reason="No real API token provided")
def test_project_creation_flow(page, browser, playwright):
    """
    1) Create a project via API.
    2) Verify the project appears in the web UI.
    3) Verify in mobile emulation (iPhone 13).
    4) Verify tenant isolation by logging into another tenant.
    5) Cleanup via API.
    """
    # Test configuration from environment
    tenant_id = os.getenv("TEST_TENANT_ID", "company1")
    api_token = os.getenv("TEST_API_TOKEN", "")
    ui_email = os.getenv("TEST_USER_EMAIL", "automation@company1.com")
    ui_pass = os.getenv("TEST_USER_PASSWORD", "password123")
    other_email = os.getenv("TEST_COMP2_EMAIL", "user@company2.com")
    other_pass = os.getenv("TEST_COMP2_PASSWORD", "password123")

    if not api_token:
        pytest.skip("TEST_API_TOKEN not set — required to create test data via API.")

    api = APIClient(api_token, API_BASE)
    project_name = f"Auto Project {int(time.time())}"

    # 1) Create project via API
    project_resp = api.create_project(tenant_id, project_name)
    project_id = project_resp.get("id")
    assert project_id, "API did not return project id"

    try:
        # 2) Verify in web UI (desktop)
        login = LoginPage(page)
        projects = ProjectsPage(page)
        login.goto(BASE)
        login.login(ui_email, ui_pass)
        projects.goto(BASE)
        # Wait & assert project visible
        page.wait_for_selector(f"text={project_name}", timeout=15000)
        assert page.locator(f"text={project_name}").is_visible()

        # 3) Mobile emulation (use Playwright device descriptor)
        device = playwright.devices.get("iPhone 13")
        mobile_ctx = browser.new_context(**device)
        mobile_page = mobile_ctx.new_page()
        try:
            from bynry_case_study.pages.login_page import LoginPage as MobileLogin
            from bynry_case_study.pages.projects_page import ProjectsPage as MobileProjects
            mlogin = MobileLogin(mobile_page)
            mprojects = MobileProjects(mobile_page)
            mlogin.goto(BASE)
            mlogin.login(ui_email, ui_pass)
            mprojects.goto(BASE)
            assert mobile_page.locator(f"text={project_name}").is_visible(timeout=15000)
        finally:
            mobile_ctx.close()

        # 4) Tenant isolation - login as other tenant and ensure project not visible
        page.goto(f"{BASE}/logout", wait_until="networkidle")
        login.goto(BASE)
        login.login(other_email, other_pass)
        projects.goto(BASE)
        assert not page.locator(f"text={project_name}").is_visible(timeout=3000)
    finally:
        # 5) Cleanup
        api.delete_project(tenant_id, project_id)
