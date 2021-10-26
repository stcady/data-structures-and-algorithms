package main

import (
	"data-structures-and-algorithms/assignments/assignment1/bag"
	"fmt"
)

func main() {

	fmt.Println("\nTest naming/versioning")
	myBag := bag.NewBag("1.0")
	fmt.Println(myBag.GetName())
	myBag.SetName("1.1")
	fmt.Println(myBag.GetName())

	fmt.Println("\nTest getting capacity")
	fmt.Println(myBag.GetCapacity())

	fmt.Println("\nTest adding items")
	myBag.AddItem("Steven")
	fmt.Println(myBag.Len())
	myBag.AddItem("Eric")
	fmt.Println(myBag.Len())
	myBag.PrintBag()
	myBag.AddItems("Katherine", "Tyler", "Bill", "Bill", "Karen", "Jane", "Jane", "Tyler", "Steven", "Steven")
	fmt.Println(myBag.Len())
	myBag.PrintBag()

	fmt.Println("\nTest removing items")
	myBag.RemoveItem(false, "Karen")
	myBag.RemoveItem(false, "Joe")
	myBag.PrintBag()
	myBag.RemoveItems(false, "Jane", "Steven")
	myBag.PrintBag()
	myBag.RemoveItem(true, "Steven")
	myBag.PrintBag()

	fmt.Println("\nTest is equal")
	fmt.Println(myBag.IsEqual("Steven", "Steven"))
	fmt.Println(myBag.IsEqual("Steven", "Seven"))

	fmt.Println("\nTest finding items")
	myBag.PrintBag()
	fmt.Println(myBag.FindAllItems("Bill"))
	fmt.Println(myBag.FindItem("Bill"))
	fmt.Println(myBag.FindMultipleItems("Bill", "Tyler"))

	fmt.Println("\nTest item frequency, bag length, bag capacity")
	myBag.PrintBag()
	fmt.Println(myBag.ItemFrequency("Tyler"))
	fmt.Println(myBag.Len())

	fmt.Println("\nTest sorting the bag")
	myBag.PrintBag()
	myBag.SortBag()
	myBag.PrintBag()

	fmt.Println("\nTest is empty and is full check")
	myBag.PrintBag()
	fmt.Println(myBag.IsFull())
	fmt.Println(myBag.IsEmpty())
	myBag.EmptyBag()
	fmt.Println(myBag.IsEmpty())

}
