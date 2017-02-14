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
	dict = {}
	ip_addresses = []
	countries = []
	count_attacks = []
	count_users = []
	for line in data_list:
		# dict[ip_address] = country, count_attack, count_users
		dict[line[0]] = [line[1], line[2], line[3]]
	return dict


def get_choice():
	choice = input("""
	(1) Find the country of origin for an IP 
	(2) Find the number of attacks associated with an IP address
	(3) Find the number of different invalid user names tried
	(4) Quit

	Please make a choice: """)
	if not (choice in ["1", "2", "3", "4"]):
		choice = get_choice()
	return int(choice)


def main():
	data_list = read_csv('attacks.csv')
	dict = parse_data(data_list)
	user_choice = get_choice()

	if (user_choice == 4):
		sys.exit(0)

	ip_address = input("Enter an IP address: ")
	result = 0
	if ip_address in dict:
		print(dict[ip_address][int(user_choice) - 1])
	else:
		print("IP address not in data store")

if __name__ == "__main__":
    main()


