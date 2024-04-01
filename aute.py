import requests

def checkAndReport(url):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      return "The website is up."
    else:
      return "The website is down."
  except requests.exceptions.RequestException as e:
    return "The website is unreachable."
