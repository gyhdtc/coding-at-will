package main

import "fmt"

func Count(ch chan int) {
	fmt.Println("In")
	ch <- 1
	fmt.Println("Counting")
}

func main() {
	chs := make([]chan int, 10)
	for i := 0; i < 10; i++ {
		chs[i] = make(chan int)
		go Count(chs[i])
	}
	fmt.Println("C")
	for i, ch := range(chs) {
		fmt.Println("A", i)
		<-ch
		fmt.Println("B", i)
	}

}