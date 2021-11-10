package main

import "fmt"

// IsPalin determines if the provided string is a palindrome
// Note: spaces are counted in palindrome check
func IsPalin(String string) bool {
	lower := 0
	upper := len(String) - 1
	for lower <= upper {
		if String[lower] != String[upper] {
			return false
		}
		lower += 1
		upper -= 1
	}
	return true
}

// Conversion converts int M in decimal to radix N
func Conversion(m int, n int) string {
	return string(conversionUtil(m, n))
}

// conversionUtil is a recursive utility function for converting int M in decimal to radix N
func conversionUtil(m int, n int) string {
	if m == 0 {
		return ""
	} else {
		return conversionUtil(m/n, n) + fmt.Sprintf("%v", m%n)
	}
}

// SudokuCheck checks if the input array contains only one occurance of each integer in the set {1, 2, 3, 4, 5, 6, 7, 8, 9}
func SudokuCheck(arr []int) bool {
	size := len(arr)
	if size != 9 {
		return false
	}
	set := make(map[int]int)
	for i := 1; i < 10; i++ {
		set[i] = 0
	}
	for _, val := range arr {
		if val > 9 || val < 1 {
			return false
		} else {
			set[val] += 1
			if set[val] > 1 {
				return false
			}
		}
	}
	return true
}

func main() {
	fmt.Println("Problem 1:")
	fmt.Println("\tIs \"abcba\" a palindrome? ", IsPalin("abcba"))
	fmt.Println("\tIs \"abba\" a palindrome? ", IsPalin("abba"))
	fmt.Println("\tIs \"abcdba\" a palindrome? ", IsPalin("abcdba"))
	fmt.Println("\tIs \"steven\" a palindrome? ", IsPalin("steven"))
	fmt.Println("\tIs \"a bb a\" a palindrome? ", IsPalin("a bb a"))
	fmt.Println("\tIs \"abb a\" a palindrome? ", IsPalin("abb a"))
	fmt.Println("Problem 2:")
	fmt.Println("\t\"256\" in base \"2\"? ", Conversion(256, 2))
	fmt.Println("\t\"256\" in base \"16\"? ", Conversion(256, 16))
	fmt.Println("\t\"99\" in base \"2\"? ", Conversion(99, 2))
	fmt.Println("Problem 3:")
	fmt.Println("\t", []int{5, 4, 8, 1, 9, 3, 6, 2, 7}, "contains", []int{1, 2, 3, 4, 5, 6, 7, 8, 9}, "? ", SudokuCheck([]int{5, 4, 8, 1, 9, 3, 6, 2, 7}))
	fmt.Println("\t", []int{5, 4, 8, 1, 9, 9, 6, 2, 7}, "contains", []int{1, 2, 3, 4, 5, 6, 7, 8, 9}, "? ", SudokuCheck([]int{5, 4, 8, 1, 9, 9, 6, 2, 7}))
	fmt.Println("\t", []int{5, 4, 8, 1, 9, 1, 10, 2, 7}, "contains", []int{1, 2, 3, 4, 5, 6, 7, 8, 9}, "? ", SudokuCheck([]int{5, 4, 8, 1, 9, 1, 10, 2, 7}))
	fmt.Println("\t", []int{5, 4, 8, 1, 9, 3, 6, 2, 7, 1}, "contains", []int{1, 2, 3, 4, 5, 6, 7, 8, 9}, "? ", SudokuCheck([]int{5, 4, 8, 1, 9, 3, 6, 2, 7, 1}))
}
