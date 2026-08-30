# Expected review families

This fixture intentionally contains review defects. Do not deploy it.

Deterministic targets include a hardcoded secret, mutable default argument,
identity comparison with an integer, bare/silent exception handling, `eval`,
blocking sleep in async code, missing HTTP timeout, shell injection, and debug
printing.

Semantic targets include a declared non-null return that can be `None`, update
success for a missing record, first-page pagination skipping records, an
incomplete cache key, authorization accepting any role, exceptions converted
to successful responses, and weak tests that do not verify behavior.

Clean controls include Pydantic validation, `default_factory`, FastAPI
dependency injection, an `httpx.AsyncClient` context manager, `pytest.raises`,
and a correctly awaited async test.
