# Worksheet 12a – Log Summary

`summary.py` reads a log file and prints:

- the total number of lines
- the top 5 most common values of one field (the service name, e.g. `[auth-service]`), counted with `collections.Counter`

It expects lines in this format:

```
2026-10-12 08:01:13 [INFO] [auth-service] [req-39999] Request processed successfully
```

## How to run

```
python3 summary.py <logfile>
```

Example output:

```
Total lines: 400
Top 5:
[payment-service] 71
[auth-service] 70
...
```

## Note

Log files are **not** committed (see `.gitignore`), because logs captured from a real machine can contain identifying information.
