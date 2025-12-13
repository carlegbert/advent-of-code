package day06_test

import (
	"testing"

	"github.com/carlegbert/advent-of-code/aoc25/solutions/day06"
)

const exampleInputPath = "example.txt"

func TestSolveP1(t *testing.T) {
	expected := 4277556

	result := day06.SolveP1(exampleInputPath)

	if result != expected {
		t.Errorf("SolveP1(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}

func TestSolveP2(t *testing.T) {
	expected := 3263827

	result := day06.SolveP2(exampleInputPath)

	if result != expected {
		t.Errorf("SolveP2(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}
