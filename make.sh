#! /bin/bash

set -e

echo "----> Making rock"
luarocks --local make luasocket-scm-0.rockspec
