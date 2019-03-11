""" Organizing List of British Colonies

Course: CS 30
Period: 3
Date created: Feb. 5, 2019
Date completed: Feb. 7, 2019
By: Andrew Li
This program spits out interesting "facts" about British Colonies

"""


def main():

    # dumps string of every British Colony
    # from a table in the following link:
    # https://www.worldatlas.com/articles/former-british-colonies.html
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

    # converts string to array/list
    colonies = foo.splitlines()

    # prints length of string (which is the # of colonies the UK has owned)
    print(f"There use to be {len(colonies)} colonies that belong to the UK")

    # pops the last colony alphabetically
    print("The last British colony in terms of alphabetical " +
          "order is " +
          colonies.pop()
          )

    # reverses the alphabetical order
    colonies.reverse()

    # adds Windward Islands back as a colony *those revolutionary pagans
    colonies.insert(0, "Windward Islands")

    # prints the last colony again
    print(f"{colonies[0]} is the last colony alphabetically.")

    # sorts the colonies alphabetically
    # It also prints the first colony alphabetically
    colonies.sort()
    print(f"{colonies[0]} is the first colony of the UK alphabetically")

    # Hong Kong is no longer a colony, thus it is removed
    colonies.remove("Hong Kong")

    # that one time Asgard was subjugated to the British Empire
    colonies.append("Asgard")

    # prints the updated list of the British Colonies
    print("The updated list of colonies is the following: ", flush=True)

    # converts array to string via join method
    # It also prints all the colonies out in alphabetical order
    print(", ".join(sorted(colonies)))

# system calls name so the main method can be called
if __name__ == "__main__":
    main()
