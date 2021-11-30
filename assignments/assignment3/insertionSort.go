package main

// less compares two values and returns true if value1 < value2
func less(value1 string, value2 string) bool {
	return value1 < value2
}

// more compares two values and returns true if value1 > value2
func more(value1 string, value2 string) bool {
	return value1 > value2
}

// InsertionSort sorts the string array in either ascending or descending order
func InsertionSort(arr []string, asc bool) {

	// initialize variables
	size := len(arr)
	comp := less
	i := 1

	// ascending switch to more function handler
	if asc {
		comp = more
	}

	// iterate picking the value to insert into the sorted array on the left
	for i < size {
		// save value to be inserted
		temp := arr[i]
		j := i
		// shift values to the right until proper position is found
		for j > 0 && comp(arr[j-1], temp) {
			arr[j] = arr[j-1]
			j -= 1
		}
		// insert value into proper position
		arr[j] = temp
		i += 1
	}
}
