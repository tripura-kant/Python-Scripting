print_help() {
    echo "Usage: ./calculate_area.sh [option] [shape] [dimension1] [dimension2]"

    echo "Calculate the area of various geometric shapes."

    echo "Options:"
    echo  "-h              Display this help message."
    echo  "-i              Interactive mode."

    echo "Shapes and dimensions:"
    echo  "circle radius          Calculate the area of a circle."
    echo  "square side            Calculate the area of a square."
    echo  "rectangle length width Calculate the area of a rectangle."
}

if [[ "$1" == "-h" ]]; then
    print_help
    exit 0
fi    