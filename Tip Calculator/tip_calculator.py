print('Welcome to the tip calculator!')

bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
n_ppl = int(input('How many people to split the bill? '))

split_pay = round(bill * (1 + tip / 100) / n_ppl, 2)

print(f'Each person should pay: ${split_pay:.2f}')      # Print as a fixed 2-decimal format. AKA $12 -> $12.00; $12.4 -> $12.40