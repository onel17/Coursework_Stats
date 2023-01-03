import random

def simulate_probability():
    children = []
    for i in range(3):
        children.append(random.choice(["Girl", "Boy"]))

    # Checking --> at least one child is a girl
    if "Girl" in children:
        # Checking --> if all children are girls
        return all(child == "Girl" for child in children)
    else:
        return False

# Run it for 1000 times
count = 0
for i in range(1000):
    result = simulate_probability()
    print(f"Simulation {i+1}: {result}")
    if result:
        count += 1

# Calculate probability
probability = count / 1000
# Print probability
print(probability)


