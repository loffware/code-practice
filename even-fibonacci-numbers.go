package main

import "fmt"

// main function that calculates the sum of even fibonacci numbers with values below 4 million
func main(){
	var sum int = 0
	for i := 2; fib(i) < 4000000; i++{
		if fib(i) % 2 == 0 {
			sum += fib(i)
			fmt.Println(sum)
		}
	}

}

// Recursive function that calculates a fibonacci number with base case n < 2
func fib (n int) int {
	if n < 2 {
		return 1
	}
	return fib(n-1) + fib(n-2)
}

