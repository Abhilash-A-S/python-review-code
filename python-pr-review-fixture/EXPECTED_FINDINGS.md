# Expected findings

This fixture contains **28 intended findings**. Closely equivalent rule names
are acceptable, but each root cause should appear once at its production or
test source line.

With reviewer build 1027, **15 findings are expected from deterministic
analysis**. The other 13 are semantic stress targets; record any missed or
rejected target before expanding the Python capability family.

## Plain Python and security

1. `plain_cases.py`: hardcoded production API secret.
2. `plain_cases.py`: mutable list default reused between calls.
3. `plain_cases.py`: value comparison uses `is` with a typed integer.
4. `plain_cases.py`: bare exception silently ignores parsing failure.
5. `plain_cases.py`: `eval` executes a runtime expression.
6. `plain_cases.py`: shell-enabled subprocess interpolates external input.
7. `plain_cases.py`: user-controlled path is joined and read without boundary validation.
8. `plain_cases.py`: untrusted pickle data is deserialized.
9. `plain_cases.py`: unsafe YAML loader can construct arbitrary objects.
10. `plain_cases.py`: MD5 is used for a security token.

## Async and resource lifecycle

11. `async_cases.py`: blocking `time.sleep` inside an async function.
12. `async_cases.py`: aiohttp response/client resource is not context-managed or closed.
13. `async_cases.py`: background task is created and discarded without lifecycle/error ownership.
14. `resource_cases.py`: opened file is returned/read without deterministic closure.

## Flask and Django-style boundaries

15. `flask_app.py`: SQL is constructed from a request parameter.
16. `flask_app.py`: authentication trusts a user-supplied role header.
17. `flask_app.py`: internal exception details are returned to the client.
18. `django_service.py`: raw SQL interpolates a user-supplied email value.
19. `django_service.py`: broad exception converts a failed update into success.

## SQLAlchemy/data correctness

20. `database_cases.py`: SQLAlchemy `text()` query interpolates external input.
21. `database_cases.py`: transaction exception is swallowed without rollback/propagation.
22. `database_cases.py`: nullable query result violates a non-null return contract.
23. `database_cases.py`: update result is ignored and success is always returned.
24. `database_cases.py`: one-based pagination skips the first page.
25. `database_cases.py`: tenant filter is missing from the cache key.

## Tests

26. `test_flask_app.py`: test checks only HTTP status.
27. `test_database_cases.py`: pagination test checks only page metadata.
28. `test_database_cases.py`: missing-record update test accepts success.

## Clean controls that must not produce findings

- `safe_controls.py`: `default_factory`, equality comparison, specific exception,
  `secrets.token_urlsafe`, safe YAML loading, resolved path boundary check, and
  parameterized SQL.
- `async_cases.py`: awaited `asyncio.sleep` and context-managed aiohttp client.
- Tests using `pytest.raises`, response-body assertions, and awaited async code.
