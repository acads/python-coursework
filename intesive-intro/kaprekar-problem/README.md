# Kaprekar Process
6174 is known as [Kaprekar's Constant](https://en.wikipedia.org/wiki/6174_(number)). The constant is notable for Kaprekar process, which involves 4 steps:

1. Take any four-digit number, using at least two different digits. (Leading zeros are allowed.)
2. Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary.
3. Subtract the smaller number from the bigger number.
4. Go back to step 2.

Applying Kaprekar process to any four digit number, would result in Kaprekar's constant in at most seven iterations.

## Kaprekar Process Graph Generator
Use Python and [Graphviz's](http://www.graphviz.org/) command line tool (for Linux and Mac OS X), dot, to generate a [pretty looking graph](https://upload.wikimedia.org/wikipedia/commons/4/4f/KaprekarRoutineFlowGraph6174.svg)

## Usage
The Python script doesn't take any input amd output's Graphviz code to actually generate the graph.
```
$ python kaprekar_process_graph_gen.py > in.graph
```

The Graphviz code (output from the Python script) can then be fed as input to the Graphviz's `dot` command line tool to generate the final graph.
```
$ dot -Tsvg -O in.graph
```