import subprocess
import sys
import time
import logging
from logging.handlers import RotatingFileHandler

# ==================== CONFIGURATION ====================
SERVICE_NAME = "nginx"  # Change this to your target service (e.g., docker, sshd)
CHECK_INTERVAL = 10      # How often to check the service status (in seconds)
MAX_RESTART_ATTEMPTS = 3 # Stop trying after this many consecutive failures
COOLDOWN_PERIOD = 5      # Seconds to wait between restart attempts
LOG_FILE = "service_watchdog.log"
# =======================================================

# Configure robust logging to track script actions and service state
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        RotatingFileHandler(LOG_FILE, maxBytes=1024*1024, backupCount=3),
        logging.StreamHandler(sys.stdout)
    ]
)

def is_service_running(service_name):
    """
    Checks if a systemd service is active and running.
    Returns True if running, False otherwise.
    """
    try:
        # systemctl is-active returns 0 if active, non-zero if inactive/failed
        result = subprocess.run(
            ["systemctl", "is-active", service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        return result.stdout.strip() == "active"
    except FileNotFoundError:
        logging.critical("Error: 'systemctl' command not found. This script requires a systemd Linux environment.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error checking service status: {e}")
        return False

def restart_service(service_name):
    """
    Attempts to restart the specified systemd service.
    Returns True if successful, False if it failed.
    """
    try:
        logging.info(f"Attempting to restart service: {service_name}...")
        result = subprocess.run(
            ["systemctl", "restart", service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            return True
        else:
            logging.error(f"Failed to restart {service_name}. Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        logging.error(f"Exception occurred while restarting service: {e}")
        return False

def monitor_loop():
    logging.info(f"Watchdog started. Monitoring service: '{SERVICE_NAME}' every {CHECK_INTERVAL} seconds.")
    restart_counter = 0

    while True:
        if is_service_running(SERVICE_NAME):
            # If the service is healthy, ensure our restart counter resets
            if restart_counter > 0:
                logging.info(f"Service '{SERVICE_NAME}' has successfully stabilized.")
                restart_counter = 0
        else:
            logging.warning(f"CRITICAL: Service '{SERVICE_NAME}' is NOT running!")
            
            if restart_counter < MAX_RESTART_ATTEMPTS:
                restart_counter += 1
                logging.info(f"Restart attempt {restart_counter} of {MAX_RESTART_ATTEMPTS}...")
                
                if restart_service(SERVICE_NAME):
                    # Give it a moment to initialize before checking status again
                    time.sleep(COOLDOWN_PERIOD)
                    if is_service_running(SERVICE_NAME):
                        logging.info(f"Success! Service '{SERVICE_NAME}' was restarted successfully.")
                        restart_counter = 0
                    else:
                        logging.error(f"Service '{SERVICE_NAME}' accepted restart command but crashed immediately.")
                else:
                    time.sleep(COOLDOWN_PERIOD)
            else:
                logging.critical(
                    f"Maximum restart attempts ({MAX_RESTART_ATTEMPTS}) reached for '{SERVICE_NAME}'. "
                    "Manual intervention required. Halting automatic restart loop to prevent system thrashing."
                )
                # In a real environment, you'd trigger a Slack/Discord webhook or Email alert here!
                
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        monitor_loop()
    except KeyboardInterrupt:
        logging.info("Watchdog script stopped manually by user.")
        sys.exit(0)
