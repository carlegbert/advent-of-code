package main

import (
	"flag"
	"fmt"
	"github.com/carlegbert/advent-of-code/aoc25/solutions/day01"

	"os"
)

const inputPathFormat = "inputs/day%02d.txt"

var solutions = map[int]map[int]func(string) int{
	1: {
		1: day01.SolveP1,
		2: day01.SolveP2,
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
