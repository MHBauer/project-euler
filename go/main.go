package main

import "fmt"

func main() {
	fmt.Println(euler1())
}

func euler1() int {
	acc := 0
	for i := 3; i < 1000; i++ {
		if i%3 == 0 || i%5 == 0 {
			acc += i
		}
	}
	return acc
}
