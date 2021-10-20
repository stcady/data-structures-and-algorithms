package bag

import "fmt"

type Bag struct {
	Name string
}

// This method means type T implements the interface I,
// but we don't need to explicitly declare that it does so.
func (t Bag) M() {
	fmt.Println(t.Name)
}
