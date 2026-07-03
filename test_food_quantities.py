#Automated Test Suite
import food_quantities

def test_single_main():
    menu = [
        {
            "name": "Burger",
            "category": "main",
            "serving_size": 1,
            "unit": "burgers"
        }
    ]

    result = food_quantities(50, menu)

    assert result[0]["Total Needed"] == "55.0 burgers"

def test_multiple_desserts():
    menu = [
        {
            "name": "Cookies",
            "category": "dessert",
            "serving_size": 2,
            "unit": "cookies"
        },
        {
            "name": "Cupcakes",
            "category": "dessert",
            "serving_size": 1,
            "unit": "cupcakes"
        }
    ]

    result = food_quantities(80, menu)

    assert result[0]["Total Needed"] == "88.0 cookies"
    assert result[1]["Total Needed"] == "44.0 cupcakes"
def test_multiple_mains():
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
        }
    ]

    result = food_quantities(100, menu)

    assert result[0]["Total Needed"] == "55.0 pieces"
    assert result[1]["Total Needed"] == "41.2 cups"