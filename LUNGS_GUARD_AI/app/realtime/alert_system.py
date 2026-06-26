"""Alert system — sends notifications for critical readings."""
import asyncio
from app.utils.logger import get_logger

logger = get_logger(__name__)


class AlertSystem:
    async def trigger(self, patient_id: str, message: str, severity: str = "warning"):
        logger.warning(f"[ALERT][{severity.upper()}] Patient {patient_id}: {message}")
        # Extend: email, SMS, push notification here
        await asyncio.sleep(0)  # non-blocking placeholder
