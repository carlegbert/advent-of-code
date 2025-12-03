package dayNN_test

import (
	"testing"

	"github.com/carlegbert/advent-of-code/aoc25/solutions/dayNN"
)

const exampleInputPath = "inputs/example/NN.txt"

func TestSolveP1(t *testing.T) {
	expected := 0

	result := dayNN.SolveP1(exampleInputPath)

	if result != expected {
		t.Errorf("SolveP1(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}

func TestSolveP2(t *testing.T) {
	expected := 0

	result := dayNN.SolveP2(exampleInputPath)

	if result != expected {
		t.Errorf("SolveP2(%s) failed, got: %d, want: %d", exampleInputPath, result, expected)
	}
}
