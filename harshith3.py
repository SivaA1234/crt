def company_name():
    print("Welcome! Please select a car company:")
    print("1. Toyota")
    print("2. Mahindra")
    print("3. Mercedes")
    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        return "Toyota"
    elif choice == 2:
        return "Mahindra"
    elif choice == 3:
        return "Mercedes"
    else:
        print("Invalid choice. Please try again.")
        return company_name()

def model_name(company):
    print(f"Welcome to {company}. Please enter the specific model name:")
    if company == "Toyota":
        return input("Toyota Models: Corolla, Camry, Innova: ")
    elif company == "Mahindra":
        return input("Mahindra Models: XUV500, Scorpio, Thar: ")
    elif company == "Mercedes":
        return input("Mercedes Models: C-Class, E-Class, S-Class: ")
    else:
        print("Invalid choice.please try again.")
        return model_name()
        
def variant(company, model):
    print(f"Welcome to {company} {model}. Please select the variant:")
    print("1. Petrol")
    print("2. Diesel")
    choice = int(input("Enter your choice (1/2): "))
    if choice == 1:
        return "Petrol"
    elif choice == 2:
        return "Diesel"
    else:
        print("Invalid choice. Please try again.")
        return variant(company, model)

def display_details(company, model, variant):
    ex_showroom_price = 0
    if company == "Toyota":
        if model == "Corolla":
            ex_showroom_price = 1500000
        elif model == "Camry":
            ex_showroom_price = 3500000
        elif model == "Innova":
            ex_showroom_price = 1800000
    elif company == "Mahindra":
        if model == "XUV500":
            ex_showroom_price = 1800000
        elif model == "Scorpio":
            ex_showroom_price = 1600000
        elif model == "Thar":
            ex_showroom_price = 1200000
    elif company == "Mercedes":
        if model == "C-Class":
            ex_showroom_price = 4000000
        elif model == "E-Class":
            ex_showroom_price = 5000000
        elif model == "S-Class":
            ex_showroom_price = 8000000

    cgst = 0.09 * ex_showroom_price
    sgst = 0.09 * ex_showroom_price
    insurance = 50000

    onroad_price = ex_showroom_price + cgst + sgst + insurance
    print(f"Ex-showroom Price: {ex_showroom_price}")
    print(f"On-road Price: {onroad_price}")


selected_company = company_name()
selected_model = model_name(selected_company)
selected_variant = variant(selected_company, selected_model)
display_details(selected_company, selected_model, selected_variant)
