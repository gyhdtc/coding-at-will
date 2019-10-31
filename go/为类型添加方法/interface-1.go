package main

import "fmt"

type interger int
func (a interger) Less(b interger) bool {
	return a < b
}
// 由于改变了 a 的值，所以需要用引用类型
func (a *interger) Add(b interger) {
	*a += b
}
func main() {
	var a interger = 2
	if a.Less(5) {
		fmt.Println("a small")
	} else {
		fmt.Println("a big")
	}
	a.Add(2)
	fmt.Println(a)
}