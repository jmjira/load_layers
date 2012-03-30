import networkx as nx
__author__ = """Joseph Jira (jmjira@gmail.com)"""
__all__ = ['load_layers']


def load_layers():
    """
    Generates a networkx.DiGraph from layers within an open map document. 
    Point geometries are translated into nodes, lines into edges. 
    Coordinate tuples are used as keys. Accepts a single layer or many
    layers.
    
    Must have an arcmap document (mxd) open with at least one point layer
    or line layer.
    
    ESRI ARCGIS 10 and networkx required
    
    Install in C:\Python26\ArcGIS10.0\site-packages\networkx-1.6-py2.6egg\networkx\readwrite
    
    Returns
    -------
    G : networkX graph

    Examples
    --------
    >>> import arcpy
    >>> import networkx as nx
    >>> G = nx.DiGraph()
    >>> G = nx.load_layers()
    >>> G.number_of_nodes()
    91
    >>>
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
