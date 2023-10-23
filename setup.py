import ast
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def generate_long_description():
    with open('README.md') as f:
        long_description = f.read()
        try:
            import pypandoc
            long_description = pypandoc.convert_text(
                long_description, 'rst', format='md')
        except ImportError:
            pass
        return long_description

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('sprucepy/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name="spruce.py",
    version=version,
    description="Sprucepy API 1.0 Wrapper",
    long_description=generate_long_description(),
    author="hunter87ff",
    author_email="hunter87@sprucebot.tech",
    license="MIT",
    url="http://github.com/hunter87ff/sprucepy",
    keywords=["Sprucepy", "api", "wrapper", "1.0"],
    include_package_data=True,
    packages=["spruce.py"],
    install_requires=[
        "requests",
    ],
    classifiers=(
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
)
