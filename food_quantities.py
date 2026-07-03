def food_quantities(guest_count, menu_items, buffer_percent=0.10):
    """"
    Estimate food quantities for a catering event.

    Parameters:
        guest_count (int): Number of guests
        menu_items (list): List of menu items
        buffer_percent (float): Extra food percentage

    Returns a list: Quantity estimates for each menu item
    """

    # Count how many items for each category
    category_counts = {}

    for item in menu_items:
        category = item["category"]
        category_counts[category] = category_counts.get(category, 0) + 1

    results = []

    # Calculate quantity for each item
    for item in menu_items:

        name = item["name"]
        category = item["category"]
        serving_size = item["serving_size"]
        unit = item["unit"]

        # Divide the serving size for items in same category
        adjusted_serving = serving_size / category_counts[category]

        # Total quantity
        quantity = adjusted_serving * guest_count

        #buffer
        quantity *= (1 + buffer_percent)

        results.append({
            "Item": name,
            "Category": category.title(),
            "Serving per Guest": f"{adjusted_serving:.2f} {unit}",
            "Total Needed": f"{quantity:.1f} {unit}"
        })

    return results


# Non-trivial case
menu = [
    {
        "name": "Chicken",
        "category": "main",
        "serving_size": 1,
        "unit": "pieces"
    },
    {
        "name": "Pasta",
        "category": "main",
        "serving_size": 0.75,
        "unit": "cups"
    },
    {
        "name": "Rice",
        "category": "side",
        "serving_size": 0.5,
        "unit": "cups"
    },
    {
        "name": "Roasted Vegetables",
        "category": "side",
        "serving_size": 0.5,
        "unit": "cups"
    },
    {
        "name": "Salad",
        "category": "side",
        "serving_size": 1,
        "unit": "cups"
    },
    {
        "name": "Cake",
        "category": "dessert",
        "serving_size": 1,
        "unit": "slices"
    },
    {
        "name": "Hand Pies",
        "category": "dessert",
        "serving_size": 2,
        "unit": "pies"
    }
]

guests = 100

food_plan = food_quantities(guests, menu)

print(f"\nFood Plan for {guests} Guests\n")

for item in food_plan:
    print(f"Item: {item['Item']}")
    print(f"Category: {item['Category']}")
    print(f"Serving Per Guest: {item['Serving per Guest']}")
    print(f"Total Needed: {item['Total Needed']}")
    print("-" * 50)