#keyword arguments= an argument preceded by an identifier
#                    helps with redablity
#                    order of argumetns doesnt matter
#                    1.postional 2.default 3.keyword 4.arbitrary



def hello(greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")

hello("hello",  first="utkarsh", last="tiwari",title="mr",)


def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num=get_phone(country=1,area=234,first=234123,last=12323)

print(phone_num)

