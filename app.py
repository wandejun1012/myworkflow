import redis
import time

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

# 等待 redis 就绪（CI 中很常见）
for i in range(5):
    try:
        r.ping()
        break
    except redis.exceptions.ConnectionError:
        time.sleep(1)

r.set("ci_test", "hello_github_actions")
value = r.get("ci_test")

print("Redis value:", value)

if value != "hello_github_actions":
    raise RuntimeError("Redis test failed")

print("Redis test passed")
