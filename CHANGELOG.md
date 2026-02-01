# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.1] - 2026-02-01

### Fixed
- **CRITICAL**: Added initial migrations for core app (`apps/core/migrations/0001_initial.py`)
- **CRITICAL**: Created `static/css/` and `static/js/` directories to prevent warnings
- Fixed `OperationalError: no such table: core_userprofile` on first setup
- Fixed `.gitignore` to properly track static directory structure
- Fixed staticfiles warning about missing static directory

### Technical Details
This patch ensures the template works immediately after `git clone` without requiring manual `makemigrations`. The UserProfile table is now created automatically during initial `migrate`.

## [1.2.0] - 2026-02-01

### Fixed
- **CRITICAL**: Removed deprecated `default_app_config` from `apps/__init__.py` (incompatible with Django 4.0+)
- **CRITICAL**: Fixed signals.py with lazy import to prevent `AppRegistryNotReady` error
- Added support for both SQLite and PostgreSQL in settings.py with automatic detection
- Fixed database config with default empty values for SQLite compatibility
- Added root URL redirect to login page (fixes 404 on homepage)
- Updated .env.example with DB_ENGINE variable and examples for both databases

### Changed
- Database configuration now requires `DB_ENGINE` in .env
- SQLite no longer requires DB_USER/DB_PASS/DB_HOST/DB_PORT values

### Migration Guide v1.1.0 → v1.2.0
For existing projects using this template:

**SQLite (Development):**
```env
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
DB_USER=
DB_PASS=
DB_HOST=
DB_PORT=
```

**PostgreSQL (Production):**
```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASS=your_password
DB_HOST=localhost
DB_PORT=5432
```

## [1.1.0] - 2026-02-01

### Added
- Complete Django 5.0 application code
- Authentication system (login/register/logout with rate limiting)
- User profiles with role-based permissions (admin/editor/viewer)
- REST API with Django REST Framework
- Tailwind CSS + Alpine.js frontend (zero build required)
- Responsive templates (mobile-first design)
- Management commands (create_admin, seed_db)
- Security middleware and headers
- PostgreSQL configuration
- pytest test suite with examples
- Automated setup and deploy scripts
- CI/CD with GitHub Actions

## [1.0.0] - 2026-02-01

### Added
- Initial template structure
- Complete documentation (README, CONTRIBUTING, SECURITY, TEMPLATE_GUIDE)
- Requirements.txt with Django 5.0 dependencies
- .env.example configuration
- .gitignore for Python/Django projects
- MIT License
- AUTHORS.md and CHANGELOG.md
- Verification script

[1.2.1]: https://github.com/turiliffiu/demo_app/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/turiliffiu/demo_app/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/turiliffiu/demo_app/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/turiliffiu/demo_app/releases/tag/v1.0.0
