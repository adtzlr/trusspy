# Changelog
All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Simplify the source code: Remove unused lines of code, To-Do's from function or class docstrings, unify file docstrings.
- Build HTML and PDF logfiles only if `Settings.logpdf=True` (Pandoc and LaTeX must be installed). Otherwise, only the Markdown logfile `analysis.md` for `Model(logfile=True)` is created (no Pandoc install required).

## [1.0.2] - 2023-03-13

### Added
- Added MyBinder badge and config file `environment.yml`.

### Fixed
- Fixed format string in `Model`.

## [1.0.1] - 2023-03-11

### Fixed
- Added missing PyPI API token to deploy the wheel to PyPI.

## [1.0.0] - 2023-03-11

### Added
- Start keeping a Changelog.