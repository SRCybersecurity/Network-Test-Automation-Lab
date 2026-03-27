import re

with open("ping.log") as f:
    data = f.read()

loss = re.search(r'(\d+)% packet loss', data)
loss_val = int(loss.group(1)) if loss else 100

if loss_val == 0:
    status = "PASS"
elif loss_val < 20:
    status = "WARNING"
else:
    status = "FAIL"

print(f"Packet Loss: {loss_val}% - {status}")
