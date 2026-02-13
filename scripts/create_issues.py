"""
Script to create GitHub issues for all 75 Blind LeetCode problems.

Usage:
    python scripts/create_issues.py

Requires:
    - GITHUB_TOKEN environment variable set with repo scope
    - GITHUB_REPOSITORY environment variable (e.g., "cd155/blind-75-python")
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error


def extract_problems(src_dir="src"):
    """Extract problem details from all solution files."""
    problems = []

    for category in sorted(os.listdir(src_dir)):
        cat_path = os.path.join(src_dir, category)
        if not os.path.isdir(cat_path) or category.startswith("_"):
            continue
        for filename in sorted(os.listdir(cat_path)):
            if filename.endswith(".py") and filename != "__init__.py":
                filepath = os.path.join(cat_path, filename)
                with open(filepath, "r") as f:
                    content = f.read()

                match = re.search(r'"""(.*?)"""', content, re.DOTALL)
                if not match:
                    continue

                docstring = match.group(1).strip()
                lines = docstring.split("\n")
                title_match = re.match(r"LeetCode\s+(\d+):\s+(.*)", lines[0])
                if not title_match:
                    continue

                lc_num = int(title_match.group(1))
                title = title_match.group(2).strip()
                description = "\n".join(lines[1:]).strip()

                problems.append(
                    {
                        "number": lc_num,
                        "title": title,
                        "category": category,
                        "filename": filename,
                        "filepath": filepath,
                        "description": description,
                    }
                )

    problems.sort(key=lambda x: x["number"])
    return problems


LEETCODE_SLUG_OVERRIDES = {
    "three_sum.py": "3sum",
    "add_and_search_word.py": "design-add-and-search-words-data-structure",
    "lowest_common_ancestor_of_a_bst.py": "lowest-common-ancestor-of-a-binary-search-tree",
    "implement_trie_prefix_tree.py": "implement-trie-prefix-tree",
    "number_of_1_bits.py": "number-of-1-bits",
    "set_matrix_zeroes.py": "set-matrix-zeroes",
}


def get_leetcode_slug(filename):
    """Get the LeetCode problem URL slug from the filename."""
    if filename in LEETCODE_SLUG_OVERRIDES:
        return LEETCODE_SLUG_OVERRIDES[filename]
    return filename.replace(".py", "").replace("_", "-")


def build_issue_body(problem):
    """Build the issue body markdown for a problem."""
    category_display = problem["category"].replace("_", " ").title()
    filepath = problem["filepath"]
    slug = get_leetcode_slug(problem["filename"])

    body = f"""## LeetCode {problem['number']}: {problem['title']}

**Category:** {category_display}
**Difficulty:** See [LeetCode](https://leetcode.com/problems/{slug}/)
**Solution File:** `{filepath}`
**Test File:** `tests/test_{problem['filename']}`

### Problem Description

{problem['description']}

### Tasks

- [ ] Implement the solution in `{filepath}`
- [ ] Ensure all test cases pass
- [ ] Analyze time complexity
- [ ] Analyze space complexity
"""
    return body


def create_github_issue(token, repo, title, body, labels):
    """Create a GitHub issue using the REST API."""
    url = f"https://api.github.com/repos/{repo}/issues"
    data = json.dumps({"title": title, "body": body, "labels": labels}).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["number"], result["html_url"]
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"  Error creating issue: {e.code} - {error_body}")
        return None, None


def ensure_labels_exist(token, repo, labels):
    """Ensure all required labels exist in the repository."""
    label_colors = {
        "array": "7057ff",
        "binary": "008672",
        "dynamic programming": "d73a4a",
        "graph": "0075ca",
        "heap": "cfd3d7",
        "interval": "a2eeef",
        "linked list": "e4e669",
        "matrix": "d876e3",
        "string": "f9d0c4",
        "tree": "0e8a16",
        "blind-75": "fbca04",
    }

    for label, color in label_colors.items():
        if label not in labels:
            continue
        url = f"https://api.github.com/repos/{repo}/labels"
        data = json.dumps(
            {"name": label, "color": color, "description": f"Blind 75 - {label.title()} problems"}
        ).encode("utf-8")

        req = urllib.request.Request(
            url,
            data=data,
            headers={
                "Authorization": f"token {token}",
                "Accept": "application/vnd.github.v3+json",
                "Content-Type": "application/json",
            },
            method="POST",
        )

        try:
            urllib.request.urlopen(req)
            print(f"  Created label: {label}")
        except urllib.error.HTTPError as e:
            if e.code == 422:
                pass  # Label already exists
            else:
                print(f"  Warning: Could not create label '{label}': {e.code}")


def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")

    if not token:
        print("Error: GITHUB_TOKEN environment variable is required")
        sys.exit(1)
    if not repo:
        print("Error: GITHUB_REPOSITORY environment variable is required")
        sys.exit(1)

    print(f"Repository: {repo}")
    print("Extracting problems from source files...")

    problems = extract_problems()
    print(f"Found {len(problems)} problems\n")

    if len(problems) != 75:
        print(f"Error: Expected 75 problems, found {len(problems)}")
        sys.exit(1)

    # Collect all unique labels
    all_labels = {"blind-75"}
    for p in problems:
        all_labels.add(p["category"].replace("_", " "))

    print("Ensuring labels exist...")
    ensure_labels_exist(token, repo, all_labels)
    print()

    # Create issues
    created = 0
    for i, problem in enumerate(problems, 1):
        category_label = problem["category"].replace("_", " ")
        title = f"LeetCode {problem['number']}: {problem['title']}"
        body = build_issue_body(problem)
        labels = ["blind-75", category_label]

        print(f"[{i}/75] Creating issue: {title}")
        issue_num, issue_url = create_github_issue(token, repo, title, body, labels)

        if issue_num:
            print(f"  Created: #{issue_num} - {issue_url}")
            created += 1
        else:
            print(f"  Failed to create issue")

        # Rate limiting - GitHub allows 30 requests per minute for issue creation
        if i % 25 == 0:
            print("  Pausing for rate limiting...")
            time.sleep(10)
        else:
            time.sleep(1)

    print(f"\nDone! Created {created}/75 issues.")


if __name__ == "__main__":
    main()
