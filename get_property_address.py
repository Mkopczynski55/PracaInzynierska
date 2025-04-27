# Web Scrapper do pobierania adresu na podstawie Parcel Identification - ostatecznie nie musiał być używany

def get_property_address(pid):

    url = f"https://beacon.schneidercorp.com/Application.aspx?AppID=165&LayerID=2145&PageTypeID=4&PageID=1108&KeyValue={pid}"

    driver = webdriver.Chrome() # Sterownik musi być zainstalowany i aktualny
    driver.get(url)

    html_content = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html_content, "html.parser") # Parsowanie HTML

    # Szukam adresu w strukturze HTML, w uzyskaniu oglądu sytuacji pomaga Devs Tool w przeglądarce
    address_element = soup.find(id="ctlBodyPane_ct101_lblPropertyAddress")
    if address_element:
        property_address = address_element.get_text(separator=" ", strip=True)
    else:
        full_address_candidates = soup.find_all(string=lambda text: "Property Address" in text)
        property_address = ""
        for element in full_address_candidates:
            parent = element.find_parent()
            if parent:
                sibling = parent.find_next("td")
                if sibling:
                    property_address = sibling.get_text(separator=" ", strip=True)
                    break

    if not property_address:
        property_address = "Nie znaleziono adresu."

    return property_address

# print(get_property_address('0527165230'))