def percent(tip_percent, value):
    return (value / 100) * tip_percent
# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    print(round(meal_cost + percent(tip_percent, meal_cost) +percent(tip_percent, tax_percent)))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
