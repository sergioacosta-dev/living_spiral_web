# Security Policy

## Reporting a Vulnerability

Please **do not** open a public GitHub issue for security vulnerabilities.

**Preferred:** Use GitHub's private vulnerability reporting for this repo:
[Report a vulnerability](../../security/advisories/new) (Security tab → "Report a vulnerability").

**Alternative:** Email sergiogabrielacosta7@gmail.com with the subject line
`SECURITY: living_spiral_web`.

You should receive an acknowledgment within 5 business days.

## What to Include

To help triage quickly, please include:

- A clear description of the vulnerability and its potential impact
- Steps to reproduce, or a minimal proof-of-concept
- Affected file(s), endpoint(s), or component(s)
- Any relevant logs, screenshots, or request/response captures
- Your assessment of severity (if you have one)

## Scope

This covers the static frontend and the Python serverless API on Vercel. Note: this project is on hold (deployed, no active development) — fixes may be delayed.

This project has a live deployment at https://livingspiralweb.vercel.app. Reports about that deployment are in scope.

**Out of scope:**
- Vulnerabilities requiring physical access to a device
- Social engineering or phishing against the maintainer
- Denial-of-service testing (please report the theoretical issue instead of running it)
- Issues in third-party dependencies (report upstream, but let me know so I can track/patch)

## This Is a Personal Project

This is a solo-maintained personal/portfolio project, not a commercial product with an SLA.
I'll do my best to respond promptly and fix confirmed issues, but there's no guaranteed
response time or bug bounty. Credit will be given in the fix commit/changelog unless you
prefer to stay anonymous.
