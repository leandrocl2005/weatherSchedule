from apscheduler.schedulers.background import BackgroundScheduler
from .data_manager import update_weather


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_weather, 'interval', minutes=2)
    scheduler.start()
