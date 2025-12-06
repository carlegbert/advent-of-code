package day03

import (
	"github.com/carlegbert/advent-of-code/aoc25/lib"
)

func joltageForBank(bank string) int {
	bestFollowers := make([]int, len(bank))
	best := 0
	for i := len(bank) - 2; i >= 0; i-- {
		val := int(bank[i+1]) - '0'
		if val > best {
			best = val
		}

		bestFollowers[i] = best
	}

	best = 0
	bestI := 0
	for i := range len(bank) - 1 {
		val := int(bank[i]) - '0'
		if val > best {
			best = val
			bestI = i
		}
	}

	return best*10 + bestFollowers[bestI]
}

func SolveP1(inputPath string) int {
	result := 0
	for s := range lib.GetLines(inputPath) {
		result += joltageForBank(s)
	}

	return result
}

func SolveP2(inputPath string) int {
	_ = inputPath
	return 0
}
