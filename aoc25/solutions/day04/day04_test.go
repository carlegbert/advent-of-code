package day04_test

import (
	"testing"

	"github.com/carlegbert/advent-of-code/aoc25/solutions/day04"
)

const exampleInputPath = "example.txt"

func TestSolveP1(t *testing.T) {
	expected := 13

	result := day04.SolveP1(exampleInputPath)

	if result != expected {
		t.Errorf("SolveP1(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}

func TestSolveP2(t *testing.T) {
	expected := 43

	result := day04.SolveP2(exampleInputPath)

	if result != expected {
		t.Errorf("SolveP2(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}
