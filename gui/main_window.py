"""
Main GUI Window
Demonstrates: MULTIPLE INHERITANCE, ENCAPSULATION
Author: Team HIT137
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox

class InputHandler:
    """Mixin class for input handling"""
    def get_text_input(self):
        return self.text_input.get("1.0", "end-1c")
    def clear_inputs(self):
        self.text_input.delete("1.0", tk.END)
        self.file_path_var.set("")

class OutputHandler:
    """Mixin class for output handling"""
    def display_output(self, text):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", text)
        self.output_text.config(state=tk.DISABLED)
    def clear_output(self):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)

class MainWindow(InputHandler, OutputHandler, tk.Tk):
    """Main Window - DEMONSTRATES MULTIPLE INHERITANCE"""
    def __init__(self):
        super().__init__()
        self.__sentiment_model = None
        self.__image_model = None
        self.title("HIT137 - AI GUI Application")
        self.geometry("1200x850")
        self.configure(bg="#f5f5f5")
        self._create_all_widgets()
    
    def _create_all_widgets(self):
        self._create_menu()
        self._create_header()
        self._create_model_section()
        
        # Container for input/output side by side
        middle_container = tk.Frame(self, bg="#f5f5f5")
        middle_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        
        self._create_input_section(middle_container)
        self._create_output_section(middle_container)
        
        self._create_info_section()
        self._create_status()
    
    def _create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear All", command=self._clear_all)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        models_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Models", menu=models_menu)
        models_menu.add_command(label="Model 1 Info", command=self._show_model1_info)
        models_menu.add_command(label="Model 2 Info", command=self._show_model2_info)
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="OOP Concepts", command=self._show_oop)
        help_menu.add_command(label="About", command=self._show_about)
    
    def _create_header(self):
        header = tk.Frame(self, bg="#2c3e50", height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        title = tk.Label(header, text="🤖 AI Model Integration System", 
                        font=("Arial", 20, "bold"), bg="#2c3e50", fg="white")
        title.pack(pady=12)
    
    def _create_model_section(self):
        frame = tk.LabelFrame(self, text="Model Selection & Loading", 
                             font=("Arial", 10, "bold"), bg="#f5f5f5", 
                             padx=15, pady=12, relief=tk.GROOVE, bd=2)
        frame.pack(fill=tk.X, padx=20, pady=10)
        
        btn1 = tk.Button(frame, text="📝 Load Model 1: Sentiment Analysis",
                        command=self._load_model1, bg="#3498db", fg="white",
                        font=("Arial", 10, "bold"), padx=20, pady=10,
                        relief=tk.RAISED, bd=2, cursor="hand2")
        btn1.pack(side=tk.LEFT, padx=8, expand=True, fill=tk.X)
        
        btn2 = tk.Button(frame, text="🖼️ Load Model 2: Image Classification",
                        command=self._load_model2, bg="#27ae60", fg="white",
                        font=("Arial", 10, "bold"), padx=20, pady=10,
                        relief=tk.RAISED, bd=2, cursor="hand2")
        btn2.pack(side=tk.LEFT, padx=8, expand=True, fill=tk.X)
    
    def _create_input_section(self, parent):
        frame = tk.LabelFrame(parent, text="User Input Section", 
                             font=("Arial", 10, "bold"), bg="#f5f5f5", 
                             padx=12, pady=12, relief=tk.GROOVE, bd=2)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))
        
        # Input type selection
        type_frame = tk.Frame(frame, bg="#f5f5f5")
        type_frame.pack(fill=tk.X, pady=(0, 8))
        
        tk.Label(type_frame, text="Input Type:", font=("Arial", 9, "bold"), 
                bg="#f5f5f5").pack(side=tk.LEFT, padx=(0, 10))
        
        self.input_type = tk.StringVar(value="text")
        tk.Radiobutton(type_frame, text="Text", variable=self.input_type, 
                      value="text", bg="#f5f5f5", font=("Arial", 9),
                      command=self._toggle_input, cursor="hand2").pack(side=tk.LEFT, padx=8)
        tk.Radiobutton(type_frame, text="Image", variable=self.input_type, 
                      value="image", bg="#f5f5f5", font=("Arial", 9),
                      command=self._toggle_input, cursor="hand2").pack(side=tk.LEFT, padx=8)
        
        # Text input
        self.text_frame = tk.Frame(frame, bg="#f5f5f5")
        self.text_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.text_frame, text="Enter Text:", font=("Arial", 9, "bold"),
                bg="#f5f5f5").pack(anchor=tk.W, pady=(0, 3))
        
        self.text_input = scrolledtext.ScrolledText(self.text_frame, height=8, 
                                                    font=("Arial", 10), wrap=tk.WORD,
                                                    relief=tk.SOLID, bd=1)
        self.text_input.pack(fill=tk.BOTH, expand=True)
        
        # Image input
        self.image_frame = tk.Frame(frame, bg="#f5f5f5")
        
        tk.Label(self.image_frame, text="Select Image File:", 
                font=("Arial", 9, "bold"), bg="#f5f5f5").pack(anchor=tk.W, pady=(0, 3))
        
        file_frame = tk.Frame(self.image_frame, bg="#f5f5f5")
        file_frame.pack(fill=tk.X, pady=(0, 8))
        
        self.file_path_var = tk.StringVar()
        tk.Entry(file_frame, textvariable=self.file_path_var, 
                font=("Arial", 9), state="readonly", relief=tk.SOLID, bd=1).pack(
                    side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))
        
        tk.Button(file_frame, text="Browse", command=self._browse_file,
                 bg="#95a5a6", fg="white", font=("Arial", 9, "bold"),
                 padx=15, pady=5, relief=tk.RAISED, bd=2, cursor="hand2").pack(side=tk.LEFT)
        
        # Action buttons
        btn_frame = tk.Frame(frame, bg="#f5f5f5")
        btn_frame.pack(fill=tk.X, pady=(12, 0))
        
        tk.Button(btn_frame, text="Run Model 1", command=self._run_model1,
                 bg="#e74c3c", fg="white", font=("Arial", 9, "bold"),
                 padx=15, pady=8, relief=tk.RAISED, bd=2, cursor="hand2").pack(
                     side=tk.LEFT, padx=(0, 5), expand=True, fill=tk.X)
        
        tk.Button(btn_frame, text="Run Model 2", command=self._run_model2,
                 bg="#9b59b6", fg="white", font=("Arial", 9, "bold"),
                 padx=15, pady=8, relief=tk.RAISED, bd=2, cursor="hand2").pack(
                     side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        tk.Button(btn_frame, text="Clear", command=self._clear_all,
                 bg="#7f8c8d", fg="white", font=("Arial", 9, "bold"),
                 padx=15, pady=8, relief=tk.RAISED, bd=2, cursor="hand2").pack(
                     side=tk.LEFT, padx=(5, 0), expand=True, fill=tk.X)
    
    def _create_output_section(self, parent):
        frame = tk.LabelFrame(parent, text="Model Output Section", 
                             font=("Arial", 10, "bold"), bg="#f5f5f5", 
                             padx=12, pady=12, relief=tk.GROOVE, bd=2)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(8, 0))
        
        tk.Label(frame, text="Output Display:", font=("Arial", 9, "bold"),
                bg="#f5f5f5").pack(anchor=tk.W, pady=(0, 5))
        
        self.output_text = scrolledtext.ScrolledText(frame, height=12, 
                                                     font=("Courier", 9), 
                                                     state=tk.DISABLED, wrap=tk.WORD,
                                                     relief=tk.SOLID, bd=1, bg="white")
        self.output_text.pack(fill=tk.BOTH, expand=True)
    
    def _create_info_section(self):
        frame = tk.LabelFrame(self, text="Model Information & OOP Explanation", 
                             font=("Arial", 10, "bold"), bg="#f5f5f5", 
                             padx=12, pady=10, relief=tk.GROOVE, bd=2)
        frame.pack(fill=tk.X, padx=20, pady=(5, 10))
        
        # Info container with two columns
        info_container = tk.Frame(frame, bg="#f5f5f5")
        info_container.pack(fill=tk.BOTH, expand=True)
        
        # Left column - Model Info
        left_frame = tk.Frame(info_container, bg="#f5f5f5")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        tk.Label(left_frame, text="Selected Model Info:", 
                font=("Arial", 9, "bold"), bg="#f5f5f5").pack(anchor=tk.W, pady=(0, 5))
        
        model_info = """• Model Name
- Category (Text, Vision, Audio)
- Short Description"""
        tk.Label(left_frame, text=model_info, font=("Arial", 8),
                bg="#f5f5f5", justify=tk.LEFT, fg="#333333").pack(anchor=tk.W, padx=5)
        
        # Right column - OOP Concepts
        right_frame = tk.Frame(info_container, bg="#f5f5f5")
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(right_frame, text="OOP Concepts Explanation:", 
                font=("Arial", 9, "bold"), bg="#f5f5f5").pack(anchor=tk.W, pady=(0, 5))
        
        oop_info = """• Where Multiple Inheritance applied
- Why Encapsulation was applied
- How Polymorphism and Method
  Overriding are shown
- Where Multiple Decorators are applied"""
        tk.Label(right_frame, text=oop_info, font=("Arial", 8),
                bg="#f5f5f5", justify=tk.LEFT, fg="#333333").pack(anchor=tk.W, padx=5)
        
        # Notes at bottom
        tk.Label(frame, text="Notes   Extra notes, instructions, or references.",
                font=("Arial", 8, "italic"), bg="#f5f5f5", 
                fg="#666666").pack(anchor=tk.W, pady=(8, 0))
    
    def _create_status(self):
        self.status_var = tk.StringVar(value="Ready")
        status = tk.Label(self, textvariable=self.status_var, bd=1, relief=tk.SUNKEN,
                         anchor=tk.W, font=("Arial", 9), bg="#ecf0f1", fg="#2c3e50")
        status.pack(side=tk.BOTTOM, fill=tk.X)
    
    def _toggle_input(self):
        if self.input_type.get() == "text":
            self.image_frame.pack_forget()
            self.text_frame.pack(fill=tk.BOTH, expand=True)
        else:
            self.text_frame.pack_forget()
            self.image_frame.pack(fill=tk.BOTH, expand=True)
    
    def _browse_file(self):
        filename = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if filename:
            self.file_path_var.set(filename)
    
    def _load_model1(self):
        self.status_var.set("Loading Model 1...")
        self.update()
        try:
            from models.sentiment_model import SentimentModel
            self.__sentiment_model = SentimentModel()
            self.__sentiment_model.load_model()
            messagebox.showinfo("Success", "Model 1 loaded successfully!")
            self.status_var.set("Model 1 loaded")
        except Exception as e:
            messagebox.showerror("Error", f"Failed: {str(e)}")
            self.status_var.set("Error")
    
    def _load_model2(self):
        self.status_var.set("Loading Model 2...")
        self.update()
        try:
            from models.image_model import ImageClassificationModel
            self.__image_model = ImageClassificationModel()
            self.__image_model.load_model()
            messagebox.showinfo("Success", "Model 2 loaded successfully!")
            self.status_var.set("Model 2 loaded")
        except Exception as e:
            messagebox.showerror("Error", f"Failed: {str(e)}")
            self.status_var.set("Error")
    
    def _run_model1(self):
        if self.__sentiment_model is None:
            messagebox.showwarning("Warning", "Load Model 1 first!")
            return
        if self.input_type.get() != "text":
            messagebox.showwarning("Warning", "Model 1 needs text!")
            return
        text = self.get_text_input()
        if not text.strip():
            messagebox.showwarning("Warning", "Enter text!")
            return
        self.status_var.set("Processing...")
        self.update()
        result = self.__sentiment_model.process(text)
        self.display_output(result)
        self.status_var.set("Completed")
    
    def _run_model2(self):
        if self.__image_model is None:
            messagebox.showwarning("Warning", "Load Model 2 first!")
            return
        if self.input_type.get() != "image":
            messagebox.showwarning("Warning", "Model 2 needs image!")
            return
        image_path = self.file_path_var.get()
        if not image_path:
            messagebox.showwarning("Warning", "Select image!")
            return
        self.status_var.set("Processing...")
        self.update()
        result = self.__image_model.process(image_path)
        self.display_output(result)
        self.status_var.set("Completed")
    
    def _clear_all(self):
        self.clear_inputs()
        self.clear_output()
        self.status_var.set("Cleared")
    
    def _show_model1_info(self):
        info = """MODEL 1: Sentiment Analysis

Name: DistilBERT Sentiment Analyzer
Category: Text Classification
Model: distilbert-base-uncased-finetuned-sst-2-english

Description:
Analyzes sentiment of text input and classifies
as POSITIVE or NEGATIVE with confidence score.

Input: Text strings
Output: Sentiment label + confidence %"""
        messagebox.showinfo("Model 1 Information", info)
    
    def _show_model2_info(self):
        info = """MODEL 2: Image Classification

Name: Vision Transformer (ViT)
Category: Computer Vision
Model: google/vit-base-patch16-224

Description:
Identifies and classifies objects in images.
Returns top 5 predictions with confidence scores.

Input: Image files (JPG, PNG, BMP, GIF)
Output: Top 5 object labels + confidence %"""
        messagebox.showinfo("Model 2 Information", info)
    
    def _show_oop(self):
        info = """OOP CONCEPTS IMPLEMENTED:

1. MULTIPLE INHERITANCE
   MainWindow inherits from 3 classes

2. ENCAPSULATION
   Private attributes protect internal state

3. POLYMORPHISM
   Abstract process() method

4. METHOD OVERRIDING
   Child classes override parent methods

5. MULTIPLE DECORATORS
   4 decorators stacked on process()

See code for detailed implementation!"""
        messagebox.showinfo("OOP Concepts", info)
    
    def _show_about(self):
        about = """HIT137 Assignment 3
AI GUI Application with OOP Concepts

Team Members:
- s395508
- s395252 - Ankita
- s395343 - Plamveerbrar
- s395499 - Sehaj

Technologies:
- Python + Tkinter
- Hugging Face Transformers
- PIL Image Processing

Version: 1.0
Semester: S1 2025"""
        messagebox.showinfo("About", about)