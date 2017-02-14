''' 
Solution by Sarah West
completed for NJIT CS645-851

Reads IP Addresses and attack information read from a CSV file,
and returns the information requested by user.
'''
import sys


def read_csv(file_name):
    """Read a csv file that lists attack information"""
    dict = {}
    with open(file_name, 'r') as file_reader:
        for line in file_reader:
        	line = line.strip().split(',')
        	# dict[key = ip_address] = [country, count attacks, count users ]
        	dict[line[0]] = [line[1], line[2], line[3]]
    return dict


def get_choice():
	choice = input("""
	(1) Find the country of origin for an IP 
	(2) Find the number of attacks associated with an IP address
	(3) Find the number of different invalid user names tried
	(4) Quit

	Please make a choice: """)
	if choice not in ["1", "2", "3", "4"]:
		choice = get_choice()
	return int(choice)


def main():
	dict = read_csv('attacks.csv')
	user_choice = get_choice()

	if (user_choice == 4):
		sys.exit(0)

	ip_address = input("Enter an IP address: ")
	
	if ip_address in dict:
		# dict[key = ip_address] = selection from list of possible choices [1, 2, 3, 4]
		print(dict[ip_address][int(user_choice) - 1])
	else:
		print("IP address not in data store")

if __name__ == "__main__":
    main()


