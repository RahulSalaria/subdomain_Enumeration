# 🔍 Subdomain Enumeration Tool using Python and Threading

### 🚀 Project Overview
This project is a **Python-based Subdomain Enumeration Tool** that automates the process of discovering active subdomains of a target domain (e.g., `youtube.com`).  
It uses **HTTP requests** and **multithreading** to check multiple subdomains concurrently, improving efficiency and speed.

Subdomain enumeration is an important step in **cybersecurity reconnaissance**, helping security professionals identify hidden assets and potential vulnerabilities.

---

### 🎯 Objective
To build a Python script that:
- Reads a list of potential subdomains from a file.
- Checks which subdomains are active (reachable via HTTP).
- Uses multithreading to make the process faster.
- Saves the discovered subdomains to an output file.

---

### ⚙️ How It Works

1. **Input Handling**
   - The script reads subdomains from a file named `subdomain.txt`.
   - Example entries: `www`, `mail`, `admin`, `api`, etc.

2. **URL Construction**
   - For each subdomain, it constructs a URL like:
     ```
     http://subdomain.youtube.com
     ```

3. **Checking for Active Subdomains**
   - It sends an HTTP request to each constructed URL.
   - If a connection is successful (status code < 400), the subdomain is considered **active**.

4. **Multithreading for Speed**
   - Multiple subdomains are checked at the same time using Python’s `threading` module.
   - A `threading.Lock()` ensures threads write results safely without overlap.

5. **Result Storage**
   - All active subdomains are saved in a file called `discovered_subdomains.txt`.

---

### 🧠 Key Concepts Learned
- **DNS & Subdomains:** Understanding how domains and subdomains work in the web hierarchy.  
- **HTTP Requests:** Using Python’s `requests` library to send and handle web requests.  
- **File I/O:** Reading from and writing to text files in Python.  
- **Multithreading:** Running multiple checks in parallel to improve efficiency.  
- **Error Handling:** Managing failed requests safely with try-except blocks.

---


