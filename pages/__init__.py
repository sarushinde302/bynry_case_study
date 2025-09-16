# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        # Update these selectors to match your app
        self.email_input = "#email"
        self.password_input = "#password"
        self.login_button = "#login-btn"
        self.dashboard_indicator = ".welcome-message"  # visible on successful login

    def goto(self, base_url: str):
        self.page.goto(f"{base_url}/login", wait_until="domcontentloaded")

    def login(self, email: str, password: str, timeout: int = 15000):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        # Wait for dashboard / stable signal
        self.page.wait_for_url("**/dashboard", timeout=timeout)
        self.page.wait_for_selector(self.dashboard_indicator, timeout=timeout)
