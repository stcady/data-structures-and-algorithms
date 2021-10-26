package bag

import (
	"fmt"
	"sort"
)

type Bag struct {
	Name     string
	Items    []interface{}
	Capacity int
}

func NewBag(name string) BagInterface {
	b := Bag{}
	b.Name = name
	b.Items = []interface{}{}
	b.Capacity = 20
	return &b
}

// AddItem adds an item to the bag
func (b *Bag) AddItem(item interface{}) error {
	if b.IsFull() {
		return fmt.Errorf("Invalid addition. Bag is at capacity.")
	} else {
		b.Items = append(b.Items, item)
	}
	return nil
}

// AddItems adds a set of items to the bag
func (b *Bag) AddItems(items ...interface{}) error {
	for _, v := range items {
		err := b.AddItem(v)
		if err != nil {
			return err
		}
	}
	return nil
}

// EmptyBag empties the bag
func (b *Bag) EmptyBag() {
	b.Items = []interface{}{}
}

// FindAllItems finds all items that match
func (b Bag) FindAllItems(item interface{}) []int {
	indices := []int{}
	for i, v := range b.Items {
		if b.IsEqual(v, item) {
			indices = append(indices, i)
		}
	}
	return indices
}

// FindItem finds single item that matches
func (b Bag) FindItem(item interface{}) int {
	for i, v := range b.Items {
		if b.IsEqual(v, item) {
			return i
		}
	}
	return -1
}

// FindMultipleItems finds all items that match provided list of items
func (b Bag) FindMultipleItems(items ...interface{}) []int {
	indices := []int{}
	for _, v := range items {
		for _, i := range b.FindAllItems(v) {
			indices = append(indices, i)
		}
	}
	return indices
}

// GetCapacity returns the capacity of the bag
func (b Bag) GetCapacity() int {
	return b.Capacity
}

// GetName returns the name of the bag
func (b Bag) GetName() string {
	return b.Name
}

// ItemFrequency determines the count of a specific item
func (b Bag) ItemFrequency(item interface{}) int {
	count := 0
	for _, v := range b.Items {
		if v == item {
			count += 1
		}
	}
	return count
}

// IsEmpty determines if the bag is empty
func (b Bag) IsEmpty() bool {
	return (len(b.Items) == 0)
}

// IsEqual determines if two items are equal
func (b Bag) IsEqual(item1 interface{}, item2 interface{}) bool {
	if item1 == item2 {
		return true
	}
	return false
}

// IsFull determines if the bag length is equal to the bag capacity
func (b Bag) IsFull() bool {
	if b.Len() >= b.Capacity {
		return true
	} else {
		return false
	}
}

// Len
func (b Bag) Len() int {
	return len(b.Items)
}

// PrintItems prints the items in the bag
func (b Bag) PrintBag() {
	fmt.Println(b.Items)
}

// RemoveItem removes an item from the bag
func (b *Bag) RemoveItem(removeAll bool, item interface{}) {
	if removeAll {
		for true {
			i := b.FindItem(item)
			if i != -1 {
				b.Items = append(b.Items[:i], b.Items[i+1:]...)
			} else {
				break
			}
		}
	} else {
		i := b.FindItem(item)
		if i != -1 {
			b.Items = append(b.Items[:i], b.Items[i+1:]...)
		}
	}
}

// RemoveItems removes a set of items from the bag
func (b *Bag) RemoveItems(removeAll bool, items ...interface{}) {
	for _, v := range items {
		b.RemoveItem(removeAll, v)
	}

}

// SetName sets the name of the bag
func (b *Bag) SetName(name string) {
	b.Name = name
}

// SortBag sorts the bag in alphanumberic order
func (b *Bag) SortBag() {
	s := make([]string, len(b.Items))
	for i, v := range b.Items {
		s[i] = v.(string)
	}
	sort.Strings(s)
	t := make([]interface{}, len(s))
	for i, v := range s {
		t[i] = v
	}
	b.Items = t
}
