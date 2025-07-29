from setuptools import setup, find_packages

setup(
    name="journalvetting",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click",
        "PyMuPDF",
        "langchain",
        "openai",
        "python-dotenv",
        "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "journalvet=journal_vetting.cli:cli",
        ]
    }
)
