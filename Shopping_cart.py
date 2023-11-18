cart = [
    {"product": "Leather Wallet", "unit_price": 1100, "gst_percentage": 18, "quantity": 1},
    {"product": "Umbrella", "unit_price": 900, "gst_percentage": 12, "quantity": 4},
    {"product": "Cigarette", "unit_price": 200, "gst_percentage": 28, "quantity": 3},
    {"product": "Honey", "unit_price": 100, "gst_percentage": 0, "quantity": 2}
]

max_gst_product = max(cart, key=lambda x: (x["gst_percentage"] / 100) * x["unit_price"])
print("Product with maximum GST amount:", max_gst_product["product"])


total_amount = sum((item["unit_price"] * (1 + item["gst_percentage"] / 100)) * item["quantity"] for item in cart)
print("Total amount: RS", total_amount)

discounted_amount = sum(item["unit_price"] * item["quantity"] * 0.95 if item["unit_price"] >= 500 else item["unit_price"] * item["quantity"] for item in cart)

print("Total amount to be paid: Rs.",discounted_amount)
