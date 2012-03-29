import networkx as nx
__author__ = """Joseph Jira (jmjira@gmail.com)"""
__all__ = ['load_Layers']


def load_Layers():
    """
    Generates a networkx.DiGraph from layers within an open map document. 
    Point geometries are translated into nodes, lines into edges. 
    Coordinate tuples are used as keys. Accepts a single layer or many
    layers.

    Returns
    -------
    G : networkX graph

    Examples
    --------
    import networkx as nx
    >>> G = nx.DiGraph()
    
    >>> nx.load_Layers()
    
    >>> G=nx.load_Layers()

    """
    import arcpy
    net = nx.DiGraph()
    current_mxd = arcpy.mapping.MapDocument('CURRENT')
    layer_list = arcpy.mapping.ListLayers(current_mxd)
    
    for layer in layer_list:
        describe_layer = arcpy.Describe(layer)
        
        if describe_layer.shapeType == 'Point':
            desc = arcpy.Describe(layer)
            shape = desc.ShapeFieldName
            rows = arcpy.SearchCursor(layer)
            for row in rows:
                feat = row.getValue(shape)
                node = feat.getPart()
                nodeXY = node.X, node.Y
                net.add_node(nodeXY)   
            del row, rows

        if describe_layer.shapeType == 'Polyline':
            desc = arcpy.Describe(layer)
            shape = desc.ShapeFieldName
            rows = arcpy.SearchCursor(layer)
            for row in rows:
                feat = row.getValue(shape)
                edge_pt1 = feat.firstPoint
                edge_pt2 = feat.lastPoint
                edge_pt1XY = edge_pt1.X, edge_pt1.Y
                edge_pt2XY = edge_pt2.X, edge_pt2.Y
                net.add_edge(edge_pt1XY, edge_pt2XY)
            del row, rows
    return net

            
            
            
        
        
    

    

