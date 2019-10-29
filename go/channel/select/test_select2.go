package main

import "fmt"

func main() {
	ch := make(chan int)
	ch <- 1
	// <- ch
	fmt.Println("gyh")
}