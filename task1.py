#task1

global_logic = ['Shashank Samant', 'Raj Radhakrishnan', 'Nitesh Banga', 'Scott Brubaker', 'Arya Barirani',
                'Zaheer Allam', 'Jim Walsh', 'Amy Hanlon-Rodemich', 'Kirk Hammett', 'Till Lindemann']

toshiba = ['Tanaka Hisashige', 'Shibaura Seisakusho', 'Dimebag Darrell', 'Tom Araya', 'Kirk Hammett', 'Till Lindemann']

toshiba.extend(global_logic)
for element in toshiba:
    print(element)

# Good. But employees of global logic now in toshiba and global logic but
# should be only in toshiba. Take a look on some methods of list which could
# help you.
