package day02_test

import (
	"testing"

	"github.com/carlegbert/advent-of-code/aoc25/solutions/day02"
)

const exampleInputPath = "example.txt"

func TestSolveP1(t *testing.T) {
	expected := 1227775554

	result := day02.SolveP1(exampleInputPath)

	if result != expected {
		t.Errorf("SolveP1(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}

func TestSolveP2(t *testing.T) {
	expected := 0

	result := day02.SolveP2(exampleInputPath)

	if result != expected {
		t.Errorf("SolveP2(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}
