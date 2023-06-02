from abc import ABC, abstractmethod

class IContextAwarenessService(ABC):

    @abstractmethod
    def recognize_location(self, user_id: str):
        """
        Recognizes the user's location.
        :param user_id: The ID of the user.
        :return: The user's current location.
        """
        pass

    @abstractmethod
    def recognize_time_of_day(self, user_id: str):
        """
        Recognizes the current time of day.
        :param user_id: The ID of the user.
        :return: The current time of day.
        """
        pass

    @abstractmethod
    def recognize_current_activity(self, user_id: str):
        """
        Recognizes the user's current activity.
        :param user_id: The ID of the user.
        :return: The user's current activity.
        """
        pass

    @abstractmethod
    def recognize_emotional_state(self, user_id: str):
        """
        Recognizes the user's current emotional state.
        :param user_id: The ID of the user.
        :return: The user's current emotional state.
        """
        pass
