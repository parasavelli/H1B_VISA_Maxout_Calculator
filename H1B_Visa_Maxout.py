"""
H1B VISA MAX OUT CALCULATOR
"""

import datetime

entry_exits = []
total_days_outside = 0

def collect_entry_exits():
  """
  """
  global entry_exits
  more_flag = 'y'
  while more_flag not in ['N', 'n']:
    dt = input("Enter the ENTRY or EXIT date (MM/DD/YYYY): ")
    valid = validate_date(dt)
    if not valid:
      print("Please enter a valid ENTRY or EXIT date.")
      continue
    entry_exits.append(dt)
    more_flag = input("You want to enter more dates (Y/N)? ")
  entry_exits = sorted(entry_exits, key=lambda x: datetime.datetime.strptime(x, '%m/%d/%Y'))

def validate_date(date_text):
  """
  """
  try:
    datetime.datetime.strptime(date_text, '%m/%d/%Y')
  except ValueError:
    print("Incorrect date format, should be MM/DD/YYYY")
    return False
  return True

def no_of_days_outside():
  """
  """
  global total_days_outside
  for ind in range(len(entry_exits)-1)[1::2]:
    exit_dt_obj = datetime.datetime.strptime(entry_exits[ind], "%m/%d/%Y")
    entry_dt_obj = datetime.datetime.strptime(entry_exits[ind+1], "%m/%d/%Y")
    days = (entry_dt_obj - exit_dt_obj).days
    total_days_outside += days
  print("Total number of days outside country: ", total_days_outside)

def get_maxout_date():
  entry_date = datetime.datetime.strptime(entry_exits[0], "%m/%d/%Y")
  orig_max_out_date = entry_date.replace(year=entry_date.year+6)
  print("ORIGINAL MAX OUT DATE: ", orig_max_out_date.strftime("%m/%d/%Y"))
  new_max_out_date = orig_max_out_date + datetime.timedelta(days=total_days_outside)
  print("NEW MAX OUT DATE: ", new_max_out_date.strftime("%m/%d/%Y"))

if __name__ == '__main__':
  collect_entry_exits()
  print("Entry and EXIT dates")
  for e in entry_exits:
    print("\t", e)
  no_of_days_outside()
  get_maxout_date()