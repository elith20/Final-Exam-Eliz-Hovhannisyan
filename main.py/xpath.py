class Xpath:
    # sign_up page xpaths
    first_name = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input'
    last_name = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[2]/div/input'
    phone = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/div/input'
    email = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[4]/div/input'
    password = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[5]/div/input'
    account_type = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[7]/button'
    customer = '//*[@id="account_type"]/option[1]'
    sign_up = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[7]/button/span[1]'

    # login page xpaths
    login = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input'
    acc_password = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input'
    login_button = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/button'

    # hotels page xpaths
    hotels = '//*[@id="fadein"]/header/div[2]/div/div/div/div/div[2]/nav/ul/li[2]/a'
    location = '//*[@id="select2-hotels_city-container"]'
    city_name_to_input = '//*[@id="fadein"]/span/span/span[1]/input'
    first_result = '//*[@id="select2-hotels_city-results"]/li[1]'
    yerevan = '//*[@id="hotels_city"]/option[2]'
    search_button =	'//*[@id="submit"]'
    any_hotel = '//*[@id="city centre apartment  international tour"]/div'
    details = '//*[@id="cascade hotel"]/div/div[2]/div/div[2]/div/a' #(Yerevan Deluxe Hotel)

    select_room = '//*[@id="contentContainer"]/div[3]/ol/li[2]/div/a/div/div[3]/div/div[3]/button/div/div/div/span'
    reserve = '//*[@id="ChildRoom-Cq8BCI7GsqoDEAIgAjAGQAFKDTM2NUQxMDBQXzEwMFBQirYDeosBU29tZSg3MTQzNjQzNyl8NDQ3MTA3NDYzfDF8MjAyMDIyMDYwXzIxMDMyMzk3MUBufDN8QkJ8TGlzdCgxKXwzNjVEMTAwUF8xMDBQfFNvbWUodHJ1ZXwxfEJCfDcxNDM2NDM3fHhpd2FufDIwMjAyMjA2MF8yMTAzMjM5NzFAbnwyMDIwMjIwNjB8KRICCAEaBCgGMAE="]/div/div[5]/div[1]/div/div[1]/button'
    full_name = '//*[@id="firstName_lastName"]'
    reserve_email = '//*[@id="email"]'
    retype_email = '//*[@id="retypeEmail"]'
    phone_number = '//*[@id="phoneNumber"]'
    country = '//*[@id="countryId"]/optgroup[2]/option[10]'
    non_smoking	= '//*[@id="SiteContent"]/div/div[1]/div[4]/div/div[3]/div[1]/div[2]/label[1]'
    large_bed = '//*[@id="SiteContent"]/div/div[1]/div[4]/div/div[3]/div[1]/div[2]/label[3]'
    next_final_step = '//*[@id="SiteContent"]/div/div[1]/div[6]/div/button/div/div/span'


def exp_url():
    expected_url = 'https://www.agoda.com/book/payment/?cnty=246&secdat=qYWM4u9zM1a%252FP7%252BzqmpO62BOpRFl0rRHqTYosVSChJ%252BLfX%252FhDy4PdEzaHJu31tZqNYgg15pYELtPN6%252F47jAhxpNqS%252FOzvePrXsfYy%252F0ZSEf3Z7NVdi48z172S4GH%252FWfZxm1ktSq8TERFIsI4k6cVP17PGnyEwMVPlBsRbFZkuz3Pqd84p1FI04lpsSdaHFviavNlxt%252BC0XHeDFCOVkXB4FRm7fo%252BywCO4ljk8JW1l1ydjFWEg5PcjsBOj8qFWNErKqUIwYMJedPSjPMLM2krF3JdS8XKrnP%252BIEHT5sRUGgY%253D&v=29&cnIcp=0&dclid=&gclid=&ame=&aso=&aca=&aco=&ate=&mrs=0&siteId=1743607&ori=AM&r0=%252FphyqQKPTcHADZvwo9x5WdfQPTww8tJ%252BFCzrzMBxmTyAl%252BMBqZ6Tv3tA%252B9n6qyCiKp5hSip6ehIJUeluE751kSveFqCcZJdtzP8fVCmre3%252F7pfmHydfKDJz8oeD78BJNUs9x4mEdvMya7tE2fzY4fssz8rFg5gfIadeZl7juiW1QFrsT4PWwyXLPeaPqvttslbGN2OfmB2F%252BcCaKb31WCKihJb3GV6y7AXpYsG0fMJX1mF7bBTehxIMkdBiR2C6DPTsAOiI2DPA39DIgJQKp5qc1RsGsnbICe%252Bw%252BYhHS0XwlQyUNhd0BH2J%252BRdnyMdbE%252FyTibrqEJ51jTp70YaQc6%252BGIqeZgF7EDhq4l1lnj7W38RWv4zZZBY4JvZU6wR3ATrsySHBfdkxdLkTcaH%252B4csGPdsQmV7D9GJKLWBDc73ooNbLQ%252BLhDdLbJaOKTJVvxsA%252Fk5nV3zfC9jdkK8lP%252Ff7g%253D%253D&nr0=1&xbr0=&sarg=i4b11F0YAv3unKg4boDGkA3gUXC4V78eWH7HDyBKMYSEx9aY3e8cBE7yA3tKL1pAX8Ggblaqlg6RD%252F9t84QZCPr7kAw6tptVNFPOE3bDFy2w0YJP07EeVAL855HfykFomHSn1WEUUkYdWVs8SB%252BW7XBFstwqIMS%252FuHH7LtCilrPGerwr9aoC8%252BTl4F6G4bF81hqbdVIhC1CjovsNEt8LeAUC4B5Bpt9DBMzGv3096CFe7Ndbe247EVVMZyTfZw%252BM&m=601&sreq=-1&finc=false&nco=0'
    return expected_url