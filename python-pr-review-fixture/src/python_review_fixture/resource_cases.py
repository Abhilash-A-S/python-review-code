from pathlib import Path


def load_report(path: Path) -> str:
    report = path.open("r", encoding="utf-8")
    return report.read()


def load_report_safely(path: Path) -> str:
    with path.open("r", encoding="utf-8") as report:
        return report.read()
