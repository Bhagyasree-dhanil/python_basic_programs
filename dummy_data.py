"""
pip install faker
"""

from faker import Faker
fake = Faker()
print(fake.name())
print(fake.address())
print(fake.text())
print(fake.profile())
