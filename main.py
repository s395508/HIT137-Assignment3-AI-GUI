"""
Main Entry Point
HIT137 Assignment 3 - AI GUI Application

Team: s395508, s395252, s395343, s395499
"""

from gui.main_window import MainWindow

def main():
    """Main function to launch the application"""
    print("="*50)
    print("HIT137 Assignment 3 - AI GUI Application")
    print("Starting application...")
    print("="*50)
    
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()