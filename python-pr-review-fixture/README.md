# Universal Python PR-review stress fixture

This repository intentionally contains insecure and incorrect code. Do not
deploy or reuse the defective implementations.

## Usage

1. Keep `main` as an empty/clean repository baseline.
2. Copy this fixture into a feature branch.
3. Commit and open a PR against `main`.
4. Run the Intelligent PR Reviewer in dry-run mode.
5. Compare the final findings with `EXPECTED_FINDINGS.md`.

The reviewer should comment only on changed lines. Metadata, this README, and
the expected-findings document should not consume semantic LLM review calls.
