# Contributing to SimpleQR

Contributions are welcome! Here's how to get started.

## Setup

```bash
git clone https://github.com/Flying-Bolt/SimpleQR.git
cd SimpleQR
pip install -r requirements.txt
python SimpleQR.py
```

## Reporting Bugs

Use the **Bug Report** issue template on GitHub. Include:
- OS and Python version
- Steps to reproduce
- Expected vs. actual behaviour

## Suggesting Features

Use the **Feature Request** issue template. Describe the use case clearly.

## Pull Requests

1. Fork the repository and create a feature branch from `master`
2. Keep changes focused – one feature or fix per PR
3. Test manually before submitting
4. Update `README.md` if the user-facing behaviour changes
5. Describe what and why in the PR description

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Keep the app self-contained (single file, no extra assets)
- No external dependencies beyond `qrcode[pil]` and `Pillow`
