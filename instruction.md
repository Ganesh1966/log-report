An Apache-style access log is waiting at /app/access.log. Read it and write a short
JSON summary of the traffic to /app/report.json.

The report must be a single JSON object with exactly these three keys:

- total_requests: the total number of request lines in the log.
- unique_ips: the number of distinct client IP addresses (the first field on each line).
- top_path: the path that was requested most often (the path portion of the request line, e.g. /index.html).

For example: {"total_requests": 42, "unique_ips": 7, "top_path": "/index.html"}

Your work is judged on:

1. /app/report.json exists and contains a single valid JSON object.
2. total_requests equals the number of request lines in /app/access.log.
3. unique_ips equals the number of distinct client IP addresses in the log.
4. top_path equals the most frequently requested path in the log.
