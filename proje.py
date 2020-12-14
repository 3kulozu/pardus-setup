#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


#project_folder = "/home/pardus/Masaüstü/proje"
img_folder = "/home/pardus/Masaüstü/proje/wallpaper/macOS-BS2.jpg"
theme_folder = "/home/pardus/Masaüstü/proje/theme/WhiteSur-light/metacity-1/metacity-theme-1.xml"
icon_folder = "/home/pardus/Masaüstü/proje/icon/adwaita-icon-theme/src/cursors/adwaita.svg" 
font_folder = "/home/pardus/Masaüstü/proje/font/lucida-grande/LucidaGrande.ttf"
consolefont_folder= "/usr/share/consolefonts/UbuntuMono-R-8x16.psf"


class Handler:
		def onQuit(self, main_window):
			Gtk.main_quit()
		
		#WALLPAPER
		def onWallpaperClicked(self, change_wallpaper_btn):
			print("Wallpaper button clicked")
			os.system("/home/pardus/Masaüstü/proje/changew.sh /home/pardus/Masaüstü/proje/wallpaper/macOS-BS2.jpg")
			try:
				f = open(img_folder)
				print("Image has already exist")
				f.close()
			except (FileNotFoundError, IOError):
				print("Image not found !")
			
			md1.run()
			md1.hide()
			
		#THEME
		def onThemeClicked(self, change_theme_btn):
			print("Theme button clicked")
			#os.system("xfconf-query -c xsettings -p /Net/ThemeName -s 'WhiteSur'") 
			os.system("xfconf-query -c xsettings -p /Net/ThemeName -s 'WhiteSur-light'")
			
			try:
				f = open(theme_folder)
				print("Theme has already exist")
				f.close()
			except (FileNotFoundError, IOError):
				print("Theme is not found !")
			
			md2.run()
			md2.hide()
			
				
		#ICON
		def onIconClicked(self, change_icon_btn):
			print("Icon button clicked")
			#os.system("gsettings set org.gnome.desktop.interface icon-theme 'Os-Catalina'")
			#os.system("gsettings set org.gnome.desktop.interface icon-theme 'Adwaita'")
			os.system("gsettings set org.gnome.desktop.interface icon-theme 'WhiteSur-dark'")
			#os.system("gsettings set org.gnome.desktop.interface icon-theme 'McMojave Cursors'")
			#os.system("gsettings set org.gnome.desktop.interface icon-theme 'file///home/pardus/Masaüstü/proje/icon/Os-Catalina'")
			
			try:
				f = open(icon_folder)
				print("Icon has already exist")
				f.close()
			except (FileNotFoundError, IOError):
				print("Icon is not found !")
				
			md3.run()
			md3.hide()
					
		#FONT
		def onFontClicked(self, change_font_btn):
			print("Font button clicked")
			#os.system("setfont home/pardus/Masaüstü/proje/font/SanFranciscoDisplay-Light.otf")
			os.system("/home/pardus/Masaüstü/proje/font.sh /home/pardus/Masaüstü/proje/font/lucida-grande/LucidaGrande.ttf")
			#os.system("setfont home/pardus/.fonts/lucida-grande/LucidaGrande.ttf")
			try:
				f = open(font_folder)
				print("Font has already exist !")
				f.close()
			except (FileNotFoundError, IOError):
				print("Font is not found !")
				
			md4.run()
			md4.hide()

		#TERMINAL FONT
		def onConsoleClicked(self, change_console_btn):
			print("Console button clicked")
			print("\n")
			ch = input("Change console fonts [Y/N] : ")
			print("\n\n")
			if ((ch=='Y') or (ch=='N')):
				os.system("ls /usr/share/consolefonts")
				#os.system("setfont /usr/share/consolefonts/UbuntuMono-R-8x16.psf")
			else:
				print(" Console fonts did not change. ")
				
				print("\n\n")
				
			try: 
				f = open(consolefont_folder)
				print("Console fonts are here !")
				f.close()
			except (FileNotFoundError, IOError):
				print("Console fonts are not here !")
					
			
				
			
					
builder = Gtk.Builder()
builder.add_from_file("/home/pardus/Masaüstü/proje/proje.glade")
builder.connect_signals(Handler())

main_window = builder.get_object("main_window")
change_wallpaper_btn = builder.get_object("wallpaper_btn")
change_theme_btn = builder.get_object("theme_btn")
change_icon_btn = builder.get_object("icon_btn")
change_font_btn = builder.get_object("font_btn")
change_console_btn = builder.get_object("console_font_btn")

md1 = builder.get_object("dialog1")
md2 = builder.get_object("dialog2")
md3 = builder.get_object("dialog3")
md4 = builder.get_object("dialog4")

def start():
	print("start function")

start()
main_window.show_all()
print("Show all function...")
Gtk.main()


