import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    # 1. URL Length
    features.append(len(url))

    # 2. Having @ symbol
    features.append(1 if "@" in url else 0)

    # 3. Having - symbol
    features.append(1 if "-" in url else 0)

    # 4. Count dots
    features.append(url.count("."))

    # 5. HTTPS
    features.append(1 if "https" in url else 0)

    # 6. Count digits
    features.append(sum(c.isdigit() for c in url))

    # 7. URL path length
    path = urlparse(url).path
    features.append(len(path))

    # 8. Suspicious words
    suspicious_words = ["login", "secure", "bank", "update", "free"]
    features.append(1 if any(word in url.lower() for word in suspicious_words) else 0)

    # 9. Count special characters
    features.append(len(re.findall(r"[?=&]", url)))

    # 10. Subdomain count
    domain = urlparse(url).netloc
    features.append(domain.count("."))

    # 🔥 IMPORTANT: Pad to 30 features
    while len(features) < 30:
        features.append(0)

    return features