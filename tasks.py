from invoke import task

import os
import shutil

@task(help={
    "features": "Specific feature files or directories to run (space-separated)",
    "tags": "Optional tags to filter scenarios"
})
def run_tests(c, features="features", tags=""):
    """
    Run behave tests with optional feature files or tags.
    Example:
      invoke run-tests --features="features/book_store.feature"
      invoke run-tests --tags="@smoke"
      invoke run-tests --features="features/file1.feature features/file2.feature" --tags="@smoke"
    """
    # Clean old Allure results before running
    results_path = "reports/allure-results"
    if os.path.exists(results_path):
        shutil.rmtree(results_path)
    os.makedirs(results_path)

    tag_option = f"--tags={tags}" if tags else ""
    c.run(f"behave {features} {tag_option} -f allure_behave.formatter:AllureFormatter -o reports/allure-results")


@task
def report(c):
    """
    Generate and open Allure report.
    """
    c.run("allure generate reports/allure-results -o reports/allure-report --clean")
    c.run("allure open reports/allure-report")
