package lib

import (
	"math"
	"slices"

	"golang.org/x/exp/constraints"
)

func DigitsInNum[T constraints.Integer](num T) T {
	if num == 0 {
		return 1
	}

	if num < 0 {
		num = -num
	}

	return T(math.Floor(math.Log10(float64(num)))) + 1
}

func Factors[T constraints.Integer](n T) []T {
	if n == 0 {
		return []T{}
	}
	if n < 0 {
		n = -n
	}

	factors := make(map[T]bool)

	limit := int(math.Sqrt(float64(n)))

	for i := 1; i <= limit; i++ {
		ii := T(i)
		if n%ii == 0 {
			factors[ii] = true
			factors[n/ii] = true
		}
	}

	factorList := make([]T, 0, len(factors))
	for f := range factors {
		factorList = append(factorList, f)
	}
	slices.Sort(factorList)

	return factorList
}
