"""Functions to prevent a nuclear meltdown."""

def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and neutrons_emitted * temperature < 500000
    

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage_value = (generated_power / theoretical_max_power) * 100

    print(percentage_value)

    if percentage_value >= 80:
        return 'green'
    if 60 <= percentage_value < 80:
        return 'orange'
    if 30 <= percentage_value < 60:
        return 'red'

    return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    state = temperature * neutrons_produced_per_second
    lower_threshold = threshold * 0.9
    upper_threshold = threshold * 1.1

    if lower_threshold > state:
        return 'LOW'
    if upper_threshold > state:
        return 'NORMAL'
    
    return 'DANGER' 
