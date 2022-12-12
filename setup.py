from setuptools import find_namespace_packages, setup

setup(
    name="cijoe",
    version="0.9.10",
    author="Simon A. F. Lund",
    author_email="os@safl.dk",
    url="https://github.com/refenv/cijoe",
    license="BSD",
    install_requires=[
        "jinja2",
        "paramiko",
        "pytest",
        "pytest-reportlog",
        "pyyaml",
        "requests",
        "scp",
        "setuptools>=60",
        "watchdog",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": ["cijoe=cijoe.cli.cli:main"],
        "pytest11": ["cijoe = cijoe.pytest_plugin.hooks_and_fixtures"],
    },
    include_package_data=True,
    package_data={
        "": ["*.html", "*.config", "*.perfreq", "*.workflow"],
    },
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src", include=["cijoe.*"]),
    zip_safe=False,
    options={"bdist_wheel": {"universal": True}},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
)
