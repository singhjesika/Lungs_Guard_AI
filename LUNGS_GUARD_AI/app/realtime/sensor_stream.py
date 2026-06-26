"""
Sensor stream — provides async generator for live or simulated sensor data.
"""
import asyncio
import random


async def mock_sensor_stream(patient_id: str = "P001", interval: float = 1.0):
    """Yield simulated SpO2 readings every `interval` seconds."""
    while True:
        yield {
            "patient_id": patient_id,
            "spo2": round(random.uniform(91.0, 99.0), 1),
            "heart_rate": random.randint(60, 100),
        }
        await asyncio.sleep(interval)
