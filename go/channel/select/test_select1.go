package main

import "fmt"
func fun1() {
	ch := make(chan int)
	ch <- 1
	// <- ch
	fmt.Println("gyh")
}

func main() {
	ch := make(chan int, 1) // !!!
	// ch <- 4
	flag := 0
	for {
		if flag == 1 {
			i := <-ch
			fmt.Println("Value received:", i)
		}
		
		select {
			case ch <- 0:
				flag = 1
			case ch <- 1:
				flag = 1
		}
		//i := <-ch
		// fmt.Println("Value received:")
	}
	// i := <-ch
	// fmt.Println("Value received:", i)
}