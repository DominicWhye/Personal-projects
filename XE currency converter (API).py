import requests

MID_URL = "https://www.xe.com/api/protected/midmarket-converter/"
HEADERS = {
    "Accept":        "application/json, text/plain, */*",
    "Referer":       "https://www.xe.com/currencyconverter/",
    "Authorization": "Basic bG9kZXN0YXI6cHVnc25heA==",  # your header
    "User-Agent":    "Mozilla/5.0 (compatible)"
}

def fetch_rates() -> dict:
    """Fetch the USD-based mid-market rates map."""
    resp = requests.get(MID_URL, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()
    return data["rates"]

if __name__ == "__main__":
    amt    = float(input("📊 Amount: "))
    base   = input("From (e.g. SGD): ").strip().upper()
    target = input("To   (e.g. USD): ").strip().upper()

    rates = fetch_rates()



    if base not in rates or target not in rates:
        print(f"Error: rates for {base} or {target} not available.")
        exit(1)

    #users amount conversion:
    converted_amount = amt / rates[base] * rates[target]
    print(f"\n💵 {amt:.2f} {base} = {converted_amount:.5f} {target}\n")

    #Compute the 1-unit cross-rate both ways:
    #    rate_base_to_target  = (units of target per USD) / (units of base per USD)
    rate_base_to_target = rates[target] / rates[base]
    #    rate_target_to_base  = inverse
    rate_target_to_base = rates[base] / rates[target]

    print(f"💰 1 {base} = {rate_base_to_target:.6f} {target}")
    print(f"💰 1 {target} = {rate_target_to_base:.6f} {base}")
    print()


    show_codes = input("Show all available currency codes? (y/n): ").strip().lower()
    if show_codes == 'y' or show_codes == 'yes':
        print() #added blank line for cleaner UI
        print("Available currency codes:")
        print(", ".join(sorted(rates.keys()))) #, is added to make cleaner display
        print() #added blank line for cleaner UI



     
