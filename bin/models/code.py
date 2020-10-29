def get_code_by_snippetId(snippetId):
    return """
    void _delete_from_node(Tree tree, Duck duck) {
        generic_type _duck = getMemberByName(tree, duck);
        if(strcmp(duck->name, tree->root->current->name) == 0) {
            free(tree);
        }
        delete_tree_from_node(_duck); 
    }
    """

def create_new_snippet(code):
    """
    return id of the new snippet
    """
    pass