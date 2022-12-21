from replit import db
import os

# store my name in the replit db
# db["Name"] = 'sam'
print(db['Name'])

keys = db.keys()

print(keys)

for key in db:
  print(db[key])








def factorial(n):
  print(f'factorial({n})')
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
    
print(factorial(3))




myApiKey = os.environ['apiKey']
print(myApiKey)

