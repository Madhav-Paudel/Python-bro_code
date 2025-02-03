def phone_code(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num=phone_code(country=977,area=789,first=879,last=546)
print(phone_num)
