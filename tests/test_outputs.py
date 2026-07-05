"""Verify /app/report.json against the instruction's success criteria.

Expected values are computed from the fixed input in environment/access.log:
  - 6 request lines                            -> total_requests == 6
  - IPs {192.168.0.1, 192.168.0.2, 10.0.0.5}   -> unique_ips == 3
  - /index.html x3, /about.html x2, /api/login x1 -> top_path == "/index.html"

Each test maps 1:1 to a numbered success criterion in instruction.md.
"""
import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load_report():
    assert REPORT.exists(), "no /app/report.json was produced"
    assert REPORT.stat().st_size > 0, "/app/report.json is empty"
    with REPORT.open() as f:
        data = json.load(f)  # invalid JSON fails the test here
    return data


def test_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and is a single valid JSON object."""
    assert isinstance(_load_report(), dict)


def test_total_requests():
    """Criterion 2: total_requests equals the number of request lines (6)."""
    assert _load_report().get("total_requests") == 6


def test_unique_ips():
    """Criterion 3: unique_ips equals the number of distinct client IPs (3)."""
    assert _load_report().get("unique_ips") == 3


def test_top_path():
    """Criterion 4: top_path equals the most frequently requested path (/index.html)."""
    assert _load_report().get("top_path") == "/index.html"
