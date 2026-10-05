#!/usr/bin/env python3
"""Call the GitHub REST API with the stored custom.github credential."""
import json
import sys
import urllib.request

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import (
    add_surrogate_to_request,
    read_json_response,
)

ALLOWED = ["api.github.com"]
CRED = "custom.github"


def api(path, method="GET", data=None):
    url = "https://api.github.com" + path
    body = None
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "muse-agent",
    }
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    add_surrogate_to_request(req, CRED, allowed_hosts=ALLOWED)
    with urllib.request.urlopen(req) as resp:
        return read_json_response(resp)


def main():
    if len(sys.argv) < 2:
        print("usage: gh_api.py <path> [METHOD] [json-data]", file=sys.stderr)
        sys.exit(2)
    path = sys.argv[1]
    method = sys.argv[2] if len(sys.argv) > 2 else "GET"
    data = json.loads(sys.argv[3]) if len(sys.argv) > 3 else None
    try:
        print(json.dumps(api(path, method, data), ensure_ascii=False, indent=2))
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
