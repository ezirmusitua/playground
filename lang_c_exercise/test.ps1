$NAME = $args[0]

clang src\$NAME.c -o build\$NAME.exe

& ".\build\$NAME.exe"