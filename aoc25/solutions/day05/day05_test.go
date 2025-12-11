package day05_test

import (
	"testing"

	"github.com/carlegbert/advent-of-code/aoc25/solutions/day05"
)

const exampleInputPath = "example.txt"

func TestSolveP1(t *testing.T) {
	expected := 3

	result := day05.SolveP1(exampleInputPath)

	if result != expected {
		t.Errorf("SolveP1(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}

func TestSolveP2(t *testing.T) {
	expected := 14

	result := day05.SolveP2(exampleInputPath)

	if result != expected {
		t.Errorf("SolveP2(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}

func TestSolveP2_2(t *testing.T) {
	expected := 24

	result := day05.SolveP2("example2.txt")

	if result != expected {
		t.Errorf("SolveP2(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}
