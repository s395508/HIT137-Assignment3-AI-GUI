"""
Sentiment Analysis Model (Model 1)
Demonstrates: Inheritance, Method Overriding, Multiple Decorators
"""

from models.base_model import BaseModel
from utils.decorators import (timing_decorator, error_handler_decorator, 
                              logging_decorator, validation_decorator)
from transformers import pipeline

class SentimentModel(BaseModel):
    """
    Sentiment Analysis Model
    DEMONSTRATES: INHERITANCE, METHOD OVERRIDING, POLYMORPHISM
    """
    
    def __init__(self):
        """Initialize - calls parent constructor"""
        super().__init__(
            model_name="DistilBERT Sentiment Analyzer",
            category="Text Classification",
            description="Analyzes if text is positive or negative"
        )
        self.hf_model = "distilbert-base-uncased-finetuned-sst-2-english"
    
    def load_model(self):
        """
        Override parent's load_model
        Demonstrates: METHOD OVERRIDING
        """
        super().load_model()  # Call parent method
        print(f"Loading sentiment pipeline...")
        self._pipeline = pipeline("sentiment-analysis", model=self.hf_model)
        self.set_loaded(True)
        print("✅ Sentiment model ready!")
    
    @timing_decorator
    @error_handler_decorator
    @logging_decorator
    @validation_decorator
    def process(self, input_data):
        """
        Process text - DEMONSTRATES: POLYMORPHISM + MULTIPLE DECORATORS
        """
        if not self.is_loaded():
            self.load_model()
        
        print(f"Analyzing: '{input_data[:50]}...'")
        result = self._pipeline(input_data)[0]
        
        label = result['label']
        score = result['score'] * 100
        
        output = f"""
╔══════════════════════════════════════╗
║     SENTIMENT ANALYSIS RESULT        ║
╚══════════════════════════════════════╝

Input: {input_data}

Sentiment: {label}
Confidence: {score:.2f}%

{'😊 Positive!' if label == 'POSITIVE' else '😔 Negative!'}
"""
        return output
    
    def get_info(self):
        """Override to add specific info - METHOD OVERRIDING"""
        info = super().get_info()
        info["huggingface_model"] = self.hf_model
        info["input_type"] = "Text"
        return info