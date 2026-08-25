#!/bin/bash
mkdir -p input/docs input/tmp
echo "alpha" > input/docs/notes\ one.txt
echo "beta" >> input/docs/notes\ one.txt
echo "hidden" > input/docs/secret.txt
touch input/tmp/empty.txt
printf "2026\n0824\n" > input/run.log

mkdir -p work/24170001032
cp --parents docs/*.txt tmp/*.txt ../work/24170001032/

find work/24170001032 -type d -exec chmod 750 {} +
find work/24170001032 -type f -exec chmod 640 {} +

(cd work/24170001032 && find . -type f -printf "%P %s\n" | sort > ../../inventory.txt)
