from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in kenyan_payroll_reports/__init__.py
from kenyan_payroll_reports import __version__ as version

setup(
	name="kenyan_payroll_reports",
	version=version,
	description="Kenyan Payroll Report App",
	author="Navari",
	author_email="solutions@navari.co.ke",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
