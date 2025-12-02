class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    # Depth-first traversal approach
    result = []
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      # 1. Remove the first node from the nodes_to_visit list
      node = nodes_to_visit.pop(0)
      
      # 2. Check if this node has the id we're looking for
      if node and node.get('id') == id:
        return node
      
      # 3. Add its children (if any) to the BEGINNING of the nodes_to_visit list
      if node and 'children' in node:
        nodes_to_visit = node['children'] + nodes_to_visit

    return None
