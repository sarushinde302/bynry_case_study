# pages/projects_page.py
class ProjectsPage:
    def __init__(self, page):
        self.page = page
        self.project_card_selector = "#projects div"

    def goto(self, base_url: str):
        # mock projects page
        html = "<h2>Projects</h2><div id='projects'></div>"
        self.page.set_content(html)

    def add_project(self, project_name: str):
        # inject fake project into DOM
        self.page.evaluate(
            """(name) => {
                const container = document.getElementById('projects');
                const div = document.createElement('div');
                div.textContent = name;
                container.appendChild(div);
            }""",
            project_name,
        )
