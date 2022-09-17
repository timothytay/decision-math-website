

def bin_pack(numbers, bin):
    output = ""
    
    numbers.sort(reverse=True)
    bins = []
    while len(numbers) > 0:
        total = 0
        bin_numbers = []
        for number in numbers:
            if float(total + number) < bin:
                total += number
                print(total)
                bin_numbers.append(number)
        for number in bin_numbers:
            numbers.remove(number)
        bins.append(bin_numbers)
    for i in range(len(bins)):
        output += f"Bin {i+1}: {bins[i]}\n"
    print(output) 


bin_pack([4, 2, 5, 12, 3], 15)
