# Filename: proactivity_service.py

from abc import ABC, abstractmethod

class IProactivityService(ABC):

    @abstractmethod
    def learn_from_interactions(self, user_id: str):
        """
        Learns from the user's past interactions to better anticipate their needs.
        :param user_id: The ID of the user.
        """
        pass

    @abstractmethod
    def offer_suggestions(self, user_id: str):
        """
        Proactively offers suggestions to the user based on their needs and preferences.
        :param user_id: The ID of the user.
        :return: A list of suggestions for the user.
        """
        pass

    @abstractmethod
    def set_reminders(self, user_id: str):
        """
        Sets reminders for the user based on their needs and preferences.
        :param user_id: The ID of the user.
        """
        pass

    @abstractmethod
    def provide_relevant_information(self, user_id: str):
        """
        Provides relevant information to the user based on their needs and preferences.
        :param user_id: The ID of the user.
        :return: A list of relevant information for the user.
        """
        pass
