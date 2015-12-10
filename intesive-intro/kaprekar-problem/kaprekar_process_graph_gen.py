"""
The Kaprekar Process.

Create a nice, pretty image of the Kaprekar process.

__author__: "Aravindhan Dhanasekaran" 
__email__: "adhanas@ncsu.edu"
"""

# Pretty graphs
# http://interactive.blockdiag.com/graphviz/
TEST_GRAPH = """\
digraph {
  graph[label="Hello &nbsp; World",
        labelloc=t,
        fontsize=16]

  A -> B -> C;
  edge[color=blue];
       B -> D [label="bd"];
  edge[color=red];
  node[shape=box];
  "123, 0012, 342, ..." -> F -> D;
}
"""


def kaprekar_step(n):
    """
    Do one Kaprekar step on number, n.

    The process works as follows:
        1. Arrange all digits of n in ascending order.
        2. Arrange all digits of n in descending order.
        3. Find the difference between the largest and smaller
           variateions.
    Reference: https://en.wikipedia.org/wiki/6174_(number)

        >>> kaprekar_step(6174)
        6174
        >>> kaprekar_step(5689)
        4176
        >>> kaprekar_step(4176)
        6174
        >>> kaprekar_step(3330)
        2997
        >>> kaprekar_step(1000)
        999
        >>> kaprekar_step(21)
        2088
    """
    #
    # Use zero pads to ensure that 'n' has 4 digits.
    # Use sorted() to sort the digits in asc/dsc order.
    #
    zero_padded_n = "%04d" % (n,)
    ascending = int(''.join(sorted(zero_padded_n)))
    descending = int(''.join(sorted(zero_padded_n, reverse=True)))
    return abs(descending - ascending)


def gen_graph():
    """
    Generate Graphviz code for Kaprekar process problem.
    """
    graph = {}
    for n in range(9999 + 1):
        graph[n] = kaprekar_step(n)

    # In graph{}, keys are all possible numbers (all sources) and values
    # are the step of all possible numbers (targets).

    # Find all targets:
    #
    # Someone points to the numbers in circles, i.e., targets.
    # Also, many sources may point to the same target. We are only
    # interested in the unique targets. So, use a set().
    targets = set(graph.values())

    # Find all non-targets:
    #
    # No one points to the numbers in boxes, i.e., non-targets.
    # Also, many non-targets might point to the same target.
    #   1. Find all non-targets. This is trivial; the set difference
    #      between all sources and targets leaves us with non-targets.
    #   2. Group non-targets that points to the same target.
    #      i.e., boxes to circles.

    # 1. Find all non-targets.
    all_sources = set(graph.keys())
    non_targets = sorted(all_sources - targets)

    # 2. Group non-targets based on the target they point to.
    non_target_boxes = {}
    for each_non_target in non_targets:
        # In which box should the non-target thrown in?
        # Eg., '1' is a non-target and it points to target '999'
        # Also, '10' is pointing to target '999' too.
        # So, '1', '10' and any other non-target that points to '999'
        # should be thrown into the same non_target_box
        #
        # WANTED:
        #   non_target_boxes[999].append(1)
        #   non_target_boxes[999].append(10)
        #   non_target_boxes[999].append(other non-targets --> to 999)
        dst_target = graph[each_non_target]
        non_target_boxes.setdefault(dst_target, []).append(each_non_target)

        # The dict setdeafault above can be replaced with the try
        # except block to achieve the same goal.
        
        # try:
        #    non_target_boxes[dst_target].append(each_non_target)
        # except KeyError:
        #   non_target_boxes[dst_target] = [each_non_target]


    # Generate Graphviz code
    graph_title = "Kaprekar Process"
    graph_settings = "  graph[rankdir=LR, label=\"%s\", " \
                     "labelloc=t, fontsize=32]" % (graph_title)
    print "digraph {"
    print graph_settings
    print "  edge[color=blue, fontcolor=blue, fontsize=10];"

    # Make all targets point to other targets.
    # i.e., circles to circles.
    for each_target in targets:
        target_dest = graph[each_target]
        print "%d -> %d;" % (each_target, target_dest)

    # All non-targets sharing the same dst. target are to be
    # grouped in a box. The edge between non-target box to dst. target
    # should have the number of non-targets sharing the dst. target
    # as a label.
    print "  node[shape=box];"
    for dst_target, non_target_box in non_target_boxes.items():
        box_data = "\"%04d, %04d, %04d, ...\"" % (tuple(non_target_box[:3]))
        node_data = "%s -> %d [label = \"%d\"];" % \
                    (box_data, dst_target, len(non_target_box))
        print node_data

    print "}"


if "__main__" == __name__:
    import doctest
    doctest.testmod()
    gen_graph()
