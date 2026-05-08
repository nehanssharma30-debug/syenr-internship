# Syenr Technologies — Internship Projects
**Intern:** [Your Name]  
**Company:** Syenr Technologies Pvt. Ltd., Pune  
**Domain:** Quality Assurance & Web Development  
**Duration:** [Start Month] – [End Month, Year]  

---

## About Syenr Technologies
Syenr Technologies is a Pune-based IT staffing and digital agency that bridges the gap between companies and consultants globally. They offer services including Staff Augmentation, Project Marketplace, Web Development, Mobile App Development, and Digital Marketing.

Website: [https://www.syenr.com](https://www.syenr.com)

---

## Projects Completed

### Project 1 — Automated QA Test Suite (`syenr_test_suite.py`)
**Domain:** Quality Assurance / Software Testing  
**Tech Stack:** Python 3, `unittest` framework, `requests` library

**What it does:**
- 17 automated test cases covering the live Syenr web platform
- Tests homepage availability, response time, HTTPS security
- Validates all 8 service pages return HTTP 200
- Checks all 3 login portals (Consultant, Organization, Employee)
- Verifies key business metrics and content are present on pages
- Generates a formatted test execution report on completion

**Why it matters in industry:**
Every software product in production needs a QA layer. This type of functional test suite is used by QA engineers at companies like Infosys, TCS, and startups alike to catch regressions before deployment. The `unittest` + `requests` combo is a standard approach for API and web testing.

**How to run:**
```bash
pip install requests
python syenr_test_suite.py
```

---

### Project 2 — Consultant Management Dashboard (Live Demo)
**Domain:** Web Development / Internal Tools  
**Tech Stack:** HTML5, CSS3, Vanilla JavaScript

**What it does:**
- Interactive dashboard to manage consultant profiles and placement status
- Displays key KPIs: total consultants, active placements, partner companies, average rating — matching Syenr's actual stats (100+ consultants, 15+ companies, 4.8/5 rating)
- Bar charts showing consultant status breakdown and top skills in demand
- Searchable consultant directory with real-time filtering
- Activity log showing recent platform events
- Placement rate donut chart by domain (Web Dev, Mobile, QA)

**Why it matters in industry:**
Internal dashboards are one of the most common projects built at IT staffing companies. HR and operations teams use these to track consultant bench status, placement timelines, and skill gaps. This project demonstrates data presentation, DOM manipulation, and UX design skills.

---

## What I Learned

| Area | Skills Gained |
|------|--------------|
| QA & Testing | Writing test cases, functional testing, HTTP status codes |
| Python | `unittest` framework, `requests` library, test automation |
| Web Dev | HTML/CSS layout, JavaScript DOM manipulation, data visualization |
| Industry Practices | Git workflow, code documentation, project structuring |
| Business Domain | IT staffing model, consultant lifecycle, staff augmentation |

---

## Git Workflow Used

```
main branch
├── commit: Initial project setup and README
├── commit: Add homepage and navigation test cases (TC-001 to TC-010)
├── commit: Add service pages and login test cases (TC-011 to TC-014)
├── commit: Add content validation tests (TC-015 to TC-017)
├── commit: Add test report generator
└── commit: Add consultant management dashboard (Project 2)
```

---

*This repository represents work done during my internship at Syenr Technologies.*
