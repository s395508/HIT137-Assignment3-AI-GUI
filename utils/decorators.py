"""
Custom Decorators - Demonstrates MULTIPLE DECORATORS
Author: Team HIT137
"""

import time
import functools

def timing_decorator(func):
    """Decorator #1: Measures execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"\n⏱️  Starting {func.__name__}...")
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"✅ Completed in {elapsed:.2f} seconds")
        return result
    return wrapper

def error_handler_decorator(func):
    """Decorator #2: Handles errors gracefully"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_msg = f"❌ Error in {func.__name__}: {str(e)}"
            print(error_msg)
            return error_msg
    return wrapper

def logging_decorator(func):
    """Decorator #3: Logs function execution"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📝 Executing: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"📝 Finished: {func.__name__}")
        return result
    return wrapper

def validation_decorator(func):
    """Decorator #4: Validates input is not empty"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > 1:
            input_data = args[1]
            if input_data is None or (isinstance(input_data, str) and input_data.strip() == ""):
                return "⚠️  Error: Input cannot be empty"
        return func(*args, **kwargs)
    return wrapper