# Python-Playwright

# 1️⃣ What the examiner expects to see 

For a Playwright Python project, reviewers usually look for:

- ✅ Clean project structure
- ✅ Virtual environment
- ✅ pytest usage
- ✅ Clear README
- ✅ Git hygiene
- ✅ Config separation
- ✅ Page Object Model (POM)
- ✅ Deterministic tests (no sleeps)
- ✅ CI-ready setup

You do not need to over-engineer — clarity beats complexity.

# 2️⃣ Install required tools (clean PC)
Install these first:
- Python 3.10+ (important)
- VS Code
- Git (already done)

Verify:
```Bash
python --version
git --version
```

# 3️⃣ Create the project
```bash
 mkdir playwright-python-exam
 cd playwright-python-exam
 git init
```

# 4️⃣ Create virtual environment (BEST PRACTICE)
```Bash
python -m venv .venv
```

Activate:

Windows
```Bash
.venv\Scripts\activate
```

💡 Examiners expect this.

# 5️⃣ Install dependencies
```Bash
pip install playwright pytest pytest-playwright
python -m playwright install
```

Freeze dependencies:
```Bash
pip freeze > requirements.txt
```

# 6️⃣ Recommended project structure (⭐⭐⭐⭐⭐)

This is a professional, exam-ready layout:
```
playwright-python-exam/
│
├── .github/
│   └── workflows/
│       └── tests.yml          # CI (optional but impressive)
│
├── src/
│   ├── config/
│   │   └── config.py
│   │
│   ├── pages/                 # Page Object Model
│   │   ├── base_page.py
│   │   └── login_page.py
│   │
│   ├── utils/
│   │   └── helpers.py
│   │
│   └── __init__.py
│
├── tests/
│   ├── test_login.py
│   └── conftest.py
│
├── .gitignore
├── pytest.ini
├── requirements.txt
├── README.md
└── playwright.config.py (optional)
```

# 7️⃣ Key best-practice files (important)
`.gitignore`
```gitignore
- `.venv/`
- `__pycache__/`
- `.pytest_cache/`
- `.env`
```

`pytest.ini`
```pytest.ini
[pytest]
addopts = -v --headed
testpaths = tests
pythonpath = src
```

Shows you understand test configuration.

`conftest.py` (fixtures = VERY important)
```python
import pytest

@pytest.fixture
def base_url():
    return "https://example.com"
```

Page Object Model example
`pages/base_page.py`
```python
class BasePage:
    def __init__(self, page):
        self.page = page
```

`pages/login_page.py`
```python
from .base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type=submit]")
```

Test example
`tests/test_login.py`
```python
def test_login_success(page, base_url):
    page.goto(base_url)
    assert page.title() != ""
```

💡 Uses Playwright’s built-in `page` fixture — good practice.

# 8️⃣ README.md (VERY IMPORTANT FOR EXAM)

Your README should include:
---------------------------------------------
# Playwright Python Automation Project

## Tech Stack
- Python
- Playwright
- pytest

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install
```

Run tests
```bash
pytest
```

Project Structure

- pages: Page Object Model

- tests: Test cases

- config: Configuration files
----------------------------------------------------

A good README = instant bonus points.

---

# 9️⃣ Best practices examiners LOVE

✅ Page Object Model  
✅ No `time.sleep()`  
✅ Use Playwright auto-waiting  
✅ Clear test names  
✅ Small focused tests  
✅ Meaningful assertions  
✅ Git commits like: feat: add login page object | test: add login happy path


---

# 🔟 Optional but impressive (CI)

Add GitHub Actions:
- Runs tests on every push
- Shows real-world readiness

I can generate this for you in 2 minutes if you want.

---

# 1️⃣1️⃣ Common mistakes to avoid ❌

❌ All logic inside tests  
❌ Hardcoded sleeps  
❌ No virtualenv  
❌ No README  
❌ Huge test functions  
❌ No structure  

---
