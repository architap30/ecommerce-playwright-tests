# E-Commerce Test Automation Suite
### Playwright + Python | Page Object Model | CI/CD Ready

A professional end-to-end test automation framework built with 
Playwright and Python, testing real-world e-commerce workflows 
on Sauce Demo — a platform designed for QA practice.

---

## 🧪 Test Coverage

| Test File | Scenarios Covered |
|---|---|
| `test_login.py` | Valid login, invalid credentials, locked out user, empty fields |
| `test_cart.py` | Add to cart, remove from cart, cart persistence _(coming soon)_ |
| `test_checkout.py` | Full checkout flow, form validation _(coming soon)_ |

---

## 🏗️ Framework Architecture
ecommerce-playwright-tests/
├── tests/                  # Test files
│   └── test_login.py
├── pages/                  # Page Object Model
│   └── login_page.py
├── conftest.py             # Pytest fixtures
├── requirements.txt        # Dependencies
└── README.md

---

## 🚀 Getting Started

**1. Clone the repo:**
```bash
git clone https://github.com/architap30/ecommerce-playwright-tests.git
cd ecommerce-playwright-tests
```

**2. Create and activate virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
playwright install
```

**4. Run all tests:**
```bash
pytest tests/ -v
```

**5. Run a specific test file:**
```bash
pytest tests/test_login.py -v
```

---

## ✅ Test Results
tests/test_login.py::test_valid_login        PASSED
tests/test_login.py::test_invalid_login      PASSED
tests/test_login.py::test_empty_login        PASSED
tests/test_login.py::test_locked_out_user    PASSED
4 passed in 0.00s

---

## 🛠️ Tech Stack

- **Language:** Python 3.13
- **Framework:** Playwright
- **Test Runner:** Pytest
- **Pattern:** Page Object Model (POM)
- **CI/CD:** GitHub Actions _(coming soon)_

---

## 👩‍💻 Author

**Archita Parvatkar** — QA Engineering Leader | Dallas, TX

[![LinkedIn](https://img.shields.io/badge/LinkedIn-architaparvatkar-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/architaparvatkar)
