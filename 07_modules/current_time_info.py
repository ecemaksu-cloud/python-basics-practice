# Display current date and time information

import time

current_time = time.localtime()

print("Year:", current_time.tm_year)
print("Hour:", current_time.tm_hour)

# Other available attributes:
# tm_mon  -> month
# tm_mday -> day
# tm_hour -> hour
# tm_min  -> minute
# tm_sec  -> second
