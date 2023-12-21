import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "ultimate_frisbee_rules_rag"
AUTHOR = "JacobKaczmarek"
VERSION = "0.0.0"
AUTHOR_EMAIL="jacob_kaczmarek@outlook.com"

setuptools.setup(
    name=REPO_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="RAG app for ultimate frisbee rules",
    long_description=long_description,
    long_description_context="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={
        "Bug tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)