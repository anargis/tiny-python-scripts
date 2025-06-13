import requests

def scan_cms(url):
    try:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        r = requests.get(url, timeout=5)
        text = r.text.lower()
        headers = {k.lower(): v.lower() for k, v in r.headers.items()}

        if r.status_code != 200:
            print("Site not reachable, status code:", r.status_code)
            return False, False, False

        is_moodle = (
            "moodle" in text or
            "moodle" in headers.get("x-powered-by", "") or
            "/theme/" in text or
            "mod_assign" in text or
            "moodle-enrol" in text or
            ("login/index.php" in text and "username" in text and "password" in text)
        )

        is_wordpress = (
            ("wp-content" in text or "wp-includes" in text) and not is_moodle
        ) or (
            "wordpress" in headers.get("x-powered-by", "") and not is_moodle
        )

        is_joomla = (
            "joomla" in text or
            "joomla" in headers.get("x-content-managed-by", "")
        )

        return is_wordpress, is_joomla, is_moodle

    except Exception as e:
        print("Error:", e)
        return False, False, False

url = input("Enter site URL (e.g domain.gr): ")
is_wordpress, is_joomla, is_moodle = scan_cms(url)

if not any([is_wordpress, is_joomla, is_moodle]):
    print("No CMS detected.")
else:
    print("CMS Detected:")
    if is_wordpress:
        print("WordPress detected.")
    if is_joomla:
        print("Joomla detected.")
    if is_moodle:
        print("Moodle detected.")
