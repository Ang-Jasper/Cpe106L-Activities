import gzip
import io
import random
import requests

url = "https://raw.githubusercontent.com/lsb/human-numbers/trunk/one-million-numbers.txt.gz"
response = requests.get(url)

with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as gz:
    lines = gz.read().decode("utf-8").splitlines()

total_count = len(lines)
numbers = list(range(1, total_count + 1))

random_number = random.choice(numbers)

believe = ""
while believe != "Y" and believe != "N":
  print("DO YOU BELIEVE IN 1 IN A MILLION CHANCE?!")
  believe = input("Y/N: ")

  if believe.upper() == "Y":
      print("Are you feeling lucky?")
      decision = input("Y/N: ")
      if decision.upper() == "Y":
          number = int(input("Pick a number from 1 to a million: "))
          if number == random_number:
            print(f"OMG YOU GOT IT, your number {number} = randon number {random_number}")
          else:
            print(f"Well... it was 1 in a million, your number {number} = randon number {random_number}")
      else:
        print("Coward.....")

  elif believe.upper() == "N":
    print("Ah too bad， Bye Bye!")
  else:
    print("Invalid input.")
