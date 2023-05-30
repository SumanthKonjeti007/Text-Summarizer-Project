import setuptools

#Reading your README.md file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "SumanthKonjeti007"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "sumanth.konjeti05@gmail.com"

#It looks for Constructor file "__init__.py" from every folder and it will install as my local package.
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)