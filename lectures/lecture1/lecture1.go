package main

import "fmt"

func leftRotate(a []string, rotation int) (newArray []string) {
	size := len(a)
	for i := 0; i < rotation; i++ {
		newArray = a[1:size]
		newArray = append(newArray, a[0])
		a = newArray
	}
	return newArray
}

func rightRotate(a []string, rotation int) (newArray []string) {
	size := len(a)
	for i := 0; i < rotation; i++ {
		newArray = a[0 : size-1]
		newArray = append([]string{a[size-1]}, newArray...)
		a = newArray
	}
	return newArray
}

func main() {
	array1 := []string{"a", "b", "c", "d", "e"}
	fmt.Println(leftRotate(array1, 1))
}
