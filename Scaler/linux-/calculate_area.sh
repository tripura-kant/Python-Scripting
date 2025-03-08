#!/bin/bash

# Function to calculate the area of a circle
calculate_circle_area() {
    radius=$1
    area=$(echo "scale=5; 3.14159 * $radius * $radius" | bc)
    echo "Area of the circle: $area"
}

# Function to calculate the area of a square
calculate_square_area() {
    side=$1
    area=$(echo "$side * $side" | bc)
    echo "Area of the square: $area"
}

# Function to calculate the area of a rectangle
calculate_rectangle_area() {
    length=$1
    width=$2
    area=$(echo "$length * $width" | bc)
    echo "Area of the rectangle: $area"
}

# Task 1: Help Flag (-h)
if [[ $1 == "-h" ]]; then
    echo "Usage: ./calculate_area.sh [option] [shape] [dimension1] [dimension2]"
    echo ""
    echo "Calculate the area of various geometric shapes."
    echo ""
    echo "Options:"
    echo "  -h              Display this help message."
    echo "  -i              Interactive mode."
    echo ""
    echo "Shapes and dimensions:"
    echo "  circle radius          Calculate the area of a circle."
    echo "  square side            Calculate the area of a square."
    echo "  rectangle length width Calculate the area of a rectangle."
    exit 0
fi

# Task 2: Command Line Arguments
if [[ $1 != "-i" ]]; then
    shape=$1
    dimension1=$2
    dimension2=$3

    case $shape in
        circle)
            if [[ -z $dimension1 ]]; then
                echo "Please provide a radius for the circle."
                exit 1
            fi
            calculate_circle_area $dimension1
            ;;
        square)
            if [[ -z $dimension1 ]]; then
                echo "Please provide the side length for the square."
                exit 1
            fi
            calculate_square_area $dimension1
            ;;
        rectangle)
            if [[ -z $dimension1 || -z $dimension2 ]]; then
                echo "Please provide both length and width for the rectangle."
                exit 1
            fi
            calculate_rectangle_area $dimension1 $dimension2
            ;;
        *)
            echo "Invalid shape. Use -h for help."
            exit 1
            ;;
    esac
fi

# Task 3: Interactive Mode (-i)
if [[ $1 == "-i" ]]; then
    echo "Choose the shape to calculate the area:"
    echo "1. Circle"
    echo "2. Square"
    echo "3. Rectangle"
    read -p "Enter your choice (1/2/3): " choice

    case $choice in
        1)
            read -p "Enter the radius of the circle: " radius
            calculate_circle_area $radius
            ;;
        2)
            read -p "Enter the side length of the square: " side
            calculate_square_area $side
            ;;
        3)
            read -p "Enter the length of the rectangle: " length
            read -p "Enter the width of the rectangle: " width
            calculate_rectangle_area $length $width
            ;;
        *)
            echo "Invalid choice."
            exit 1
            ;;
    esac
fi
