package main

import (
	"fmt"
	"flag"
)

func main() {

	//takes argument in the form of -n=(some integer) to determine which number to factor
	argumentPtr := flag.Int("n",40, "input number to factor")
	flag.Parse()

	fmt.Println(MaxSlice(prime_factors(*argumentPtr)))
}

// returns a slice of all prime factors of a positive integer
// modified version of stackoverflow.com/a/412942 which was written in python 
func prime_factors(n int) []int {
	var factors []int
	divisor := 2

	for n > 1 {
		for n % divisor == 0 {
			factors = append(factors, divisor)
			n /= divisor
		}

		divisor += 1
		if divisor * divisor > n {
			if n > 1 {
			factors = append(factors, n)
			return factors
			}
	}
}
	return factors

}


//Steps through the slice of factors and selects a maximal element
func MaxSlice(s []int) int {
	max := s[0]
	for i := 1; i < len(s); i++ {
		if s[i] > max {
			max = s[i]
		}
	}
	return max
}
