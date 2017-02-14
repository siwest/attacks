import sys

def read_csv(file_name):
    """Read a csv file that lists possible transactions"""
    result = list()
    with open(file_name, 'r') as file_reader:
        for line in file_reader:
            order_set = list(line.strip().split(','))
            result.append(order_set)
    return result[1:]

def parse_data(data_list):
	ip_addresses = []
	countries = []
	count_attacks = []
	count_users = []
	for line in data_list:
		# Assumes a valid, well-formed attacks file
		ip_addresses.append(line[0])  
		countries.append(line[1])
		count_attacks.append(line[2])
		count_users.append(line[3])
	print (ip_addresses)
	print(countries) 
	return ip_addresses, countries, count_attacks, count_users


def get_choice():
	choice = input("""
	(1) Find the number of attacks associated with an IP address
	(2) Find the country of origin for an IP
	(3) Find the number of different invalid user names tried
	(4) Quit

	Please make a choice: """)
	return choice


def get_dictionary_key_value(ip_input, ip_addresses, option_list):
	result = ''
	if (ip_input in ip_addresses):
		result = option_list[ip_addresses.index(ip_input)]
	else:
		print("There is no record of an attack attempt from that IP")
	return result


def main():
	data_list = read_csv('attacks.csv')
	ip_addresses, countries, count_attacks, count_users = parse_data(data_list)
	user_choice = get_choice()
	result = ''

	if (user_choice == '1'):
		ip_input = input("Enter an IP address: ")
		result = get_dictionary_key_value(ip_input, ip_addresses, count_attacks)
	if (user_choice == '2'):
		ip_input = input("Enter an IP address: ")
		result = get_dictionary_key_value(ip_input, ip_addresses, countries)
	if (user_choice == '3'):
		ip_input = input("Enter an IP address: ")
		result = get_dictionary_key_value(ip_input, ip_addresses, count_users)
	if (user_choice == '4'):
		sys.exit(0)



	print(result)

if __name__ == "__main__":
    main()


