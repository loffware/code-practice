package main

import "fmt"

// this pretty simply adds up the multiples of 3 and 5 from 1 to 100000, without double-counting
func main() {

	var sum int

	for i := range 100000 {
		if i%3 == 0 {
			sum += i
		}
		if i%5 == 0 {
			sum += i
		}

		if i%3 == 0 && i%5 == 0 {
			sum -= i
		}
	}

	fmt.Println(sum)

}
