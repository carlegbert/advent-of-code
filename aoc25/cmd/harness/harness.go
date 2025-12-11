package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/carlegbert/advent-of-code/aoc25/solutions/day01"
	"github.com/carlegbert/advent-of-code/aoc25/solutions/day02"
	"github.com/carlegbert/advent-of-code/aoc25/solutions/day03"
	"github.com/carlegbert/advent-of-code/aoc25/solutions/day04"
	"github.com/carlegbert/advent-of-code/aoc25/solutions/day05"
)

const inputPathFormat = "inputs/day%02d.txt"

func notImplemented(day, part int) func(string) int {
	return func(string) int {
		panic(fmt.Sprintf("Day %02d Part %d is not yet implemented", day, part))
	}
}

var solutions = map[int]map[int]func(string) int{
	1: {
		1: day01.SolveP1,
		2: day01.SolveP2,
	},
	2: {
		1: day02.SolveP1,
		2: day02.SolveP2,
	},
	3: {
		1: day03.SolveP1,
		2: day03.SolveP2,
	},
	4: {
		1: day04.SolveP1,
		2: day04.SolveP2,
	},
	5: {
		1: day05.SolveP1,
		2: day05.SolveP2,
	},
	6: {
		1: notImplemented(6, 1),
		2: notImplemented(6, 2),
	},
	7: {
		1: notImplemented(7, 1),
		2: notImplemented(7, 2),
	},
	8: {
		1: notImplemented(8, 1),
		2: notImplemented(8, 2),
	},
	9: {
		1: notImplemented(9, 1),
		2: notImplemented(9, 2),
	},
	10: {
		1: notImplemented(10, 1),
		2: notImplemented(10, 2),
	},
	11: {
		1: notImplemented(11, 1),
		2: notImplemented(11, 2),
	},
	12: {
		1: notImplemented(12, 1),
		2: notImplemented(12, 2),
	},
}

func main() {
	dayPtr := flag.Int("d", 0, "The day number to solve.")
	partPtr := flag.Int("p", 0, "The part number (1 or 2) to solve.")
	flag.Parse()

	day := *dayPtr
	part := *partPtr

	daySolutions, ok := solutions[day]
	if !ok {
		fmt.Printf("Error: Solution for Day %02d not yet implemented or imported.\n", day)
		os.Exit(1)
	}

	solver := daySolutions[part]

	inputPath := fmt.Sprintf(inputPathFormat, day)

	result := solver(inputPath)

	fmt.Printf("--- Day %02d Part %d Result ---\n", day, part)
	fmt.Printf("Input: %s\n", inputPath)
	fmt.Printf("Result: %d\n", result)
}
