# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = "input[name='email']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"
        self.dashboard_indicator = "text=Dashboard"

    def goto(self, base_url: str):
        # mock login page
        self.page.goto("data:text/html,<h1>Mock Login Page</h1>")

    def login(self, email: str, password: str):
        # simulate login success
        print(f"[MOCK LOGIN] Logging in as {email}")
        # fake dashboard HTML
        self.page.set_content("<h1>Dashboard</h1><div id='projects'></div>")
