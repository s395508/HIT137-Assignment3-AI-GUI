"""
Image Classification Model (Model 2)
Demonstrates: Inheritance, Method Overriding, Multiple Decorators
"""

from models.base_model import BaseModel
from utils.decorators import (timing_decorator, error_handler_decorator,
                              logging_decorator, validation_decorator)
from transformers import pipeline
from PIL import Image

class ImageClassificationModel(BaseModel):
    """
    Image Classification Model
    DEMONSTRATES: INHERITANCE, METHOD OVERRIDING, POLYMORPHISM
    """
    
    def __init__(self):
        """Initialize with parent constructor"""
        super().__init__(
            model_name="Vision Transformer (ViT)",
            category="Computer Vision",
            description="Identifies objects in images"
        )
        self.hf_model = "google/vit-base-patch16-224"
    
    def load_model(self):
        """
        Override parent's load_model
        Demonstrates: METHOD OVERRIDING
        """
        super().load_model()
        print(f"Loading image classification pipeline...")
        self._pipeline = pipeline("image-classification", model=self.hf_model)
        self.set_loaded(True)
        print("✅ Image model ready!")
    
    @timing_decorator
    @error_handler_decorator
    @logging_decorator
    @validation_decorator
    def process(self, input_data):
        """
        Process image - DEMONSTRATES: POLYMORPHISM + MULTIPLE DECORATORS
        """
        if not self.is_loaded():
            self.load_model()
        
        print(f"Classifying image: {input_data}")
        image = Image.open(input_data)
        results = self._pipeline(image)
        
        output = """
╔══════════════════════════════════════╗
║   IMAGE CLASSIFICATION RESULTS       ║
╚══════════════════════════════════════╝

Top 5 Predictions:

"""
        for i, result in enumerate(results[:5], 1):
            label = result['label']
            score = result['score'] * 100
            bar = "█" * int(score / 5)
            output += f"{i}. {label:.<30} {score:>6.2f}%\n   {bar}\n\n"
        
        return output
    
    def get_info(self):
        """Override for specific info - METHOD OVERRIDING"""
        info = super().get_info()
        info["huggingface_model"] = self.hf_model
        info["input_type"] = "Image"
        return info