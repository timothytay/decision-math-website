
test_list = [5, 89, 123, 4, 23]

def bin_pack(numbers, bin):
    output = ""
    for number in numbers:
        if number > bin:
            return f"{number} is bigger than the bin size so it cannot be packed."
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
    return output


def sort_items(items):
	output = "Passes:\n" + f'{", ".join([str(number) for number in items])}\n'
	while True:

		swap = False
		for i in range(len(items)-1):
			first_item = items[i]
			second_item = items[i+1]
			if first_item > second_item:
				items[i] = second_item
				items[i+1] = first_item
				swap = True

		if swap == False:
			break
		output += f'{", ".join([str(number) for number in items])}\n'
		print(items)
	return output

edges = {"AB":2.0, "BC":3.0}
vertices = ["A", "B", "C"]

def find_mst(edges, vertices):

    for edge in list(edges.keys()):
        first_counter = 0
        second_counter = 0
        for comparison_edge in list(edges.keys()):
            if edge[0] in list(comparison_edge):
                first_counter += 1
            if edge[1] in list(comparison_edge):
                second_counter += 1
        if first_counter < 2 and second_counter < 2:
            return "The graph is not connected."


    sorted_edges = dict(sorted(edges.items(), key=lambda item: item[1]))
    total_weight = 0
    used_vertices = [list(sorted_edges.keys())[0][0]]
    used_edges = []
    while True:
        for edge, weight in sorted_edges.items():
            if edge[0] not in used_vertices and edge[1] in used_vertices:
                used_vertices.append(edge[0])
                used_edges.append(edge)
                total_weight += weight
                del edges[edge]
                break

            elif edge[0] in used_vertices and edge[1] not in used_vertices:
                used_vertices.append(edge[1])
                used_edges.append(edge)
                total_weight += weight
                del edges[edge]
                break

        if sorted(used_vertices) == sorted(vertices):
            break

    return f"The MST weight is {total_weight} and it includes edges {used_edges}."


if __name__ == "__main__":
	find_mst(edges, vertices)

