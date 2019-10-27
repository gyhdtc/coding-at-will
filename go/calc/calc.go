package main

import (
	"os"
	"fmt"
	"simplemath"
	"strconv"
)

func Usage = func() {
	fmt.Println("Usage : calc command [arguments] ...")
	fmt.Println("\nThe commands are:\n\tadd\tAddition of two values.\n\tsqrt\tSquare root of a non-negative value.")
}

func main() {
	args := os.args[1:]
	if args == nil || len(args) < 2{
		Usage()
		return
	}

	switch args[0] {
		case "add":
			if len(args) != 3 {
				fmt.Println("Usage: calc add <interger1><interger2>")
				return
			}
			v1, err1 := strconv.Atoi(args)
	}
} 