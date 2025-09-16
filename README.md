# Bynry Case Study – QA Automation Engineer Intern

This repository contains my solution for the **Bynry QA Automation Engineer Intern** case study.  
The goal was to design a test automation framework that validates **authentication, multi-tenant isolation, and project creation flows** using **Pytest + Playwright**.

---

## 📂 Project Structure

bynry_case_study/
├─ pages/ # Page Object Model (POM) classes for UI
│ ├─ login_page.py # Handles login-related actions
│ └─ projects_page.py # Handles project page interactions
├─ services/ # Mock API client
│ └─ api_client.py # Simulates project create/delete
├─ tests/ # Automated test cases
│ ├─ test_auth_and_multi_tenant.py # Login + tenant isolation tests
│ └─ test_project_creation_flow.py # End-to-end project creation flow
├─ conftest.py # Pytest + Playwright fixtures
├─ requirements.txt # Dependencies
├─ pytest.ini # Pytest config
└─ README.md # Documentation (this file)

## ⚡ Features

- **Pytest + Playwright** test framework.
- **Page Object Model (POM)** structure for maintainability.
- **Mock API client** (`api_client.py`) to simulate backend project creation/deletion.
- **Tests implemented**:
  - ✅ User login test.  
  - ✅ Multi-tenant isolation test.  
  - ✅ Project creation end-to-end test (desktop + mobile emulation + tenant isolation).
- **Cross-device validation**: desktop and **iPhone 13 emulation**.  
- **Cleanup after tests** via API client.

## 🛠️ Setup Instructions

### 1. Clone the repository
git clone <your-repo-link>
cd bynry_case_study
### 2. Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate  # on Mac/Linux
### 3. Install dependencies
pip install -r requirements.txt
playwright install
### 4. Run tests
pytest -v -s
Expected output:
tests/test_auth_and_multi_tenant.py ..    [ 66%]
tests/test_project_creation_flow.py .     [100%]

3 passed in X.XXs

## Notes on Test Execution
- Some tests are marked as **skipped** if no real Bynry accounts or API tokens are provided.
- This is intentional: it keeps the suite clean while showing how tests would work in a real environment.
- To enable them, set the following environment variables with real values:
  - `TEST_USER_EMAIL`, `TEST_USER_PASSWORD`
  - `TEST_COMP2_EMAIL`, `TEST_COMP2_PASSWORD`
  - `TEST_API_TOKEN`, `TEST_TENANT_ID`

### Mock Mode
Since no real Bynry accounts or API tokens were provided, this framework runs in Mock Mode:

Login is simulated in login_page.py.

Projects page is simulated in projects_page.py.

API calls are mocked in api_client.py.

This ensures all tests pass locally and demonstrate the expected flows.

If Bynry provides real test accounts, simply:

### 1.Replace the mock implementations with real ones.

### 2.Set environment variables for:

TEST_USER_EMAIL

TEST_USER_PASSWORD

TEST_COMP2_EMAIL

TEST_COMP2_PASSWORD

TEST_API_TOKEN

TEST_TENANT_ID

### 3.Re-run pytest -v.

### Conclusion:

This framework demonstrates:

A scalable test structure (POM + services + tests).

End-to-end flows for login, tenant isolation, and project creation.

Adaptability → runs in mock mode today but can easily integrate with real accounts and APIs.

### Submission Note:

Dear Bynry Team,

Please find my completed case study implementation for the QA Automation Engineer Intern role.

Implemented using Pytest + Playwright with Page Object Model (POM).

Includes tests for login, multi-tenant isolation, and project creation flows.

Since no real test accounts were provided, the framework runs in Mock Mode, but it is fully structured to switch to real APIs and UI when credentials are available.

All tests currently pass locally (pytest -v).

Thank you for the opportunity!

Best regards,
saraswati shinde