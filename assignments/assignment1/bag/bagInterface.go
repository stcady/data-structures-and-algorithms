package bag

// BagInterface type that defines a set of methods
type BagInterface interface {
	AddItem(item interface{}) error
	AddItems(item ...interface{}) error
	EmptyBag()
	GetCapacity() int
	GetName() string
	FindAllItems(item interface{}) []int
	FindItem(item interface{}) int
	FindMultipleItems(item ...interface{}) []int
	ItemFrequency(interface{}) int
	IsEmpty() bool
	IsEqual(item1 interface{}, item2 interface{}) bool
	IsFull() bool
	Len() int
	PrintBag()
	RemoveItem(removeAll bool, item interface{})
	RemoveItems(removeAll bool, item ...interface{})
	SetName(name string)
	SortBag()
}
