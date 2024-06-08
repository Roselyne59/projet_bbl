import tkinter as tk
import re
from tkinter import messagebox
from tkcalendar import DateEntry
from book import Book
from bookManager import BookManager


#liste déroulente pour genres

class BookApp :
    def __init__(self, root) :
        self.root = root
        self.root.title("Gestion des livres")

        screen_width = self.root.get_screenwd()
        screen_height = self.root.get_screenhg()

        windows_width = int(screen_width * 0.8)
        windows_height = int(screen_height * 0.8)

        position_x = (screen_width // 2) - (windows_width // 2)
        position_y = (screen_height // 2) - (windows_height // 2)

