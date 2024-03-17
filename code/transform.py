def transform(data):
    '''Convert inches to meters and round off to two decimals
    1 inch is 0.0254 meters '''
    data['height'] = data.height.astype(float).mul(0.0254).round(2)
    
    '''Convert pounds to kilograms and round off to two decimals
    1 pound is 0.45359237 kilograms '''

    data['weight'] = data.weight.astype(float).mul(0.45359237).round(2)
    
    return data