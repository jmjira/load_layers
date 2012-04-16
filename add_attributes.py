def add_local_manhole_attributes(layer):
    desc = arcpy.Describe(layer)
    shape = desc.ShapeFieldName
    rows = arcpy.SearchCursor(layer)    
    for row in rows:

        feat = row.getValue(shape)
        node = feat.getPart()
        nodeXY = node.X,node.Y
        ownership = row.getValue('OWNERSHIP')
        flow = row.getValue('FLOW')

# For local terminator label (degree == 1, with no shape)
        if G.degree(nodeXY) == 1:
            attributes = {}
            flow = flow.replace(' ','\n')
            attributes['label'] = ownership + '\n' + flow
            attributes['shape'] = 'none'
            G.add_node(nodeXY, attributes)
            
# For a local manhole within the DiGraph (a ellipse labeled 'LOCAL')
        else:
            attributes = {}
            ownership = ownership.replace(' ','\n')
            attributes['label'] = ownership
            G.add_node(nodeXY, attributes)

    del row, rows
    
def add_district_manhole_attributes(layer):
    desc = arcpy.Describe(layer)
    shape = desc.ShapeFieldName
    rows = arcpy.SearchCursor(layer)    
    for row in rows:   
        feat = row.getValue(shape)
        node = feat.getPart()
        nodeXY = node.X,node.Y
        name = row.getValue('NAME')
        manholetype = row.getValue('TYPE')
        districttype = row.getValue('DISTRICTTYPE')
        interceptor = row.getValue('INTERCEPTOR')
        
# default District manhole
        if G.degree(nodeXY) > 1:
            attributes = {}
            attributes['label'] = name
            attributes['style'] = 'filled'
            attributes['fillcolor'] = '#E5CCFF'
            G.add_node(nodeXY, attributes)
            
# Blind Junction
        if G.degree(nodeXY) > 1 and manholetype == 'BLIND JUNCTION':
            attributes = {}
            attributes['label'] = name + '\n' + '(BJ)'
            attributes['fillcolor'] = '#E0E0E0'
            G.add_node(nodeXY, attributes)

# Terminators:
        if G.degree(nodeXY) == 1 and manholetype == 'BULKHEAD':
            attributes = {}
            attributes['xlabel'] = 'BULKHEAD'
            attributes['shape'] = 'point'
            G.add_node(nodeXY, attributes)

        if G.degree(nodeXY) == 1 and districttype == 'INTERCEPTOR':
            attributes = {}
            interceptor = interceptor.replace(' - ', '\n')
            interceptor = interceptor.replace(' ', '\n')
            attributes['label'] = interceptor
            attributes['shape'] = 'none'
            G.add_node(nodeXY, attributes)
            
        if G.degree(nodeXY) == 1 and districttype == 'CSO RESPONSIBILITY':
            attributes = {}
            name = name[3:6]
            name = 'TO' + '\n' + 'CSO-' + name
            attributes['label'] = name
            attributes['shape'] = 'none'
            G.add_node(nodeXY, attributes)
            
    del row, rows
            
def add_district_permit_point_attributes(layer):
    attributes = {}
    desc = arcpy.Describe(layer)
    shape = desc.ShapeFieldName
    rows = arcpy.SearchCursor(layer)    
    for row in rows:
        feat = row.getValue(shape)
        node = feat.getPart()
        nodeXY = node.X,node.Y
        name = row.getValue('NAME')
        attributes['label'] = name_attributes
        attributes['style'] = 'filled'
        attributes['fillcolor'] = '#FF99FF'
        attributes['peripheries'] = '2'
        G.add_node(nodeXY, attributes)
    del row, rows
 
def add_district_pump_station_attributes(layer):
    attributes = {}
    desc = arcpy.Describe(layer)
    shape = desc.ShapeFieldName
    rows = arcpy.SearchCursor(layer)    
    for row in rows:
        feat = row.getValue(shape)
        node = feat.getPart()
        nodeXY = node.X,node.Y
        name = row.getValue('NAME')
        name = name.replace(' ','\n')
        attributes['label'] = name
        attributes['style'] = 'filled'
        attributes['fillcolor'] = '#FFFF99'
        attributes['shape'] = 'rectangle'
        attributes['peripheries'] = '2'
        G.add_node(nodeXY, attributes)
    del row, rows
       
def add_local_pump_station_attributes(layer):
    attributes = {}
    desc = arcpy.Describe(layer)
    shape = desc.ShapeFieldName
    rows = arcpy.SearchCursor(layer)    
    for row in rows:
        feat = row.getValue(shape)
        node = feat.getPart()
        nodeXY = node.X,node.Y
        name = row.getValue('LOCALNAME')
        name = name.replace('-','\n')
        name = name.replace(' ','\n')
        attributes['label'] = name
        attributes['style'] = 'filled'
        attributes['fillcolor'] = '#C0C0C0'
        attributes['shape'] = 'rectangle'
        attributes['fontsize'] = '10'
        G.add_node(nodeXY, attributes)
    del row, rows

def add_district_flow_regulating_structure_attributes(layer):
    attributes = {}
    desc = arcpy.Describe(layer)
    shape = desc.ShapeFieldName
    rows = arcpy.SearchCursor(layer)      
    for row in rows:
        feat = row.getValue(shape)
        node = feat.getPart()
        nodeXY = node.X,node.Y
        regulatortype = row.getValue('TYPE')
        name = row.getValue('NAME')
        if regulatortype == 'REGULATOR':
            attributes['label'] = name
            attributes['shape'] = 'box'
            attributes['style'] = 'filled'
            attributes['fillcolor'] = '#CCFFCC'
        if regulatortype == 'RE-REGULATOR':
            attributes['label'] = name
            attributes['shape'] = 'hexagon'
            attributes['style'] = 'filled'
            attributes['fillcolor'] = '#FFB266'
        if regulatortype == 'SANITARY FLOW DIVIDER':
            attributes['label'] = name
            attributes['shape'] = 'hexagon'
            attributes['style'] = 'filled'
            attributes['fillcolor'] = '#CCFFCC'
        if regulatortype == 'AUTOMATED REGULATOR':
            attributes['label'] = name
            attributes['shape'] = 'rectangle'
            attributes['style'] = 'filled'
            attributes['fillcolor'] = '#FFB266'
            attributes['peripheries'] = '2'
        if regulatortype == 'BACKFLOW':
            attributes['label'] = name
            attributes['shape'] = 'house'
            attributes['style'] = 'filled'
            attributes['fillcolor'] = '#C0C0C0'
        if regulatortype == 'HYDROBRAKE':
            attributes['label'] = name
            attributes['shape'] = 'rectangle'
            attributes['style'] = 'filled'
            attributes['fillcolor'] = '#FF56B2'
        if regulatortype == 'MANUAL GATE':
            attributes['label'] = name
            attributes['shape'] = 'rectangle'
            attributes['style'] = 'filled'
            attributes['fillcolor'] = '#FFCCCC'
            attributes['peripheries'] = '2'
        if regulatortype == 'SIPHON':
            attributes['label'] = name
            attributes['shape'] = 'circle'
            attributes['style'] = 'filled'
            attributes['fillcolor'] = '#FFCCE5'
            attributes['peripheries'] = '2'
        if regulatortype == 'TBD':
            attributes['label'] = name
            attributes['shape'] = 'box'
            attributes['style'] = 'filled'
            attributes['fillcolor'] = '#E0E0E0'            
        G.add_node(nodeXY, attributes)
    del row, rows   

def add_district_sewerpipe_attributes(layer):
    attributes = {}
    desc = arcpy.Describe(layer)
    shape = desc.ShapeFieldName
    rows = arcpy.SearchCursor(layer)
    for row in rows:
        feat = row.getValue(shape)
        firstPt = feat.firstPoint
        lastPt = feat.lastPoint
        firstPointXY = firstPt.X, firstPt.Y
        lastPointXY = lastPt.X, lastPt.Y
        pipetext = row.getValue('PIPETEXT')
        flow = row.getValue('FLOW')
        attributes['label'] = pipetext
        attributes['fontsize'] = '8'
        G.add_edge(firstPointXY, lastPointXY, attributes)
    del row, rows


def add_local_sewerpipe_attributes(layer):
    attributes = {}
    desc = arcpy.Describe(layer)
    shape = desc.ShapeFieldName
    rows = arcpy.SearchCursor(layer)
    for row in rows:
        feat = row.getValue(shape)
        firstPt = feat.firstPoint
        lastPt = feat.lastPoint
        firstPointXY = firstPt.X, firstPt.Y
        lastPointXY = lastPt.X, lastPt.Y
        pipetext = row.getValue('PIPETEXT')
        attributes['label'] = pipetext
        attributes['fontsize'] = '8'
        G.add_edge(firstPointXY, lastPointXY, attributes)
    del row, rows
