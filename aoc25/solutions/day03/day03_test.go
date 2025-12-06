package day03_test

import (
	"testing"

	"github.com/carlegbert/advent-of-code/aoc25/solutions/day03"
)

const exampleInputPath = "example.txt"

func TestSolveP1(t *testing.T) {
	expected := 357

	result := day03.SolveP1(exampleInputPath)

	if result != expected {
		t.Errorf("SolveP1(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}

func TestSolveP2(t *testing.T) {
	expected := 0

	result := day03.SolveP2(exampleInputPath)

	if result != expected {
		t.Errorf("SolveP2(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}
