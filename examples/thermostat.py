from kvencoder import Encodable


class Thermostat(Encodable):

    def __init__(self, temperature, damping, applies_to_hydrogen):
        self.temperature = temperature
        self.damping = damping
        self.applies_to_hydrogen = applies_to_hydrogen

    @property
    def _schema(self):
        return "thermostat.yaml"

    @property
    def _encoders(self):
        return {'yes_no': lambda x: ('no', 'yes')[x],
                'on_off': lambda x: ('off', 'on')[x],
                'enum': lambda x: x.value,
                'iter': lambda x: ' '.join(str(xs) for xs in x),
                'two_digit_iter': lambda xs: ' '.join(f'{x:.2f}' for x in xs)}


if __name__ == '__main__':
    t = Thermostat(temperature=300, damping=5, applies_to_hydrogen=False)

    t.encode(path='thermostat.conf')
