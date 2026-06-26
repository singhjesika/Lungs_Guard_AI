
import asyncio
from app.realtime.alert_system import AlertSystem
from app.config import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)
alert = AlertSystem()


async def monitor(stream):
    """Continuously read SpO2 from stream and alert on low values."""
    async for reading in stream:
        spo2 = reading.get("spo2")
        patient_id = reading.get("patient_id", "unknown")
        if spo2 is not None and spo2 < settings.ALERT_OXYGEN_THRESHOLD:
            await alert.trigger(
                patient_id=patient_id,
                message=f"LOW SpO2: {spo2}% (threshold: {settings.ALERT_OXYGEN_THRESHOLD}%)",
                severity="critical",
            )
        logger.debug(f"Patient {patient_id} SpO2: {spo2}")
