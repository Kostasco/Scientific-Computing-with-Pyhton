def add_time(start, duration, starting_day=None):
  """
  Adds a duration to a given start time and returns the new time.

  Parameters:
  - start (str): Start time in the format "HH:MM AM/PM".
  - duration (str): Duration in the format "HH:MM".
  - starting_day (str, optional): Starting day of the week. Defaults to None.

  Returns:
  - str: New time after adding the duration.
  """

  # Mapping weekdays to numbers
  week_days = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}

  # Splitting start time and duration
  start_time, midday_time = start.split(" ")
  start_hour, start_min = map(int, start_time.split(":"))
  duration_hour, duration_min = map(int, duration.split(":"))

  # Converting to 24-hour format if PM
  if midday_time == "PM":
      start_hour += 12

  # Calculating total hours and minutes
  total_min = (start_min + duration_min) % 60
  total_hour = start_hour + duration_hour + ((start_min + duration_min) // 60)

  # Calculating days and final hours for 12-hour format
  final_hour = (total_hour % 24) % 12
  if final_hour == 0:
      final_hour = 12

  # Determining AM/PM
  midday_time = "AM" if (total_hour % 24) <= 11 else "PM"

  # Formatting minutes
  final_min = str(total_min).zfill(2)  # Zeros padding for single digit minutes

  # Handling starting_day and day calculation
  if starting_day:
      total_days = total_hour // 24
      final_weekday = (week_days[starting_day.lower().capitalize()] + total_days) % 7
      final_day = list(week_days.keys())[list(week_days.values()).index(final_weekday)]
      if total_days == 0:
          return f"{final_hour}:{final_min} {midday_time}, {final_day}"
      elif total_days == 1:
          return f"{final_hour}:{final_min} {midday_time}, {final_day} (next day)"
      else:
          return f"{final_hour}:{final_min} {midday_time}, {final_day} ({total_days} days later)"
  else:
      if total_hour // 24 == 1:
          return f"{final_hour}:{final_min} {midday_time} (next day)"
      elif total_hour // 24 > 1:
          return f"{final_hour}:{final_min} {midday_time} ({total_hour // 24} days later)"
      else:
          return f"{final_hour}:{final_min} {midday_time}"
