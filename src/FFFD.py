import sys
from datetime import datetime, timedelta

logfile = f"/home/terrapin/FFFDlogs/FFFD_log_run_{datetime.today().strftime('%Y-%m-%d-%H-%M-%S')}"

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename = logfile, level = logging.DEBUG)


import pandas as pd

yesterday = (datetime.today() - timedelta(days = 1)).strftime('%Y-%m-%d')
csv_filename = f"/home/terrapin/FFFD_Data/FFFD_{yesterday}.csv"

logger.debug(f'Beginning download of data for {yesterday}')
try:
    tabs = pd.read_html('https://eservices.fairfield.ca.gov/FireLog/')
    tabs[1].to_csv(csv_filename)
    logger.info(f'The script has executed Successfully for Firelog {yesterday}')
except Exception as e:
    logger.error(f'an error has occured when fetching the table: {e}')
    sys.exit(1)
