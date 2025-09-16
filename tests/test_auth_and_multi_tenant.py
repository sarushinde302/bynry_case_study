# bynry_case_study/tests/test_auth_and_multi_tenant.py
import os
import pytest
from bynry_case_study.pages.login_page import LoginPage
from bynry_case_study.pages.projects_page import ProjectsPage

BASE = os.getenv("APP_URL", "https://app.workflowpro.com")


@pytest.mark.skipif(os.getenv("TEST_USER_EMAIL") in [None, "user1@example.com"],
                    reason="No real test accounts provided")
def test_user_login(page):
    login = LoginPage(page)
    login.goto(BASE)
    login.login(os.getenv("TEST_USER_EMAIL"), os.getenv("TEST_USER_PASSWORD"))
    assert page.locator(login.dashboard_indicator).is_visible()


@pytest.mark.skipif(os.getenv("TEST_COMP2_EMAIL") in [None, "user2@example.com"],
                    reason="No real test accounts provided")
def test_multi_tenant_access(page):
    login = LoginPage(page)
    projects = ProjectsPage(page)

    login.goto(BASE)
    login.login(os.getenv("TEST_COMP2_EMAIL"), os.getenv("TEST_COMP2_PASSWORD"))
    projects.goto(BASE)
    assert page.locator(projects.project_card_selector).first.is_visible(timeout=15000)
