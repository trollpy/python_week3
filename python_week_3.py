def discount_calculation(price, discount_percent):
    if discount_percent >= 10:
        discount = price * (discount_percent / 100)
        return price - discount, discount
    return price, 0

def calculation():
    while True:
        try:
            original_price = float(input("Enter the original price: R"))
            discount = float(input("Enter the discount percentage: "))
            final_price, discount_amount = discount_calculation(original_price, discount)
            
            if final_price < original_price:
                print(f"\nNormal price: R{original_price:.2f}")
                print(f"Discount applied: {discount}%")
                print(f"Discount amount: R{discount_amount:.2f}")
                print(f"Final price: R{final_price:.2f}")
            else:
                print(f"\nNo discount applied. Price remains R{original_price:.2f}")
                print("Note: Minimum 15% discount required to apply discount")
            break
        except ValueError:
            print("Please enter valid numerical values!")

if __name__ == "__main__":
    calculation()