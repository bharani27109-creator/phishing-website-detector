# Feature extraction from URLs
def extract_features(url):
    return {
        "url_length": len(url),
        "has_https": int(url.startswith("https")),
        "num_dots": url.count("."),
        "has_at_symbol": int("@" in url),
    }