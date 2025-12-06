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
INPUT_FILE="inputs/day${DAY_NN}.txt"
EXAMPLE_INPUT_FILE="${DAY_DIR}/example.txt"

mkdir -p "$DAY_DIR"

sed "s/dayNN/${PACKAGE_NAME}/g" "${TEMPLATES_DIR}/solution.go" > "${DAY_DIR}/${PACKAGE_NAME}.go"

sed -e "s/dayNN/${PACKAGE_NAME}/g" \
    -e "s/NN/${DAY_NN}/g" \
    "${TEMPLATES_DIR}/solution_test.go" > "${DAY_DIR}/${PACKAGE_NAME}_test.go"

touch "${INPUT_FILE}"
touch "${EXAMPLE_INPUT_FILE}"
