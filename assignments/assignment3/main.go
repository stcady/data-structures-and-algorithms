package main

import (
	"fmt"
	"strconv"
)

func main() {

	fmt.Println("Problem 1:")
	// test insertion sort ascending
	data := []string{"C", "Z", "B", "K", "G", "U", "A", "R"}
	fmt.Println("\toriginal:\t", data)
	InsertionSort(data, true)
	fmt.Println("\tasc-sorted:\t", data)

	// test insertion sort descending
	data = []string{"C", "Z", "B", "K", "G", "U", "A", "R"}
	InsertionSort(data, false)
	fmt.Println("\tdesc-sorted:\t", data)

	// demonstrate hashmaps by counting the frequency of integers
	fmt.Println("Problem 2:")
	array := []int{1, 1, 1, 3, 8, 5, 3, 0, 8, 4, 5, 1, 2, 3, 8, 0, 9, 10, 7, 8, 5, 2, 1, 7, 4, 3}
	map1 := make(map[string]int)
	for _, val := range array {
		map1[strconv.Itoa(val)] += 1
	}
	fmt.Println("\toriginal:\t", array)
	fmt.Println("\tcounting:\t", map1)

	// demonstrate hashmaps by mapping integers to english spelling using a helper map
	map2 := map[int]string{
		0:  "zero",
		1:  "one",
		2:  "two",
		3:  "three",
		4:  "four",
		5:  "five",
		6:  "six",
		7:  "seven",
		8:  "eight",
		9:  "nine",
		10: "ten",
	}
	stringArray := make([]string, len(array), len(array))
	i := 0
	for _, val := range array {
		stringArray[i] = map2[val]
		i += 1
	}
	fmt.Println("\thelper-map:\t", map2)
	fmt.Println("\tpronounce:\t", stringArray)
}
