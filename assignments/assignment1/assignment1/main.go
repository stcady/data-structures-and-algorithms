package main

import (
	bag "assignment1/bag"
)

func main() {
	var i bag.I = bag.T{S: "hello"}
	i.M()
}
