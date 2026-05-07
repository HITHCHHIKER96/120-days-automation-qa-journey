# 120-days-automation-qa-journey

# 🚀 120 Days Automation QA Challenge — Pritam's Journey
> Started: April 22, 2026 | Target End: August 20, 2026  
> Goal: Land a job as Automation QA Engineer / SDET

---

## 👨‍💻 About Me
- B.Tech in ECE (2025)
- Currently working in Telecom sector
- Transitioning into IT as Automation QA / SDET
- Background: Python, Java, DSA, Web Dev (HTML, CSS, JS), SQL

---

## 🎯 Goal
Get hired as an **Automation QA Engineer / SDET** by August 2026 using:
- **Python** (primary language)
- **Playwright with Python**
- **Pytest framework**
- **API Testing** (Postman + Python Requests)
- **SQL**
- **Git + GitHub Actions (CI)**

---

## 📅 The 120 Day Roadmap

### ✅ Days 1–20 | Python Foundation
- [ ] Variables, data types, loops, conditions
- [ ] Functions — args, return, scope
- [ ] OOP — classes, objects, inheritance
- [ ] Lists, dicts, tuples, sets
- [ ] File handling, exception handling
- [ ] Modules and pip — installing libraries
- **Resource:** Bro Code Python — YouTube (free)
- **Practice:** HackerRank Python track, Exercism.org Python track
- **Output:** 10 small Python scripts pushed to GitHub

---

### ✅ Days 21–55 | Playwright with Python
- [ ] Install Playwright: `pip install playwright`
- [ ] Browser launch — Chromium, Firefox, WebKit
- [ ] Locators — get_by_role, get_by_text, get_by_placeholder
- [ ] Actions — click, fill, select, hover
- [ ] Assertions — `expect(locator).to_be_visible()`
- [ ] Page Object Model (POM) pattern
- [ ] Pytest with Playwright plugin
- [ ] Screenshots and video on failure
- [ ] Headless and headed mode
- **Resources:**
  - [Playwright Official Docs](https://playwright.dev/python/docs/intro)
  - [Rahul Shetty Academy — YouTube (free)](https://www.youtube.com/@RahulShettyAcademy)
  - [Test Automation University — free](https://testautomationu.applitools.com)
- **Practice Sites:**
  - [SauceDemo](https://www.saucedemo.com)
  - [OrangeHRM Demo](https://www.orangehrm.com/demo)
  - [The Internet (Herokuapp)](https://the-internet.herokuapp.com)
- **Output:** Full automation of SauceDemo — login, add to cart, checkout, logout

---

### ✅ Days 56–80 | API Testing with Python
- [ ] What is an API — GET, POST, PUT, DELETE
- [ ] Postman — manual API testing first
- [ ] Python Requests library
- [ ] Pytest for API automation
- [ ] JSON parsing and assertion
- [ ] Status code validation
- [ ] SQL basics — SELECT, WHERE, JOIN, GROUP BY
- **Resources:**
  - Rahul Shetty Academy — YouTube (free)
  - [Python Requests Docs](https://requests.readthedocs.io)
  - [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/)
  - [HackerRank SQL](https://www.hackerrank.com/domains/sql)
- **Practice APIs:**
  - [Reqres.in](https://reqres.in) — free API to practice
  - [JSONPlaceholder](https://jsonplaceholder.typicode.com) — free
  - [Restful Booker](https://restful-booker.herokuapp.com) — main project
- **Output:** Full CRUD API automation on restful-booker.herokuapp.com

---

### ✅ Days 81–100 | Reports + CI Basics
- [ ] Pytest HTML report plugin
- [ ] Allure Reports setup with Playwright
- [ ] GitHub Actions — run tests on every commit (free CI)
- [ ] Clean README for both projects
- [ ] Polish GitHub — profile photo, bio, pinned repos
- **Resources:**
  - [Allure Report Docs](https://allurereport.org/docs)
  - [GitHub Actions Docs](https://docs.github.com/en/actions)
  - [Shields.io](https://shields.io) — add badges to README
- **Output:** Both projects have auto-generated HTML reports + CI pipeline running

---

### ✅ Days 101–110 | Resume + Interview Prep
- [ ] 1-page resume — skills, projects, education only
- [ ] LinkedIn — headline, about section, featured projects
- [ ] ISTQB Foundation Level study
- [ ] Prepare top 30 QA Automation interview Q&A
- [ ] Record yourself answering — fix your delivery
- **Resources:**
  - [ISTQB Official Syllabus (free PDF)](https://www.istqb.org)
  - [Glassdoor Interview Questions](https://www.glassdoor.co.in)
  - [ResumeWorded — free resume score](https://resumeworded.com)
- **Output:** Resume done. LinkedIn active. ISTQB exam booked.

---

### ✅ Days 111–120 | Attack the Job Market
- [ ] Minimum 10 applications per day
- [ ] Give ISTQB Foundation exam
- [ ] Follow up on applications after 5 days
- [ ] Join QA communities on LinkedIn — comment, post, engage
- [ ] Never stop pushing to GitHub
- **Where to Apply:**
  - [Naukri.com](https://www.naukri.com)
  - [LinkedIn Jobs](https://www.linkedin.com/jobs)
  - [Instahyre](https://www.instahyre.com)
  - [Foundit](https://www.foundit.in)
  - [Indeed India](https://www.indeed.co.in)
- **Output:** 100+ applications sent. Interview calls incoming.

---

## ⏰ Daily Schedule
| Time | Task |
|------|------|
| 6:00 AM – 7:30 AM | Learn and code (follow the phase) |
| 9:00 PM – 10:00 PM | Practice and push to GitHub |
| Weekends | Build projects + apply to jobs |

---

## 📂 Repository Structure
```
📦 120-days-automation-qa-journey
 ┣ 📂 python-basics
 ┃ ┗ 📄 (10 small scripts — one per topic)
 ┣ 📂 playwright-ui-testing
 ┃ ┣ 📂 pages
 ┃ ┃ ┣ 📄 login_page.py
 ┃ ┃ ┣ 📄 home_page.py
 ┃ ┃ ┗ 📄 checkout_page.py
 ┃ ┣ 📂 tests
 ┃ ┃ ┣ 📄 test_login.py
 ┃ ┃ ┣ 📄 test_checkout.py
 ┃ ┃ ┗ 📄 conftest.py
 ┃ ┗ 📄 playwright.config.py
 ┣ 📂 api-testing
 ┃ ┣ 📄 test_get_booking.py
 ┃ ┣ 📄 test_create_booking.py
 ┃ ┗ 📄 test_delete_booking.py
 ┣ 📂 reports
 ┃ ┗ 📄 (auto-generated HTML reports)
 ┣ 📂 .github
 ┃ ┗ 📂 workflows
 ┃   ┗ 📄 run-tests.yml
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```

---

## 🔥 Non-Negotiable Rules
1. **No new technology for 120 days** — Python + Playwright + API only
2. **GitHub commit every single day** — one line still counts
3. **Never miss two days in a row** — miss one, fine. Two, the habit breaks
4. **Type every line yourself** — no copy-paste from tutorials
5. **Apply from Day 111 even if not ready** — especially if not ready

---

## 📈 Progress Tracker
| Phase | Days | Status |
|-------|------|--------|
| Python Foundation | May 1–May 20 | 🔄 In Progress |
| Playwright with Python | 21–55 | ⏳ Pending |
| API Testing | 56–80 | ⏳ Pending |
| Reports + CI | 81–100 | ⏳ Pending |
| Resume + Interview Prep | 101–110 | ⏳ Pending |
| Job Applications | 111–120 | ⏳ Pending |

---

## 💭 Why I Am Doing This
I completed B.Tech in ECE in 2025. I want to build a career in IT.  
The market is clear — Python is the language. Playwright is the tool. QA Automation is the door.  
This is my commitment to myself. 120 days of focused, consistent work.  
No more confusion. No switching. Just execution.

**August 20, 2026 — I will have a job offer. 🎯**

---

*"Stop thinking. Start doing. The 120 days begin today."*
