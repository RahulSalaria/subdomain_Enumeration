import requests
import threading

domain = "youtube.com"

discovered_subdomains = []

lock = threading.Lock()

with open("subdomain.txt") as f:
    subdomains = f.read().splitlines()  # Reads each line as an item in a list

print("Loaded subdomains:", subdomains)

def check_subdomain(subdomain):
    url = f"http://{subdomain}.{domain}"  # Build the full URL
    try:
        response = requests.get(url, timeout=3)  # Try to connect
        if response.status_code < 400:  # Status < 400 usually means success
            with lock:  # Ensure thread-safe writing
                print(f"[+] Active: {url}")
                discovered_subdomains.append(url)
    except requests.ConnectionError:
        pass  # Ignore unreachable subdomains
    except requests.exceptions.RequestException as e:
        pass  # Ignore other request errors

threads = []

for sub in subdomains:
    t = threading.Thread(target=check_subdomain, args=(sub,))
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

with open("discovered_subdomains.txt", "w") as f:
    for url in discovered_subdomains:
        f.write(url + "\n")

print("Saved discovered subdomains to discovered_subdomains.txt")
