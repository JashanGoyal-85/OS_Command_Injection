# Assignment 3 — OS Command Injection Demo
**Variant:** In-band (command output returned to user)  
**Backend language:** C++  &nbsp;|&nbsp; **Web server:** Python / Flask

---

## Project structure

```
Assignment 3/
├── ping_vuln.cpp      ← VULNERABLE C++ program  (uses system())
├── ping_safe.cpp      ← SECURE C++ program       (uses execvp() + allow-list)
├── ping_vuln          ← compiled binary (auto-built, see below)
├── ping_safe          ← compiled binary (auto-built, see below)
├── app.py             ← Flask web server (calls the C++ binaries)
├── index.html         ← Single-page UI
└── requirements.txt
```

---

## How to run

```bash
# 1. Compile C++ binaries (one-time)
g++ -std=c++17 -o ping_vuln ping_vuln.cpp
g++ -std=c++17 -o ping_safe ping_safe.cpp

# 2. Install Flask
pip install -r requirements.txt

# 3. Start server
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

---

## What to demo (video checklist)

| Step | What to do |
|------|-----------|
| (a) Vulnerable implementation | Show `ping_vuln.cpp` — the `system(cmd)` line |
| (b) Working exploit | Enter `127.0.0.1; whoami` in the **Unsafe** box — see injected command run |
| (c) Root cause | `system()` passes a string to `/bin/sh -c`, which evaluates `;` as a command separator |
| (d) Mitigation | Same payload in the **Safe** box → **BLOCKED** by allow-list in `ping_safe.cpp` |
| (e) Other mitigations | Explain the theory card on the page |

---

## Ownership declaration

| Member name | Roll number | Category | Variant implemented |
|-------------|-------------|----------|---------------------|
|Jashan Goyal | IIT2024223  | OS Command Injection | In-band (output returned) |
