def applydiscount(bill):
    discount = bill * 0.35
    final_bill = bill - discount
    print("Discount is :: ",discount)
    print("Final bill after discount is :: ",final_bill)
    
applydiscount(50000)