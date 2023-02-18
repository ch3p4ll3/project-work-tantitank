from dataclasses import dataclass
from string import Template


@dataclass
class PublishTopics:
    """Topics for the simulator to publish to."""
    topic: Template = Template('t/simulator/silos/${silos_id}/measurements/${slung}')


@dataclass
class SubscribeTopics:
    """Topics for the simulator to subscribe to."""
    fill: Template = Template('t/simulator/silos/${silos_id}/command/fill')
    empty: Template = Template('t/simulator/silos/${silos_id}/command/empty')
    idle: Template = Template('t/simulator/silos/${silos_id}/command/idle')
    kill: Template = Template('t/simulator/silos/${silos_id}/command/kill')
    start_simulation: Template = Template('t/simulator/silos/${silos_id}/command/start')
    stop_simulation: Template = Template('t/simulator/silos/${silos_id}/command/stop')

    def __iter__(self):
        return iter([self.fill, self.empty, self.idle, self.kill])


@dataclass
class Topics:
    """Topics for the simulator to publish and subscribe to."""
    publish: PublishTopics = PublishTopics()
    subscribe: SubscribeTopics = SubscribeTopics()
