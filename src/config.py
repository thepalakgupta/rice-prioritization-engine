# Configuration file for RICE Calculator

RICE_COMPONENTS = {
    'reach': {
        'description': 'Number of users/customers affected',
        'min': 0,
        'max': 1000000
    },
    'impact': {
        'description': 'Impact magnitude per user',
        'scale': {
            3: 'Major (3x)',
            2: 'Medium (2x)', 
            1: 'Minor (1x)',
            0.5: 'Minimal (0.5x)'
        }
    },
    'confidence': {
        'description': 'Confidence in Reach and Impact estimates',
        'scale': '0-100%'
    },
    'effort': {
        'description': 'Work required in days',
        'min': 1,
        'max': 365
    }
}

FORMULA = "(Reach × Impact × Confidence) / Effort"