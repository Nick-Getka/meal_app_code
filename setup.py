# The MIT License (MIT)
#
# Copyright (c) 2014-2016 Benedikt Schmitt <benedikt@benediktschmitt.de>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from setuptools import setup

try:
    import meal_planner
except ImportError:
    meal_planner = None

if meal_planner:
    description = open("./README.rst").read()
    version = meal_planner.VERSION

    requirements = [
        line.strip() for line in open("./requirements.txt")
        ]

    setup(
        name = "meal_planner",
        version = version,
        url = "https://github.com/Nick-Getka/meal_app_code",
        license = "MIT License",
        author = "Nick Getka",
        author_email = "nicholas.getka@gmail.com",
        description = "A smart weekly meal planning app and food organizer",
        long_description = description,
        packages = ["meal_planner"],
        install_requires = requirements,
    )
else:
    print "ERROR: During Setup"
