import subprocess
import time
import requests
import os
import pytest

@pytest.fixture
def report_dir():
    report_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(report_dir, exist_ok=True)
    return report_dir

def test_locust(report_dir):
    # запускаем locust
    locust_process = subprocess.Popen(["locust", "-f", "locustfile.py"])
    time.sleep(5)
    locust_process.poll()
    assert locust_process.returncode is None
    response = requests.get("http://localhost:8089")
    assert response.status_code == 200
    # отправляем запрос пост с параметрами
    start_test_url = "http://localhost:8089/swarm"
    data = {"user_count": 10, "spawn_rate": 1}
    response = requests.post(start_test_url, data=data)
    assert response.status_code == 200
    time.sleep(5)
    # проверяем статус теста
    stats_url = "http://localhost:8089/stats/requests"
    response = requests.get(stats_url)
    assert response.status_code == 200
    stats = response.json()
    print(stats)
    # создаем отчет
    report_file = f"{report_dir}/locust_report.html"
    with open(report_file, "w") as f:
        f.write("<html><body>")
        f.write("<h1>Locust Test Report</h1>")
        f.write(f"<pre>{stats}</pre>")
        f.write("</body></html>")
    # остановка теста
    locust_process.terminate()


