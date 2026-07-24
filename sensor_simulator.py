import random
import time

from aquaguard_agent import run_telemetry


customer_id = "CUST101"
phone = "+911234567890"


while True:

    tds = random.randint(100,700)
    filter_life = random.randint(1,100)

    print("\n📡 New Sensor Data")
    print("TDS:", tds)
    print("Filter:", filter_life,"%")

    run_telemetry(
        tds,
        filter_life,
        customer_id,
        phone
    )

    time.sleep(10)