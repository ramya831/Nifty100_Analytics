import threading
import requests
import time

URL = "http://127.0.0.1:8000/api/v1/screener/screener/"

times = []


def call_api():
    start = time.time()
    requests.get(URL)
    end = time.time()
    times.append(end - start)


threads = []

overall_start = time.time()

for _ in range(10):
    t = threading.Thread(target=call_api)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

overall_end = time.time()

print("=" * 40)
print("Concurrent Requests:", len(times))
print("Total Time:", round(overall_end - overall_start, 2), "seconds")
print("Average Response:", round(sum(times) / len(times), 3), "seconds")
print("=" * 40)