from print_block import PrintBlock
#from b_tree.utility.print_block import PrintBlock
#from b_tree.pointer import Pointer
from Noeud import Noeud


def get_btree_trace(btree):
    """
    Returns the string trace of a BTree, that could be printed in the console
    :param btree: the btree that we want to display
    :return: the String trace of the btree
    """
    max_depth = -1
    blocks = get_subtree_print_blocks(btree.racine, 0)
    for print_block in blocks:
        if print_block.depth > max_depth:
            max_depth = print_block.depth

    output_list = [""] * (max_depth + 1)
    for print_block in blocks:
        for i in range(max_depth+1):
            if i == print_block.depth:
                output_list[i] += print_block.content
            else:
                output_list[i] += " " * len(print_block.content)

    output = ""
    for line in output_list:
        output += line + "\n"

    return output


def get_subtree_print_blocks(node, depth):
    """
    Returns the PrintBlock list of the subtree, associated to the subtree node
    :param node: the subtree for which we want to get the printblocks
    :param depth: the current depth of the subtree
    :return: a list of StringBlocks with different depths, that represent the tree from left to right
    """
    print(str(node))
    output = []
    if node:
        if node.feuille:
            return [PrintBlock("|"+str(node)+"|", depth)]
        else:
            for i in range(len(node.cles)):
                output += [PrintBlock(str(node.cles[i]), depth)]
            for i in range(len(node.fils)):
                output += get_subtree_print_blocks(node.fils[i], depth+1)
            
            return output
    return []

