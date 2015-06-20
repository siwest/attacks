import sys

def read_csv(file_name):
    """Read a csv file that lists possible transactions"""
    result = list()
    with open(file_name, 'r') as file_reader:
        for line in file_reader:
            order_set = list(line.strip().split(','))
            result.append(order_set)
    return result[1:]

def create_dictionaries(data_list):
	N = len(data_list) -1
	country_dictionary = []
	count_attacks_dictionary = []
	count_users_dictionary = []
	while (data_list): 	#while data_list is not empty
		string1 = data_list.pop(0)

		line = list(string1)	#get a line item
		print(line)

		ip_address = str(line.pop(0))  #use this as key
		print(ip_address)
		string2 = line.pop(0)
		print(string2)
		country_dictionary = {ip_address: string2}
		string3 = line.pop(0)
		print(string3)
		count_attacks_dictionary = {ip_address: string3}
		string4 = line.pop(0)
		print(string4)
		count_users_dictionary = {ip_address: string4}

	dictionary_list = list()
	dictionary_list.append(country_dictionary)
	dictionary_list.append(count_attacks_dictionary)
	dictionary_list.append(count_users_dictionary)
	return dictionary_list


def get_choice():
	choice = input("""
	(1) Find the number of attacks associated with an IP address
	(2) Find the country of origin for an IP
	(3) Find the number of different invalid user names tried
	(4) Quit

	Please make a choice: """)
	return choice


def get_dictionary_key_value(ip_input, dictionary):
	value = ''
	if (ip_input in dictionary):
		value = dictionary[ip_input]
	else:
		print("There is no record of an attack attempt from that IP")
	return value


def main():
	data_list = read_csv('attacks.csv')
	dictionary_list = create_dictionaries(data_list)
	country_dictionary = dictionary_list.pop(0)
	count_attacks_dictionary = dictionary_list.pop(0)
	count_users_dictionary = dictionary_list.pop(0)

	user_choice = get_choice()
	value = ''
	if (user_choice == '1'):
		ip_input = input("Enter an IP address: ")
		value = get_dictionary_key_value(ip_input, country_dictionary)
	if (user_choice == '2'):
		ip_input = input("Enter an IP address: ")
		value = get_dictionary_key_value(ip_input, count_attacks_dictionary)
	if (user_choice == '3'):
		ip_input = input("Enter an IP address: ")
		value = get_dictionary_key_value(ip_input, count_users_dictionary)
	if (user_choice == '4'):
		sys.exit(0)


	print(value)

if __name__ == "__main__":
    main()


