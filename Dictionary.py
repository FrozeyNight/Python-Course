prices = {"pizza" : "$6.99",
            "apple" : "$0.49",
            "water bottle" : "$0.99",
            "sandwich": "$2.52"}

print(prices.get("sandwich"))
print(prices["sandwich"])

prices.update({"sushi":"$8.99"})
print(prices.get("sushi"))
prices.update({"sushi":"$7.99"})
print(prices.get("sushi"))

print(prices)
prices.pop("pizza")
print(prices)
# popitem removes the last item (weird...)
prices.popitem()
print(prices)

if prices.get("burger"):
    print("This food is available")
else:
    print("This food is not available")

for key in prices.keys():
    print(key)

for key, value in prices.items():
    print(f"{key}:{value}")