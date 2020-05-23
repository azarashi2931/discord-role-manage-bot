import os

def get_observer():
  return int(os.environ['ROLE_ID_OBSERVER'])

def get_participant():
  return int(os.environ['ROLE_ID_PARTICIPANT'])
