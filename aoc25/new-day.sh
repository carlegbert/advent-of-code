#!/bin/bash

TEMPLATES_DIR="templates"
SOLUTIONS_DIR="solutions"
ROOT_MODULE_PATH="github.com/carlegbert/advent-of-code/aoc25"

if [ -z "$1" ]; then
    echo "Usage: $0 <Day Number>"
    echo "Example: $0 5"
    echo "Example: $0 10"
    exit 1
fi

DAY_NUM=$1
DAY_NN=$(printf "%02d" $DAY_NUM)
DAY_DIR="${SOLUTIONS_DIR}/day${DAY_NN}"
PACKAGE_NAME="day${DAY_NN}"
INPUT_FILE="inputs/${DAY_NN}.txt"
EXAMPLE_INPUT_FILE="inputs/example/${DAY_NN}.txt"

mkdir -p "$DAY_DIR"

cp "${TEMPLATES_DIR}/solution.go" "${DAY_DIR}/${PACKAGE_NAME}.go"
cp "${TEMPLATES_DIR}/solution_test.go" "${DAY_DIR}/${PACKAGE_NAME}_test.go"

mkdir -p inputs/example
touch "${INPUT_FILE}"
touch "${EXAMPLE_INPUT_FILE}"
