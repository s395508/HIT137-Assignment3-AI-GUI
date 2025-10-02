"""
Base Model Class - Abstract class for all AI models
Demonstrates: Polymorphism, Encapsulation, Method Overriding
Author: Team HIT137 - s395508, s395252, s395343, s395499
"""

from abc import ABC, abstractmethod

class BaseModel(ABC):
    """
    Abstract base class for AI models
    
    OOP CONCEPTS DEMONSTRATED:
    - Polymorphism: Abstract method forces children to implement process()
    - Encapsulation: Private and protected attributes
    """
    
    def __init__(self, model_name, category, description):
        """Initialize base model with encapsulation"""
        self.model_name = model_name
        self.category = category
        self.description = description
        self._pipeline = None  # Protected attribute (Encapsulation)
        self.__is_loaded = False  # Private attribute (Encapsulation)
    
    @abstractmethod
    def process(self, input_data):
        """
        Abstract method - MUST be implemented by child classes
        Demonstrates: POLYMORPHISM
        """
        pass
    
    def load_model(self):
        """
        Base load method - can be overridden
        Demonstrates: METHOD OVERRIDING potential
        """
        print(f"Loading {self.model_name}...")
        self.__is_loaded = True
    
    def is_loaded(self):
        """Getter for private attribute - ENCAPSULATION"""
        return self.__is_loaded
    
    def set_loaded(self, status):
        """Setter for private attribute - ENCAPSULATION"""
        self.__is_loaded = status
    
    def get_info(self):
        """Return model information"""
        return {
            "name": self.model_name,
            "category": self.category,
            "description": self.description,
            "loaded": self.__is_loaded
        }