#!/usr/bin/env python

# mptensor - Parallel Library for Tensor Network Methods
#
# Copyright 2016 Satoshi Morita
#
# mptensor is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# mptensor is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with mptensor.  If not, see
# <https://www.gnu.org/licenses/>.

import sys


def func(n):
    str = "Index("
    for i in range(n):
        str += "size_t j{0},".format(i)
    str = str[:-1] + "):idx({0})\n".format(n)
    str += "{"
    for i in range(n):
        str += "idx[{0}]=j{0};".format(i)
    str += "};\n"
    return str


num = 16 if len(sys.argv) < 2 else int(sys.argv[1])
output = open('index_constructor.hpp', 'w')

output.write("""
#ifndef _INDEX_CONSTRUCTOR_HPP_
#define _INDEX_CONSTRUCTOR_HPP_

/*! @name
These constructors generated by @c index_constructor.py mimic the list literal of python.
Constructors with more arguments exist but they are omitted from this document for simplicity.
*/
//! @{
""")

for n in range(1, 4):
    output.write(func(n))

output.write("""
//! @cond
""")

for n in range(4, num + 1):
    output.write(func(n))

output.write("""
//! @endcond
""")

output.write("""
//! @}
#endif // _INDEX_CONSTRUCTOR_HPP_
""")
output.close()
