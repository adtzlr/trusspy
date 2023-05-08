# Changelog
All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.0.0] - 2023-05-08

### Changed
- Don't include the zero (undeformed) increment in the output of `Model.plot_movie()`.
- Enhance `ResultHandler.add_increment(analysis=None, extforces=None, lpf=None)`.

### Removed
- Remove Excel-based input files. This removes the `file`-argument of `Model`, all `add_..._matrix()`-related methods of handlers as well as all Excel-based tests.
- Remove PDF- and HTML-output conversions of Markdown-logfiles. This is considered as an external `pandoc`-task and is no more a part of TrussPy.
- Remove broken `increments` argument of `Model.plot_history()` and always plot all increments instead.

### Fixed
- The result of the first increment contained the displacements of the first solution. However, the very first item of the results should contain the undeformed model.
- For `Model.plot_model(inc=0, contour="force")`, the contour-plot is disabled for the first increment.
- Fix the plot force label shown in `Model.plot_model()`: For the first (zero) increment, the initial external loads are shown. For all other increments, the external loads scaled by the load-proportionality-factor (LPF) are shown.
- Fix `Model.plot_movie(incs="all")`: Get number of increments from length of list of results

## [2.0.0] - 2023-05-03

### Changed
- Change default `force_scale=1.0` (from `0.5`) in `Model.plot_model()` and `Model.plot_movie()`.
- Set `title="UNDEFORMED"` if increment zero is passed to `Model.plot_model(inc=0)`.
- If `inc < 0` in `Model.plot_model()`, evaluate the increment to `inc = len(Model.Results.R) - inc`.

### Removed
- Remove the `config`-argument in `Model.plot_model()` (plot the deformed configuration if `inc > 0`, show the undeformed configuration with `lpf=1` if `inc==0`).
- Don't support `Model.plot_model(force_scale=None)`, must be `float`.

## [1.0.4] - 2023-05-03

### Changed
- Change default config from `Model.plot_model(config="both")` to `Model.plot_model(config="deformed")`. 
- Change default config from `Model.plot_movie(config="both")` to `Model.plot_movie(config="deformed")`. 
- Pass optional keyword-arguments (like `fps` or `duration`) to the underlying `png_to_gif(**kwargs)`-call inside `Model.plot_movie(**kwargs)`.

### Fixed
- Fix overlapping title and text in `Model.plot_model()` and `Model.plot_movie()`: Change relative position of the force-scale text box in `tools.plot_utilities.p_model()` from `ax.text2D(0.3, 1.05, verticalalignment="top")` to `ax.text2D(0.5, 0.95, verticalalignment="top", horizontalalignment="center")`. Now identical arguments for calling 2D (`ax.text()`) and 3D (`ax.text2D()`) are used.
- Don't pass `fps` to `imagio.mimwrite()` (use the default settings instead).

## [1.0.3] - 2023-03-15

### Changed
- Simplify the source code: Remove unused lines of code, To-Do's from function or class docstrings, unify file docstrings. Trim the header printed by `Model`.
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
