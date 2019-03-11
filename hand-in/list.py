# Organizing List of British Colonies


def main():

    # dumps string of every British Colony
    foo = """Aden Protectorate
Anglo-Egyptian Sudan
Auckland Islands
Bahamas
Bahrain
Balleland
Bangladesh
Barbados
Basutoland
Bechuanaland
Bermuda
British Borneo
British Cameroons
British East Africa
British Egypt
British Egypt
British Guiana
British Honduras
British India
British Malaya
British Solomon Islands
British Somaliland
British Togoland
British Western Pacific Territories
Brunei
Burma
Ceylon
Colonial Fiji
Colonial Nigeria
Colony of Newfoundland
Corsica
Cyprus
Emirate of Transjordan
Falkalnd Islands
Federated Malay States
Gambia Colony and Protectorate
Gilbert and Ellice Islands
Gold Coast
Heligoland
Hong Kong
India
Indian Reserve
Ionian Islands
Ireland
Island of St. John
Jamaica
Kingdom of Rarotonga
Kingdom of Sarawak
Leeward Islands
Malta
Mandatory Iraq
Mandatory Palestine
Menorca
Mosquito Coast
Muscat and Oman
Nauru
New Hebrides
New Hebrides
New South Wales
Niue
North Borneo
Northern Rhodesia
Nyasaland
Oregon Country
Pakistan
Phoenix Islands
Province of East Florida
Province of Nova Scotia
Province of Quebec
Province of West Florida
Qatar
Queensland
Rupert's Land
Sheikhdom of Kuwait
Sierra Leone Colony and Protectorate
Singapore
Solomon Islands
South Africa
South Arabia
South Australia
South Georgia
South-West Africa
Southern Rhodesia
Straits Settlements
Sultanate of Zanzibar
Swan River Colony
Swaziland
Tanganyika Territory
Territory of New Guinea
Territory of Papua
Territory of Papua New Guinea
Thirteen Colonies
Tokelau
Tonga
Trucial States
Uganda Protectorate
Unfederated Malay States
Van Diemen's Land
Victoria
Western Samoa
Windward Islands
"""

    # converts string to array
    array = foo.splitlines()
    print(f"There use to be {len(array)} colonies that belong to the UK")

    popped_array = array.pop()
    print(f"The last British colony in terms of alphabetical order is {popped_array}")

    array.reverse()
    array.insert(0, "Windward Islands")
    print(f"{array[0]} is the last colony alphabetically.")

    array.sort()
    print(f"{array[0]} is the first colony of the UK alphabetically")

    array.remove("Hong Kong") # Hong Kong is no longer a colony

    array.append("Asgard") # that one time Asgard was subjugated to the British Empire
    print(f"{sorted(array)} is the updated list")
    
    # uncomment to  print the string
    # for foo in array:
    #     print(f"{foo}", end=",\n", flush=True)
    
    
    # index = 1
    # for foo in array:
    #     if (foo == "Hong Kong"):
    #         print(f"{index}")
    #         break
    #     index += 1

        

if __name__ == "__main__":
    main()