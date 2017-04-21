#!/bin/sh

cat <<EOF > $1
#include <stdio.h>
void hello() { printf("hello, world\n"); }
EOF
