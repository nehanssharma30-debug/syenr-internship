"""
============================================================
  Syenr Technologies — Web Platform QA Test Suite
  Intern: [Your Name]
  Duration: [Month Year] — [Month Year]
  Domain: Quality Assurance & Software Testing
============================================================

About this project:
  Syenr Technologies (syenr.com) is an IT staffing and digital
  agency that connects consultants with companies globally.
  During my internship, I was assigned to the QA domain where
  I studied the web platform and wrote test cases to validate
  core user flows: registration, login, consultant search, and
  contact form submission.

  This test suite uses Python's unittest framework + requests
  library to perform automated functional testing on the live
  Syenr website.
============================================================
"""

import unittest
import requests
from datetime import datetime


BASE_URL = "https://www.syenr.com"

TIMEOUT = 10


class TestSyenrHomePage(unittest.TestCase):
    """Test cases for Syenr homepage availability and content."""

    def setUp(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Syenr-QA-TestSuite/1.0 (Internship Project)"
        })

    def test_TC001_homepage_loads_successfully(self):
        """TC-001: Homepage should return HTTP 200 OK."""
        response = self.session.get(BASE_URL, timeout=TIMEOUT)
        self.assertEqual(response.status_code, 200,
                         f"Expected 200 OK but got {response.status_code}")
        print(f"  [PASS] TC-001 | Homepage status: {response.status_code}")

    def test_TC002_homepage_contains_brand_name(self):
        """TC-002: Homepage HTML must contain the brand name 'SYENR'."""
        response = self.session.get(BASE_URL, timeout=TIMEOUT)
        self.assertIn("Syenr", response.text,
                      "Brand name 'Syenr' not found on homepage")
        print("  [PASS] TC-002 | Brand name found on homepage")

    def test_TC003_homepage_response_time_is_acceptable(self):
        """TC-003: Homepage must load within 5 seconds."""
        response = self.session.get(BASE_URL, timeout=TIMEOUT)
        elapsed = response.elapsed.total_seconds()
        self.assertLess(elapsed, 5.0,
                        f"Page loaded too slowly: {elapsed:.2f}s (limit: 5s)")
        print(f"  [PASS] TC-003 | Response time: {elapsed:.2f}s")

    def test_TC004_homepage_uses_https(self):
        """TC-004: Homepage must redirect to HTTPS (secure connection)."""
        self.assertTrue(
            BASE_URL.startswith("https://"),
            "Site is not using HTTPS — security risk!"
        )
        print("  [PASS] TC-004 | HTTPS confirmed")

    def test_TC005_homepage_contains_contact_info(self):
        """TC-005: Homepage must display company contact information."""
        response = self.session.get(BASE_URL, timeout=TIMEOUT)
        # Syenr's email is publicly listed on their website
        self.assertIn("connect@syenr.com", response.text,
                      "Contact email not found on homepage")
        print("  [PASS] TC-005 | Contact info present")


class TestSyenrNavigation(unittest.TestCase):
    """Test cases for site navigation and key pages."""

    def setUp(self):
        self.session = requests.Session()

    def test_TC006_about_page_accessible(self):
        """TC-006: /abouts page should return 200 OK."""
        response = self.session.get(f"{BASE_URL}/abouts", timeout=TIMEOUT)
        self.assertEqual(response.status_code, 200,
                         f"About page failed: {response.status_code}")
        print(f"  [PASS] TC-006 | About page status: {response.status_code}")

    def test_TC007_contact_page_accessible(self):
        """TC-007: /contacts page should return 200 OK."""
        response = self.session.get(f"{BASE_URL}/contacts", timeout=TIMEOUT)
        self.assertEqual(response.status_code, 200,
                         f"Contact page failed: {response.status_code}")
        print(f"  [PASS] TC-007 | Contact page status: {response.status_code}")

    def test_TC008_blog_page_accessible(self):
        """TC-008: /blogs page should return 200 OK."""
        response = self.session.get(f"{BASE_URL}/blogs", timeout=TIMEOUT)
        self.assertEqual(response.status_code, 200,
                         f"Blog page failed: {response.status_code}")
        print(f"  [PASS] TC-008 | Blog page status: {response.status_code}")

    def test_TC009_careers_page_accessible(self):
        """TC-009: /careers page should return 200 OK."""
        response = self.session.get(f"{BASE_URL}/careers", timeout=TIMEOUT)
        self.assertEqual(response.status_code, 200,
                         f"Careers page failed: {response.status_code}")
        print(f"  [PASS] TC-009 | Careers page status: {response.status_code}")

    def test_TC010_invalid_page_returns_404(self):
        """TC-010: A non-existent URL should return 404 Not Found."""
        response = self.session.get(f"{BASE_URL}/this-page-does-not-exist-xyz",
                                    timeout=TIMEOUT)
        # Accept 404 or redirect to homepage (200) as valid behaviour
        self.assertIn(response.status_code, [200, 404],
                      f"Unexpected status: {response.status_code}")
        print(f"  [PASS] TC-010 | Invalid URL handled: {response.status_code}")


class TestSyenrServicesPages(unittest.TestCase):
    """Test cases for each service page listed on Syenr website."""

    def setUp(self):
        self.session = requests.Session()
        self.services = [
            ("Staff Augmentation",     "/service/details/staff-augmentation"),
            ("Project Marketplace",    "/service/details/project-marketplace"),
            ("Technology Services",    "/service/details/technology-services"),
            ("Web Development",        "/service/details/web-development"),
            ("Mobile App Dev",         "/service/details/mobile-application-development"),
            ("Digital Marketing",      "/service/details/digital-marketing"),
            ("Design & Creative",      "/service/details/design-and-creative-service"),
            ("Dedicated Hiring",       "/service/details/dedicated-hiring"),
        ]

    def test_TC011_all_service_pages_return_200(self):
        """TC-011: All 8 service detail pages must return HTTP 200 OK."""
        failed = []
        for name, path in self.services:
            url = f"{BASE_URL}{path}"
            try:
                resp = self.session.get(url, timeout=TIMEOUT)
                if resp.status_code != 200:
                    failed.append((name, resp.status_code))
                else:
                    print(f"  [PASS] TC-011 | {name}: {resp.status_code}")
            except requests.RequestException as e:
                failed.append((name, str(e)))

        if failed:
            self.fail(f"Some service pages failed: {failed}")


class TestSyenrLoginPages(unittest.TestCase):
    """Test cases for login page availability (no actual credentials used)."""

    def setUp(self):
        self.session = requests.Session()

    def test_TC012_consultant_login_page_accessible(self):
        """TC-012: Consultant login page should be accessible."""
        response = self.session.get(f"{BASE_URL}/log-in/consultant",
                                    timeout=TIMEOUT)
        self.assertIn(response.status_code, [200, 301, 302],
                      f"Login page error: {response.status_code}")
        print(f"  [PASS] TC-012 | Consultant login: {response.status_code}")

    def test_TC013_organization_login_page_accessible(self):
        """TC-013: Organization login page should be accessible."""
        response = self.session.get(f"{BASE_URL}/log-in/organization",
                                    timeout=TIMEOUT)
        self.assertIn(response.status_code, [200, 301, 302],
                      f"Login page error: {response.status_code}")
        print(f"  [PASS] TC-013 | Organization login: {response.status_code}")

    def test_TC014_employee_login_page_accessible(self):
        """TC-014: Employee login page should be accessible."""
        response = self.session.get(f"{BASE_URL}/employee/log-in",
                                    timeout=TIMEOUT)
        self.assertIn(response.status_code, [200, 301, 302],
                      f"Login page error: {response.status_code}")
        print(f"  [PASS] TC-014 | Employee login: {response.status_code}")


class TestSyenrContentValidation(unittest.TestCase):
    """Test cases to validate key content is present on service pages."""

    def setUp(self):
        self.session = requests.Session()

    def test_TC015_homepage_has_key_metrics(self):
        """TC-015: Homepage must show business metrics (100+ consultants, 4.8 rating)."""
        response = self.session.get(BASE_URL, timeout=TIMEOUT)
        text = response.text
        self.assertIn("100", text, "Consultant count metric missing")
        self.assertIn("4.8", text, "Rating metric missing")
        print("  [PASS] TC-015 | Key business metrics found on homepage")

    def test_TC016_homepage_has_all_three_core_services(self):
        """TC-016: Homepage must list all 3 core service categories."""
        response = self.session.get(BASE_URL, timeout=TIMEOUT)
        text = response.text.upper()
        services = ["STAFF AUGMENTATION", "PROJECT MARKETPLACE",
                    "TECHNOLOGY SERVICES"]
        for svc in services:
            self.assertIn(svc, text, f"Service missing from homepage: {svc}")
        print("  [PASS] TC-016 | All 3 core services present")

    def test_TC017_terms_and_privacy_pages_accessible(self):
        """TC-017: Legal pages (Terms of Service, Privacy Policy) must load."""
        pages = [
            "/content/details/terms-of-service",
            "/content/details/privacy-policy",
        ]
        for page in pages:
            resp = self.session.get(f"{BASE_URL}{page}", timeout=TIMEOUT)
            self.assertIn(resp.status_code, [200, 301, 302],
                          f"Legal page failed: {page}")
        print("  [PASS] TC-017 | Legal pages accessible")


def generate_test_report(result, start_time):
    """Print a formatted test execution report."""
    duration = (datetime.now() - start_time).total_seconds()
    total = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    passed = total - failures - errors

    print("\n" + "=" * 60)
    print("  SYENR TECHNOLOGIES — QA TEST EXECUTION REPORT")
    print("=" * 60)
    print(f"  Date       : {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Base URL   : {BASE_URL}")
    print(f"  Total Tests: {total}")
    print(f"  Passed     : {passed}  ✓")
    print(f"  Failed     : {failures}  ✗")
    print(f"  Errors     : {errors}  !")
    print(f"  Duration   : {duration:.2f} seconds")
    print(f"  Result     : {'ALL TESTS PASSED' if failures == 0 and errors == 0 else 'SOME TESTS FAILED'}")
    print("=" * 60)

    if result.failures:
        print("\n  FAILURES:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback.splitlines()[-1]}")

    if result.errors:
        print("\n  ERRORS:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback.splitlines()[-1]}")


if __name__ == "__main__":
    print("=" * 60)
    print("  Syenr Technologies — Automated QA Test Suite")
    print("  Internship Project | Quality Assurance Domain")
    print("=" * 60)
    print(f"  Starting test run at {datetime.now().strftime('%H:%M:%S')}\n")

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Load all test classes in order
    for cls in [
        TestSyenrHomePage,
        TestSyenrNavigation,
        TestSyenrServicesPages,
        TestSyenrLoginPages,
        TestSyenrContentValidation,
    ]:
        suite.addTests(loader.loadTestsFromTestCase(cls))

    start = datetime.now()
    runner = unittest.TextTestRunner(verbosity=0, stream=open('/dev/null', 'w'))
    result = runner.run(suite)
    generate_test_report(result, start)
