kilo_of_Durian = int(input("Enter number of Durian (kilo) ==>"))
purchase_price_of_Durian = int(input("Enter purchase price of Durian (Baht) ==>"))
sale_price_of_Durian = int(input("Enter sale price of Durian (Baht) ==>"))

Cost = kilo_of_Durian * purchase_price_of_Durian
Total = kilo_of_Durian * sale_price_of_Durian
Profit1 = (Total * 100) / Cost
profit2 = sale_price_of_Durian - purchase_price_of_Durian
print("Total profit = %.2f" %(Profit1), "%", "or", profit2, "Baht")
