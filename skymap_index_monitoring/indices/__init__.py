COLOR_RAMP = {
    'NDVI': [
        [0, '#F44336', 'Stressed (0-0.2)'],
        [0.2, '#FF9800', 'Slightly Stressed (0.2-0.4)'],
        [0.4, '#FFEB3B', 'Moderate (0.4-0.6)'],
        [0.6, '#8BC34A', 'Healthy (0.6-0.8)'],
        [0.8, '#4CAF50', 'Very Healthy (0.8-1)']
    ],
    'SAVI': [
        [0, '#800000', 'Open (0-0.2)'],
        [0.2, '#F44336', 'Low Dense (0.2-0.4)'],
        [0.4, '#FF9800', 'Slightly Dense (0.4-0.6)'],
        [0.6, '#FFEB3B', 'Dense (0.6-0.8)'],
        [0.8, '#8BC34A', 'Highly Dense (0.8-1)'],
        [1, '#4CAF50', 'Very High (1+)']
    ],
    'RECI': [
        [0, '#F44336', 'Very Low (0-1)'],
        [1, '#FF9800', 'Low (1-1.5)'],
        [1.5, '#FFEB3B', 'Normal (1.5-2)'],
        [2, '#8BC34A', 'High (2-2.5)'],
        [2.5, '#4CAF50', 'Very High (2.5+)']
    ],
    'GCI': [
        [0, '#F44336', 'Very Low (0-1)'],
        [1, '#FF9800', 'Low (1-1.5)'],
        [1.5, '#FFEB3B', 'Normal (1.5-2)'],
        [2, '#8BC34A', 'High (2-2.5)'],
        [2.5, '#4CAF50', 'Very High (2.5+)']
    ],
    'EVI2': [
        [0, '#800000', 'Extremely Low (0-0.2)'],
        [0.2, '#F44336', 'Very Low (0.2-0.5)'],
        [0.5, '#FF9800', 'Low (0.5-0.8)'],
        [0.8, '#FFEB3B', 'Normal (0.8-1.1)'],
        [1.1, '#8BC34A', 'High (1.1-1.4)'],
        [1.4, '#4CAF50', 'Very High (1.4+)']
    ],
    'SIPI': [
        [0.8, '#FFEB3B', 'Stressed (0.8-1)'],
        [1, '#8BC34A', 'Healthy (1-1.2)'],
        [1.2, '#4CAF50', 'Very Healthy (1.2+)']
    ],
    'NDRE': [
        [0, '#F44336', 'Open Soil (0-0.2)'],
        [0.2, '#FFEB3B', 'Unhealthy (0.2-0.6)'],
        [0.6, '#8BC34A', 'Healthy (0.6-1)']
    ],
    'NDMI': [
        [0, '#F44336', 'Average (0-0.2)'],
        [0.2, '#FF9800', 'Mid-high (0.2-0.4)'],
        [0.4, '#FFEB3B', 'High (0.4-0.6)'],
        [0.6, '#8BC34A', 'Very high (0.6-0.8)'],
        [0.8, '#4CAF50', 'Total (0.8-1)']
    ],
    'NDRVI': [
        [0, '#F44336', 'Stressed (0-0.2)'],
        [0.2, '#FF9800', 'Slightly Stressed (0.2-0.4)'],
        [0.4, '#FFEB3B', 'Moderate (0.4-0.6)'],
        [0.6, '#8BC34A', 'Healthy (0.6-0.8)'],
        [0.8, '#4CAF50', 'Very Healthy (0.8-1)']
    ],
    'RI': [
        [0, '#F44336', 'Very Low (0-1)'],
        [1, '#FF9800', 'Low (1-1.25)'],
        [1.25, '#FFEB3B', 'Normal (1.25-1.5)'],
        [1.5, '#8BC34A', 'High (1.5-1.75)'],
        [1.75, '#4CAF50', 'Very High (1.75+)']
    ],
    'RVI': [
        [0, '#F44336', 'Background (0-0.5)'],
        [0.5, '#FF9800', 'Very Early (0.5-1)'],
        [1, '#FFEB3B', 'Early (1-1.5)'],
        [1.5, '#8BC34A', 'Timely (1.5-2.5)'],
        [2.5, '#4CAF50', 'Slightly Late (2.5+)']
    ],
    'RVI4S1': [
        [0, '#F44336', 'Open (0-1)'],
        [1, '#FF9800', 'Low Dense (1-1.25)'],
        [1.25, '#FFEB3B', 'Slightly Dense (1.25-1.5)'],
        [1.5, '#8BC34A', 'Dense (1.5-1.75)'],
        [1.75, '#4CAF50', 'Highly Dense (1.75+)']
    ],
    'NDBI': [
        [-1, '#800000', 'Extremely Low (-1 to -0.66)'],
        [-0.66, '#F44336', 'Very Low (-0.66 to -0.33)'],
        [-0.33, '#FF9800', 'Low (-0.33 to 0)'],
        [0, '#FFEB3B', 'Normal (0 to 0.33)'],
        [0.33, '#8BC34A', 'High (0.33 to 0.66)'],
        [0.66, '#4CAF50', 'Very High (0.66 to 1)'],
    ],
    'NDCI': [
        [-1, '#800000', 'Extremely Low (-1 to -0.66)'],
        [-0.66, '#F44336', 'Very Low (-0.66 to -0.33)'],
        [-0.33, '#FF9800', 'Low (-0.33 to 0)'],
        [0, '#FFEB3B', 'Normal (0 to 0.33)'],
        [0.33, '#8BC34A', 'High (0.33 to 0.66)'],
        [0.66, '#4CAF50', 'Very High (0.66 to 1)'],
    ],
    'NDESI': [
        [-2, '#800000', 'Extremely Low (-2 to -1.25)'],
        [-1.25, '#F44336', 'Very Low (-1.25 to -0.5)'],
        [-0.5, '#FF9800', 'Low (-0.5 to 0)'],
        [0, '#FFEB3B', 'Normal (0 to 0.5)'],
        [0.5, '#8BC34A', 'High (0.5 to 1.25)'],
        [1.25, '#4CAF50', 'Very High (1.25 to 2)'],
    ],
    'NSI': [
        [0, '#F44336', 'Very Low (0-0.2)'],
        [0.2, '#FF9800', 'Low (0.2-0.4)'],
        [0.4, '#FFEB3B', 'Normal (0.4-0.6)'],
        [0.6, '#8BC34A', 'High (0.6-0.8)'],
        [0.8, '#4CAF50', 'Very High (0.8-1)']
    ],
    'CMI': [
        [0, '#800000', 'Extremely Low (0 to 0.3)'],
        [0.3, '#F44336', 'Very Low (0.3 to 0.8)'],
        [0.8, '#FF9800', 'Low (0.8 to 1)'],
        [1, '#FFEB3B', 'Normal (1 to 1.25)'],
        [1.25, '#8BC34A', 'High (1.25 to 1.5)'],
        [1.5, '#4CAF50', 'Very High (1.5+)'],
    ],
    'FMI': [
        [0, '#800000', 'Extremely Low (0 to 0.3)'],
        [0.3, '#F44336', 'Very Low (0.3 to 0.6)'],
        [0.6, '#FF9800', 'Low (0.6 to 0.9)'],
        [0.9, '#FFEB3B', 'Normal (0.9 to 1.2)'],
        [1.2, '#8BC34A', 'High (1.2 to 1.5)'],
        [1.5, '#4CAF50', 'Very High (1.5+)'],
    ]
}


def index_statistics(index):
    return [
        {'min_value': x[0], 'color': x[1], 'label': x[2]} for x in COLOR_RAMP[index.upper()]
    ]


def get_color_map(index: str):
    color_map = [f'{x[0]},{x[1]}' for x in COLOR_RAMP.get(index.upper()) or []]
    return ';'.join(color_map)


def index_colors(index):
    return [
        (x[0], x[1]) for x in COLOR_RAMP[index]
    ]
