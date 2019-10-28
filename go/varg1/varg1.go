package main

import "fmt"

func MyPrint(args ...interface{}) {
	for _, arg := range args {
		switch arg.(type) {
		case int :
			fmt.Println("int.")
		case string :
			fmt.Println("string.")
		case int64 :
			fmt.Println("int64.")
		default:
			fmt.Println("unknown.")
		}
	}
}

func main() {
	var v1 int = 1
	var v2 string = "2"
	var v3 int64 = 234
	var v4 float64 = 3.14
	MyPrint(v1, v2, v3, v4)
}