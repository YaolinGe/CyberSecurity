# Notes for cybersecurity
# I have updated the video for the final project. 

## Securing accounts

## Securing data

## Securing systems
- WPA (wifi protected access (WPA))
- HTTP (machine-in-the-middle attacks) if only http is used.
- HTML
- Packet sniffing
- Cookies
- Session hijacking
- HTTPS (SSL, TLS, X.509, CA(signature hashing))
- SSL stripping
- HSTS (HTTP Strict Transport Security)
- VPN
- SSH
- Port, 80(HTTP), 443(HTTPS), 22(SSH)
- Port scanning
- Penetration testing (Pen-testing)
- Ethical hacking (red team: attack, blue team: defend)
- Firewall (IP adress, deep packet inspection, proxy, url rewritting)
- Malware (virus, worm, botnet, denial-of-service attack (DOS attack), distributed denial-of-service attack (DDoS))
- Antivirus (automatic updates)
- Zero-day attack

## Securing software
- Phishing
- Code injection (cross-site scripting (xss), reflected attack, stored attack, character escapes)
- `Content-Security-Policy: script-src www.example.com` to ignore any inline javascript code.
- `Content-Security-Policy: style-src www.example.com` to ignore any inline CSS code.
- SQL injection
- Prepared statements
- Command injection (system, eval)
- Client-side validation / Server-side validation
- Cross-site request forgery (CSRF)
- GET (`<img src="someurl">` might download or buy stuff for the user even though the user has not done anything since it downloads the images automatically.)
- POST (javascript can automatically submit it in the backend)
- Open Worldwide Application Security Project (OWASP)
- Arbitrary code execution (ACE)
- Remote code execution (RCE)
- Buffer overflow
- Stack overflow
- Cracking
- Reverse engineering
- Open-source software
- Closed-source software
- Bug bounty
- CVSS (common vulnerability scoring system)
- CVE (common vulnerabilities and exposures)
- EPSS (exploit prediction scoring system)
- KEV (known exploited vulnerabilities)

## Preserving privacy
- Logs (servers log user activities)
- `<referrer content=none>` to not send any referrer.
- `Referrer-Policy: no-referrer` to not send any original website.
- Fingerprinting: User-Agent (OS, Browser)
- No SMS validation
- Tracking cookies have time duration that is allowed to track the user.
- Tracking parameters
- Third-party cookies
- DNS over HTTPS (DoH)
- DNS over TLS (DoT)
